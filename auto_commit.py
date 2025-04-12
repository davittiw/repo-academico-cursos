import subprocess

# Pega os arquivos que foram adicionados ao staging com git add
resultado = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True)
arquivos = resultado.stdout.strip().split('\n')

# Evita erro se não houver arquivos
if not arquivos or arquivos == ['']:
    print("❌ Nenhum arquivo no staging para commitar.")
    exit()

# Agrupa os arquivos por extensão
extensoes = {
    "js": [],
    "css": [],
    "html": [],
    "py": [],
    "outros": []
}

for arquivo in arquivos:
    if arquivo.endswith(".js"):
        extensoes["js"].append(arquivo)
    elif arquivo.endswith(".css"):
        extensoes["css"].append(arquivo)
    elif arquivo.endswith(".html"):
        extensoes["html"].append(arquivo)
    elif arquivo.endswith(".py"):
        extensoes["py"].append(arquivo)
    else:
        extensoes["outros"].append(arquivo)

# Realiza os commits para cada tipo
for tipo, lista_arquivos in extensoes.items():
    if lista_arquivos:
        # Adiciona os arquivos (por segurança, caso tenha sido desfeito)
        subprocess.run(["git", "add"] + lista_arquivos)
        # Cria a mensagem de commit
        mensagem = f"update {tipo} files"
        subprocess.run(["git", "commit", "-m", mensagem])
        print(f"✅ Commit feito: {mensagem}")
