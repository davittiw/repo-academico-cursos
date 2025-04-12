import subprocess
from collections import defaultdict
import os

def main():
    # Adiciona todos os arquivos modificados e novos
    subprocess.run(["git", "add", "."])

    # Agora pega tudo que está no staging
    resultado = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True)
    arquivos = resultado.stdout.strip().split('\n')

    if not arquivos or arquivos == ['']:
        print("❌ Nenhum arquivo no staging para commitar.")
        return

    # Agrupa por extensão
    por_extensao = defaultdict(list)

    for arquivo in arquivos:
        if '.' in arquivo:
            extensao = os.path.splitext(arquivo)[1].lower().strip('.')
        else:
            extensao = 'sem_extensao'

        por_extensao[extensao].append(arquivo)

    # Faz commit para cada tipo de arquivo
    for ext, lista in por_extensao.items():
        subprocess.run(["git", "add"] + lista)
        mensagem = f"update {ext} files"
        subprocess.run(["git", "commit", "-m", mensagem])
        print(f"✅ Commit feito: {mensagem}")

if __name__ == "__main__":
    main()
