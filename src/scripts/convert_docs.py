import os
import sys
from pathlib import Path
from markitdown import MarkItDown

SUPPORTED_EXTENSIONS = {'.pdf', '.pptx', '.docx', '.xlsx', '.png', '.jpg', '.jpeg'}

def convert_file(file_path: Path, md_engine: MarkItDown, overwrite: bool = False) -> bool:
    """Converte um arquivo bruto em .md no mesmo diretório."""
    output_path = file_path.with_suffix('.md')
    
    if output_path.exists() and not overwrite:
        print(f"[PULADO] Arquivo .md já existe: {output_path.name}")
        return False
        
    print(f"[CONVERTENDO] {file_path.relative_to(Path.cwd())} -> {output_path.name}...")
    try:
        result = md_engine.convert(str(file_path))
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result.text_content)
        print(f"[SUCESSO] Gerado: {output_path.relative_to(Path.cwd())}")
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao converter {file_path.name}: {e}", file=sys.stderr)
        return False

def scan_and_convert(target_dirs: list[str], overwrite: bool = False):
    """Varre os diretórios informados e converte todos os arquivos suportados."""
    md_engine = MarkItDown()
    root_dir = Path.cwd()
    
    converted_count = 0
    for target in target_dirs:
        dir_path = root_dir / target
        if not dir_path.exists():
            print(f"[AVISO] Diretório {target} não encontrado.")
            continue
            
        print(f"\n--- Escaneando diretório: {target} ---")
        for root, _, files in os.walk(dir_path):
            for file in files:
                file_path = Path(root) / file
                if file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
                    if convert_file(file_path, md_engine, overwrite=overwrite):
                        converted_count += 1

    print(f"\nConversão concluída! Total de arquivos processados: {converted_count}")

if __name__ == "__main__":
    # Diretórios padrão do repositório contendo arquivos brutos
    dirs_to_process = ["AULAS", "CONTEXTO_PROJETO"]
    
    force_overwrite = "--force" in sys.argv
    scan_and_convert(dirs_to_process, overwrite=force_overwrite)
