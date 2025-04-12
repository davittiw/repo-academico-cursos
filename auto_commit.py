import subprocess
from collections import defaultdict
import os

# Define os arquivos que devem ser ignorados
ARQUIVOS_IGNORADOS = ["auto_commit.py"]


def obter_mensagem_commit(arquivo):
    # Ignora o arquivo auto_commit.py ou qualquer outro especificado
    if arquivo in ARQUIVOS_IGNORADOS:
        return None

    # Pega a diferença entre o arquivo no staging e o último commit
    resultado_diff = subprocess.run(
        ["git", "diff", "--cached", arquivo], capture_output=True, text=True, encoding='utf-8'
    )

    # Verifica se a saída não está vazia e se existe conteúdo
    if not resultado_diff.stdout or not resultado_diff.stdout.strip():
        return None

    # Se houver diferença, gera uma mensagem básica com base no tipo de modificação
    if resultado_diff.stdout.startswith("+"):
        return f"Adicionou conteúdo no arquivo {arquivo}"
    elif resultado_diff.stdout.startswith("-"):
        return f"Remoção no arquivo {arquivo}"
    else:
        return f"Alteração no arquivo {arquivo}"


def main():
    # Adiciona todos os arquivos (modificados e novos)
    subprocess.run(["git", "add", "."])

    # Pega os arquivos que estão no staging
    resultado = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True,
                               encoding='utf-8')
    arquivos = resultado.stdout.strip().split('\n')

    if not arquivos or arquivos == ['']:
        print("❌ Nenhum arquivo no staging para commitar.")
        return

    # Agrupa arquivos por extensão
    por_extensao = defaultdict(list)

    for arquivo in arquivos:
        # Ignora o arquivo auto_commit.py
        if arquivo in ARQUIVOS_IGNORADOS:
            continue

        if '.' in arquivo:
            extensao = os.path.splitext(arquivo)[1].lower().strip('.')
        else:
            extensao = 'sem_extensao'

        por_extensao[extensao].append(arquivo)

    # Commit para cada grupo de extensão, mas com mensagem personalizada
    for ext, lista in por_extensao.items():
        # Para cada arquivo, cria a mensagem de commit
        for arquivo in lista:
            mensagem = obter_mensagem_commit(arquivo)
            if mensagem:
                subprocess.run(["git", "commit", "-m", mensagem])
                print(f"✅ Commit feito: {mensagem}")
            else:
                print(f"❌ Nenhuma modificação detectada no arquivo {arquivo}")

    # Descobre o nome do branch atual
    branch_atual = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        capture_output=True, text=True, encoding='utf-8'
    ).stdout.strip()

    # Faz push com upstream se for necessário
    print(f"📤 Enviando commits para o branch remoto '{branch_atual}'...")
    subprocess.run(["git", "push", "--set-upstream", "origin", branch_atual])
    print("✅ Push concluído com sucesso!")


if __name__ == "__main__":
    main()
