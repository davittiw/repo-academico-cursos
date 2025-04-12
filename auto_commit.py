import subprocess
from collections import defaultdict
import os

def main():
    # Adiciona todos os arquivos (modificados e novos)
    subprocess.run(["git", "add", "."])

    # Pega os arquivos que estão no staging
    resultado = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True)
    arquivos = resultado.stdout.strip().split('\n')

    if not arquivos or arquivos == ['']:
        print("❌ Nenhum arquivo no staging para commitar.")
        return

    # Agrupa arquivos por extensão
    por_extensao = defaultdict(list)

    for arquivo in arquivos:
        if '.' in arquivo:
            extensao = os.path.splitext(arquivo)[1].lower().strip('.')
        else:
            extensao = 'sem_extensao'

        por_extensao[extensao].append(arquivo)

    # Commit para cada grupo de extensão
    for ext, lista in por_extensao.items():
        subprocess.run(["git", "add"] + lista)
        mensagem = f"update {ext} files"
        subprocess.run(["git", "commit", "-m", mensagem])
        print(f"✅ Commit feito: {mensagem}")

    # Descobre o nome do branch atual
    branch_atual = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        capture_output=True, text=True
    ).stdout.strip()

    # Faz push com upstream se for necessário
    print(f"📤 Enviando commits para o branch remoto '{branch_atual}'...")
    subprocess.run(["git", "push", "--set-upstream", "origin", branch_atual])
    print("✅ Push concluído com sucesso!")

if __name__ == "__main__":
    main()
