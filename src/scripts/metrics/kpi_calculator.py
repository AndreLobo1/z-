"""
Módulo de Cálculo de KPIs e Fichas Matemáticas de Negócio.
Calcula o catálogo principal e complementar de KPIs usado na documentação.
"""

import numpy as np
import pandas as pd


def _numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce") if series is not None else pd.Series(dtype=float)


def _date(series: pd.Series) -> pd.Series:
    return pd.to_datetime(series, errors="coerce", dayfirst=True) if series is not None else pd.Series(dtype="datetime64[ns]")


def _pct_to_float(series: pd.Series) -> pd.Series:
    if series is None:
        return pd.Series(dtype=float)
    cleaned = (
        series.astype(str)
        .str.replace("%", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.strip()
    )
    return pd.to_numeric(cleaned, errors="coerce")


def _normalize_assoc(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower() if series is not None else pd.Series(dtype=str)


def _safe_pct(numerator: float, denominator: float) -> float:
    return round(float(numerator / denominator * 100.0), 2) if denominator else 0.0


def _safe_mean(series: pd.Series) -> float:
    cleaned = series.dropna()
    return round(float(cleaned.mean()), 2) if not cleaned.empty else 0.0


def _safe_median(series: pd.Series) -> float:
    cleaned = series.dropna()
    return round(float(cleaned.median()), 2) if not cleaned.empty else 0.0


def _mode_rate(series: pd.Series) -> float:
    cleaned = series.dropna().astype(str).str.strip()
    if cleaned.empty:
        return 0.0
    return round(float(cleaned.value_counts(normalize=True).iloc[0] * 100.0), 2)


def _quarter_key(date_series: pd.Series) -> pd.Series:
    return date_series.dt.to_period("Q").astype(str)


def calculate_kpis(datasets: dict) -> list:
    """Calcula o catálogo expandido de KPIs de negócio."""
    df_clientes = datasets.get("clientes", pd.DataFrame())
    df_empresas = datasets.get("empresas", pd.DataFrame())
    df_pesquisas = datasets.get("pesquisas", pd.DataFrame())
    df_questoes = datasets.get("questoes", pd.DataFrame())
    df_respondentes = datasets.get("respondentes", pd.DataFrame())
    df_respostas = datasets.get("respostas", pd.DataFrame())

    pesquisas_dates = _date(df_pesquisas["data_solicitacao"]) if "data_solicitacao" in df_pesquisas.columns else pd.Series(dtype="datetime64[ns]")
    participantes = _numeric(df_pesquisas["participantes"]) if "participantes" in df_pesquisas.columns else pd.Series(dtype=float)
    tempo_preenchimento = _numeric(df_pesquisas["tempo_preenchimento"]) if "tempo_preenchimento" in df_pesquisas.columns else pd.Series(dtype=float)
    dias_entrega = _numeric(df_pesquisas["dias_uteis_para_entrega"]) if "dias_uteis_para_entrega" in df_pesquisas.columns else pd.Series(dtype=float)
    dias_aberta = _numeric(df_pesquisas["dias úteis aberta"]) if "dias úteis aberta" in df_pesquisas.columns else pd.Series(dtype=float)
    dias_tabulacao = _numeric(df_pesquisas["dias para tabulação"]) if "dias para tabulação" in df_pesquisas.columns else pd.Series(dtype=float)
    dias_ciclo = _numeric(df_pesquisas["dias entre a solicitação e a divulgação"]) if "dias entre a solicitação e a divulgação" in df_pesquisas.columns else pd.Series(dtype=float)
    mercado_pct = _pct_to_float(df_empresas["% de mercado"]) if "% de mercado" in df_empresas.columns else pd.Series(dtype=float)

    total_pesquisas = len(df_pesquisas)
    total_questoes = len(df_questoes)
    total_respostas = len(df_respostas)
    total_participacoes = len(df_respondentes)
    total_empresas = len(df_empresas)
    empresas_participantes_unicas = df_respondentes["id_empresa"].nunique(dropna=True) if "id_empresa" in df_respondentes.columns else 0
    empresas_associadas = len(df_empresas[_normalize_assoc(df_empresas["Associado"]).isin(["sim", "s", "true", "1"])]) if "Associado" in df_empresas.columns else 0

    period_counts = pd.Series(dtype=int)
    latest_period = None
    prev_period = None
    if not pesquisas_dates.dropna().empty:
        period_counts = _quarter_key(pesquisas_dates).value_counts().sort_index()
        if len(period_counts) > 0:
            latest_period = period_counts.index[-1]
        if len(period_counts) > 1:
            prev_period = period_counts.index[-2]

    if "ID" in df_empresas.columns:
        mercado_lookup = pd.DataFrame({"ID": df_empresas["ID"].astype(str), "mercado_pct": mercado_pct})
        empresa_ids = df_empresas["ID"].astype(str)
    else:
        mercado_lookup = pd.DataFrame(columns=["ID", "mercado_pct"])
        empresa_ids = pd.Series(dtype=str)

    empresas_participantes_set = set(df_respondentes["id_empresa"].dropna().astype(str)) if "id_empresa" in df_respondentes.columns else set()
    empresas_nunca = int((~empresa_ids.isin(empresas_participantes_set)).sum()) if not empresa_ids.empty else 0
    participacoes_por_empresa = df_respondentes["id_empresa"].dropna().astype(str).value_counts() if "id_empresa" in df_respondentes.columns else pd.Series(dtype=int)
    empresas_recorrentes = int((participacoes_por_empresa >= 2).sum()) if not participacoes_por_empresa.empty else 0
    empresas_participantes_df = df_empresas[df_empresas["ID"].astype(str).isin(empresas_participantes_set)].copy() if "ID" in df_empresas.columns else pd.DataFrame()
    associadas_participantes = 0
    if not empresas_participantes_df.empty and "Associado" in empresas_participantes_df.columns:
        associadas_participantes = int(_normalize_assoc(empresas_participantes_df["Associado"]).isin(["sim", "s", "true", "1"]).sum())

    latest_period_count = int(period_counts.get(latest_period, 0)) if latest_period is not None else 0
    latest_completed_count = 0
    if latest_period is not None and "status" in df_pesquisas.columns:
        latest_mask = _quarter_key(pesquisas_dates) == latest_period
        completed_mask = df_pesquisas["status"].astype(str).str.lower().isin(["concluída", "concluida", "finalizada"])
        latest_completed_count = int((latest_mask & completed_mask).sum())

    growth_pct = 0.0
    if latest_period is not None and prev_period is not None and period_counts.get(prev_period, 0) > 0:
        growth_pct = round(float((period_counts.get(latest_period, 0) - period_counts.get(prev_period, 0)) / period_counts.get(prev_period, 0) * 100.0), 2)

    participantes_mercado = mercado_lookup[mercado_lookup["ID"].isin(empresas_participantes_set)] if not mercado_lookup.empty else pd.DataFrame(columns=["ID", "mercado_pct"])
    cobertura_total = round(float(participantes_mercado["mercado_pct"].dropna().sum()), 2) if not participantes_mercado.empty else 0.0
    cobertura_media_por_pesquisa = 0.0
    cobertura_growth = 0.0
    if not df_respondentes.empty and "id_pesq" in df_respondentes.columns and "id_empresa" in df_respondentes.columns and not mercado_lookup.empty:
        cobertura_df = df_respondentes[["id_pesq", "id_empresa"]].dropna().copy()
        cobertura_df["id_empresa"] = cobertura_df["id_empresa"].astype(str)
        cobertura_df["id_pesq"] = cobertura_df["id_pesq"].astype(str)
        cobertura_df = cobertura_df.drop_duplicates()
        cobertura_df = cobertura_df.merge(mercado_lookup, left_on="id_empresa", right_on="ID", how="left")
        cobertura_por_pesquisa = cobertura_df.groupby("id_pesq")["mercado_pct"].sum(min_count=1)
        cobertura_media_por_pesquisa = round(float(cobertura_por_pesquisa.dropna().mean()), 2) if not cobertura_por_pesquisa.dropna().empty else 0.0
        if "id" in df_pesquisas.columns and not pesquisas_dates.dropna().empty:
            periodo_pesquisa = pd.DataFrame({"id_pesq": df_pesquisas["id"].astype(str), "periodo": _quarter_key(pesquisas_dates)}).dropna()
            cobertura_periodo = cobertura_por_pesquisa.reset_index().merge(periodo_pesquisa, on="id_pesq", how="left")
            cobertura_periodo = cobertura_periodo.groupby("periodo")["mercado_pct"].mean().sort_index()
            if len(cobertura_periodo) > 1 and cobertura_periodo.iloc[-2] != 0:
                cobertura_growth = round(float((cobertura_periodo.iloc[-1] - cobertura_periodo.iloc[-2]) / cobertura_periodo.iloc[-2] * 100.0), 2)

    top_share_participantes = 0
    if not participantes_mercado.empty:
        positivos = mercado_lookup["mercado_pct"].dropna()
        threshold = positivos.quantile(0.75) if not positivos.empty else np.nan
        if pd.notna(threshold):
            top_share_participantes = int((participantes_mercado["mercado_pct"] >= threshold).sum())

    questoes_tipo = df_questoes["tipo"].astype(str).str.strip().str.lower() if "tipo" in df_questoes.columns else pd.Series(dtype=str)
    questoes_conf = df_questoes["confianca"].astype(str).str.strip().str.lower() if "confianca" in df_questoes.columns else pd.Series(dtype=str)
    qtd_alternativas = _numeric(df_questoes["qtd_alternativas"]) if "qtd_alternativas" in df_questoes.columns else pd.Series(dtype=float)
    geo_states = int(empresas_participantes_df["Estado"].dropna().astype(str).str.strip().nunique()) if "Estado" in empresas_participantes_df.columns else 0
    total_questoes_fechadas = int(questoes_tipo.isin(["multipla_escolha", "caixas_de_selecao", "matriz_avaliacao", "numerica"]).sum()) if not questoes_tipo.empty else 0
    total_questoes_abertas = int((questoes_tipo == "aberta").sum()) if not questoes_tipo.empty else 0
    total_questoes_matriz = int(questoes_tipo.str.contains("matriz", na=False).sum()) if not questoes_tipo.empty else 0
    confianca_alta = int((questoes_conf == "alta").sum()) if not questoes_conf.empty else 0
    media_respostas_pergunta = (total_respostas / total_questoes) if total_questoes > 0 else 0.0

    return [
        {"id": "KPI-01", "name": "Volume Total de Pesquisas", "objective": "Medir a escala do catálogo de pesquisas setoriais do Sidusfarma.", "granularity": "Global (Sidusfarma)", "numerator": "Contagem de registros na tabela pesquisas", "denominator": "N/A (Contagem absoluta)", "formula": "COUNT(pesquisas.id)", "value": float(total_pesquisas), "unit": "pesquisas", "category": "Volume"},
        {"id": "KPI-02", "name": "Taxa de Conclusão de Pesquisas", "objective": "Avaliar o percentual de pesquisas que atingiram o status finalizado.", "granularity": "Global (Sidusfarma)", "numerator": "Pesquisas com status finalizado", "denominator": "Total de pesquisas cadastradas", "formula": "(Pesquisas finalizadas / Total pesquisas) * 100", "value": float(_safe_pct(len(df_pesquisas[df_pesquisas["status"].astype(str).str.lower().isin(["concluída", "concluida", "finalizada"])]) if "status" in df_pesquisas.columns else 0, total_pesquisas)), "unit": "percentual", "category": "Eficiência"},
        {"id": "KPI-03", "name": "Média de Participantes por Pesquisa", "objective": "Medir a adesão média de respondentes por instrumento de pesquisa.", "granularity": "Por Pesquisa", "numerator": "Total de registros de participação em respondentes", "denominator": "Total de pesquisas cadastradas", "formula": "COUNT(respondentes) / COUNT(pesquisas)", "value": round(float(total_participacoes / total_pesquisas), 2) if total_pesquisas else 0.0, "unit": "respondentes/pesquisa", "category": "Engajamento"},
        {"id": "KPI-04", "name": "Taxa de Empresas Associadas Cadastradas", "objective": "Mapear a proporção de empresas que possuem vínculo associativo formal.", "granularity": "Global (Empresas)", "numerator": "Empresas associadas", "denominator": "Total de empresas cadastradas", "formula": "(Empresas associadas / Total empresas) * 100", "value": float(_safe_pct(empresas_associadas, total_empresas)), "unit": "percentual", "category": "Cadastro"},
        {"id": "KPI-05", "name": "Taxa de Adesão de Empresas", "objective": "Medir a cobertura geral de empresas ativas em pesquisas sobre o total cadastrado.", "granularity": "Por Empresa", "numerator": "Empresas distintas presentes em respondentes", "denominator": "Total de empresas no cadastro", "formula": "(Empresas distintas com resposta / Total empresas cadastradas) * 100", "value": float(_safe_pct(empresas_participantes_unicas, total_empresas)), "unit": "percentual", "category": "Engajamento"},
        {"id": "KPI-06", "name": "Taxa de Adesão das Associadas", "objective": "Medir a adesão focalizando a base estratégica de empresas associadas.", "granularity": "Por Empresa Associada", "numerator": "Empresas distintas presentes em respondentes", "denominator": "Total de empresas associadas", "formula": "(Empresas distintas com resposta / Empresas associadas) * 100", "value": float(_safe_pct(empresas_participantes_unicas, empresas_associadas)), "unit": "percentual", "category": "Engajamento"},
        {"id": "KPI-07", "name": "Tempo Médio de Preenchimento", "objective": "Medir o esforço necessário do respondente para completar uma pesquisa.", "granularity": "Por Pesquisa", "numerator": "Soma da duração em minutos das pesquisas", "denominator": "Pesquisas com tempo preenchido", "formula": "MEAN(pesquisas.tempo_preenchimento)", "value": float(_safe_mean(tempo_preenchimento)), "unit": "minutos", "category": "Usabilidade"},
        {"id": "KPI-08", "name": "Tempo Médio de Entrega de Resultados", "objective": "Avaliar a agilidade operacional na tabulação e divulgação dos relatórios.", "granularity": "Global (Sidusfarma)", "numerator": "Soma dos dias úteis de entrega", "denominator": "Pesquisas com prazo computado", "formula": "MEAN(pesquisas.dias_uteis_para_entrega)", "value": float(_safe_mean(dias_entrega)), "unit": "dias úteis", "category": "Desempenho Operacional"},
        {"id": "KPI-09", "name": "Média de Questões por Instrumento", "objective": "Medir a extensão dos questionários elaborados.", "granularity": "Por Pesquisa", "numerator": "Total de questões cadastradas", "denominator": "Total de pesquisas cadastradas", "formula": "COUNT(questoes) / COUNT(pesquisas)", "value": round(float(total_questoes / total_pesquisas), 2) if total_pesquisas else 0.0, "unit": "questões/pesquisa", "category": "Complexidade"},
        {"id": "KPI-10", "name": "Média de Respostas por Pergunta", "objective": "Mapear o volume de microdados coletados por questão.", "granularity": "Por Questão", "numerator": "Total de registros na tabela respostas", "denominator": "Total de questões cadastradas", "formula": "COUNT(respostas) / COUNT(questoes)", "value": round(float(media_respostas_pergunta), 2), "unit": "respostas/questão", "category": "Volume de Dados"},
        {"id": "KPI-11", "name": "Volume de Pesquisas no Último Período", "objective": "Medir quantas pesquisas foram registradas no último período temporal observado.", "granularity": "Por Período", "numerator": f"Pesquisas do período {latest_period}" if latest_period else "Pesquisas do último período disponível", "denominator": "N/A (Contagem absoluta)", "formula": "COUNT(pesquisas por período)", "value": float(latest_period_count), "unit": "pesquisas", "category": "Volume"},
        {"id": "KPI-12", "name": "Volume de Pesquisas Finalizadas no Último Período", "objective": "Medir quantas pesquisas atingiram status finalizado no último período observado.", "granularity": "Por Período", "numerator": f"Pesquisas finalizadas no período {latest_period}" if latest_period else "Pesquisas finalizadas no último período disponível", "denominator": "N/A (Contagem absoluta)", "formula": "COUNT(status = finalizada por período)", "value": float(latest_completed_count), "unit": "pesquisas", "category": "Eficiência"},
        {"id": "KPI-13", "name": "Volume de Pesquisas em Andamento", "objective": "Medir quantas pesquisas permanecem fora do status final.", "granularity": "Global (Sidusfarma)", "numerator": "Pesquisas sem status finalizado", "denominator": "N/A (Contagem absoluta)", "formula": "COUNT(status não final)", "value": float(len(df_pesquisas[~df_pesquisas["status"].astype(str).str.lower().isin(["concluída", "concluida", "finalizada"])]) if "status" in df_pesquisas.columns else 0), "unit": "pesquisas", "category": "Operação"},
        {"id": "KPI-14", "name": "Crescimento do Volume vs. Período Anterior", "objective": "Medir a variação percentual do volume de pesquisas entre os dois últimos períodos observados.", "granularity": "Por Período", "numerator": f"Volume em {latest_period}" if latest_period else "Volume do período atual", "denominator": f"Volume em {prev_period}" if prev_period else "Volume do período anterior", "formula": "((t - t-1) / t-1) * 100", "value": float(growth_pct), "unit": "percentual", "category": "Tendência"},
        {"id": "KPI-15", "name": "Taxa de Pesquisas Prorrogadas", "objective": "Medir o peso das prorrogações no portfólio de pesquisas.", "granularity": "Por Pesquisa", "numerator": "Pesquisas com prorrogada_ate preenchida", "denominator": "Total de pesquisas cadastradas", "formula": "COUNT(prorrogada_ate preenchida) / Total * 100", "value": float(_safe_pct(df_pesquisas["prorrogada_ate"].notna().sum() if "prorrogada_ate" in df_pesquisas.columns else 0, total_pesquisas)), "unit": "percentual", "category": "Prazo"},
        {"id": "KPI-16", "name": "Ciclo Mediano da Pesquisa", "objective": "Medir o valor central do ciclo total entre solicitação e divulgação.", "granularity": "Por Pesquisa", "numerator": "Mediana dos dias entre solicitação e divulgação", "denominator": "Pesquisas com ciclo preenchido", "formula": "MEDIAN(dias entre a solicitação e a divulgação)", "value": float(_safe_median(dias_ciclo)), "unit": "dias", "category": "Prazo"},
        {"id": "KPI-17", "name": "Média de Dias Úteis Aberta", "objective": "Medir quanto tempo a pesquisa permanece aberta para resposta.", "granularity": "Por Pesquisa", "numerator": "Soma dos dias úteis aberta", "denominator": "Pesquisas com campo preenchido", "formula": "MEAN(dias úteis aberta)", "value": float(_safe_mean(dias_aberta)), "unit": "dias", "category": "Prazo"},
        {"id": "KPI-18", "name": "Mediana de Dias Úteis Aberta", "objective": "Medir o valor central do tempo em que a pesquisa permanece aberta.", "granularity": "Por Pesquisa", "numerator": "Mediana dos dias úteis aberta", "denominator": "Pesquisas com campo preenchido", "formula": "MEDIAN(dias úteis aberta)", "value": float(_safe_median(dias_aberta)), "unit": "dias", "category": "Prazo"},
        {"id": "KPI-19", "name": "Média de Dias para Tabulação", "objective": "Medir o tempo médio consumido na etapa de tabulação.", "granularity": "Por Pesquisa", "numerator": "Soma dos dias para tabulação", "denominator": "Pesquisas com campo preenchido", "formula": "MEAN(dias para tabulação)", "value": float(_safe_mean(dias_tabulacao)), "unit": "dias", "category": "Prazo"},
        {"id": "KPI-20", "name": "Mediana de Dias para Tabulação", "objective": "Medir o valor central do tempo de tabulação.", "granularity": "Por Pesquisa", "numerator": "Mediana dos dias para tabulação", "denominator": "Pesquisas com campo preenchido", "formula": "MEDIAN(dias para tabulação)", "value": float(_safe_median(dias_tabulacao)), "unit": "dias", "category": "Prazo"},
        {"id": "KPI-21", "name": "Empresas Participantes Distintas", "objective": "Medir quantas empresas diferentes aparecem na base de participações.", "granularity": "Por Empresa", "numerator": "Empresas distintas presentes em respondentes", "denominator": "N/A (Contagem absoluta)", "formula": "COUNT(DISTINCT respondentes.id_empresa)", "value": float(empresas_participantes_unicas), "unit": "empresas", "category": "Engajamento"},
        {"id": "KPI-22", "name": "Empresas que Nunca Participaram", "objective": "Medir quantas empresas do cadastro ainda não aparecem em participações.", "granularity": "Por Empresa", "numerator": "Total de empresas sem participação", "denominator": "N/A (Contagem absoluta)", "formula": "Total empresas - empresas participantes", "value": float(empresas_nunca), "unit": "empresas", "category": "Engajamento"},
        {"id": "KPI-23", "name": "Participações Médias por Empresa Ativa", "objective": "Medir a recorrência média de participação entre empresas ativas.", "granularity": "Por Empresa Ativa", "numerator": "Total de participações", "denominator": "Empresas participantes distintas", "formula": "COUNT(participações) / empresas ativas", "value": round(float(total_participacoes / empresas_participantes_unicas), 2) if empresas_participantes_unicas else 0.0, "unit": "participações/empresa", "category": "Engajamento"},
        {"id": "KPI-24", "name": "Empresas Recorrentes", "objective": "Medir quantas empresas participaram de duas ou mais pesquisas.", "granularity": "Por Empresa", "numerator": "Empresas com duas ou mais participações", "denominator": "N/A (Contagem absoluta)", "formula": "COUNT(empresas com 2+ participações)", "value": float(empresas_recorrentes), "unit": "empresas", "category": "Engajamento"},
        {"id": "KPI-25", "name": "Taxa de Associadas entre Empresas Participantes", "objective": "Medir a proporção de associadas dentro da base que efetivamente participa.", "granularity": "Por Empresa Participante", "numerator": "Empresas participantes associadas", "denominator": "Empresas participantes distintas", "formula": "(Associadas participantes / participantes) * 100", "value": float(_safe_pct(associadas_participantes, empresas_participantes_unicas)), "unit": "percentual", "category": "Perfil"},
        {"id": "KPI-26", "name": "Cobertura Total de Mercado das Participantes", "objective": "Estimar quanto do mercado é coberto pelas empresas que efetivamente participam.", "granularity": "Global (Empresas Participantes)", "numerator": "Soma do % de mercado das empresas participantes", "denominator": "N/A (Soma acumulada)", "formula": "SUM(% mercado participantes)", "value": float(cobertura_total), "unit": "pontos percentuais", "category": "Mercado"},
        {"id": "KPI-27", "name": "Cobertura Média de Mercado por Pesquisa", "objective": "Medir a representatividade média do portfólio no nível de pesquisa.", "granularity": "Por Pesquisa", "numerator": "Cobertura de mercado por pesquisa", "denominator": "Total de pesquisas com cobertura estimável", "formula": "MEAN(cobertura por pesquisa)", "value": float(cobertura_media_por_pesquisa), "unit": "pontos percentuais", "category": "Mercado"},
        {"id": "KPI-28", "name": "Variação da Cobertura de Mercado vs. Período Anterior", "objective": "Medir a evolução da cobertura média de mercado entre os dois últimos períodos observados.", "granularity": "Por Período", "numerator": "Cobertura média do período atual", "denominator": "Cobertura média do período anterior", "formula": "((cobertura_t - cobertura_t-1) / cobertura_t-1) * 100", "value": float(cobertura_growth), "unit": "percentual", "category": "Mercado"},
        {"id": "KPI-29", "name": "Empresas Top-Share Participantes", "objective": "Medir quantas empresas de maior participação de mercado aparecem na base ativa.", "granularity": "Por Empresa", "numerator": "Empresas participantes no quartil superior de % de mercado", "denominator": "N/A (Contagem absoluta)", "formula": "COUNT(empresas participantes com % mercado >= P75)", "value": float(top_share_participantes), "unit": "empresas", "category": "Mercado"},
        {"id": "KPI-30", "name": "Concentração Departamental", "objective": "Medir o peso do departamento modal no cadastro de contatos.", "granularity": "Por Contato", "numerator": "Contatos no departamento modal", "denominator": "Total de contatos com departamento preenchido", "formula": "COUNT(departamento modal) / Total * 100", "value": float(_mode_rate(df_clientes["departamento"]) if "departamento" in df_clientes.columns else 0.0), "unit": "percentual", "category": "Perfil"},
        {"id": "KPI-31", "name": "Concentração por Cargo", "objective": "Medir o peso do cargo modal no cadastro de contatos.", "granularity": "Por Contato", "numerator": "Contatos no cargo modal", "denominator": "Total de contatos com cargo preenchido", "formula": "COUNT(cargo modal) / Total * 100", "value": float(_mode_rate(df_clientes["cargo"]) if "cargo" in df_clientes.columns else 0.0), "unit": "percentual", "category": "Perfil"},
        {"id": "KPI-32", "name": "Concentração por Nacionalidade", "objective": "Medir o peso da nacionalidade modal no cadastro institucional.", "granularity": "Por Empresa", "numerator": "Empresas na nacionalidade modal", "denominator": "Total de empresas com nacionalidade preenchida", "formula": "COUNT(nacionalidade modal) / Total * 100", "value": float(_mode_rate(df_empresas["Nacionalidade"]) if "Nacionalidade" in df_empresas.columns else 0.0), "unit": "percentual", "category": "Perfil"},
        {"id": "KPI-33", "name": "Cobertura Geográfica das Participantes", "objective": "Medir a amplitude territorial da base ativa de empresas.", "granularity": "Por Empresa Participante", "numerator": "Estados distintos entre empresas participantes", "denominator": "N/A (Contagem absoluta)", "formula": "COUNT(DISTINCT Estado)", "value": float(geo_states), "unit": "estados", "category": "Perfil"},
        {"id": "KPI-34", "name": "Total de Questões Cadastradas", "objective": "Medir o volume bruto de itens de questionário disponíveis na base.", "granularity": "Por Questão", "numerator": "Total de questões cadastradas", "denominator": "N/A (Contagem absoluta)", "formula": "COUNT(id_pergunta)", "value": float(total_questoes), "unit": "questões", "category": "Questionário"},
        {"id": "KPI-35", "name": "Taxa de Questões Fechadas", "objective": "Medir a proporção de questões fechadas na base de questionários.", "granularity": "Por Questão", "numerator": "Questões fechadas", "denominator": "Total de questões cadastradas", "formula": "COUNT(tipo fechado) / Total * 100", "value": float(_safe_pct(total_questoes_fechadas, total_questoes)), "unit": "percentual", "category": "Questionário"},
        {"id": "KPI-36", "name": "Taxa de Questões Abertas", "objective": "Medir a proporção de questões abertas na base de questionários.", "granularity": "Por Questão", "numerator": "Questões abertas", "denominator": "Total de questões cadastradas", "formula": "COUNT(tipo aberta) / Total * 100", "value": float(_safe_pct(total_questoes_abertas, total_questoes)), "unit": "percentual", "category": "Questionário"},
        {"id": "KPI-37", "name": "Taxa de Questões Matriciais", "objective": "Medir a proporção de questões matriciais no instrumento.", "granularity": "Por Questão", "numerator": "Questões matriciais", "denominator": "Total de questões cadastradas", "formula": "COUNT(tipo matriz) / Total * 100", "value": float(_safe_pct(total_questoes_matriz, total_questoes)), "unit": "percentual", "category": "Questionário"},
        {"id": "KPI-38", "name": "Média de Alternativas por Questão", "objective": "Medir a complexidade média das perguntas fechadas.", "granularity": "Por Questão", "numerator": "Soma das alternativas cadastradas", "denominator": "Questões com alternativas mensuráveis", "formula": "MEAN(qtd_alternativas)", "value": float(_safe_mean(qtd_alternativas)), "unit": "alternativas", "category": "Questionário"},
        {"id": "KPI-39", "name": "Taxa de Perguntas com Confiança Alta", "objective": "Medir a proporção de questões classificadas com alta confiança.", "granularity": "Por Questão", "numerator": "Questões com confiança alta", "denominator": "Total de questões cadastradas", "formula": "COUNT(confianca = alta) / Total * 100", "value": float(_safe_pct(confianca_alta, total_questoes)), "unit": "percentual", "category": "Governança"},
        {"id": "KPI-40", "name": "Total de Respostas Coletadas", "objective": "Medir o volume bruto de microdados de resposta já coletados.", "granularity": "Por Resposta", "numerator": "Total de respostas coletadas", "denominator": "N/A (Contagem absoluta)", "formula": "COUNT(id_resposta)", "value": float(total_respostas), "unit": "respostas", "category": "Volume de Dados"},
        {"id": "KPI-41", "name": "Taxa de Respostas por Pergunta Cadastrada", "objective": "Medir a densidade média de respostas na base de perguntas cadastradas.", "granularity": "Por Questão", "numerator": "Total de respostas coletadas", "denominator": "Total de questões cadastradas", "formula": "COUNT(respostas) / COUNT(questoes)", "value": round(float(media_respostas_pergunta), 2), "unit": "respostas/questão", "category": "Volume de Dados"},
    ]
