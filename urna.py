import os
import base64
import requests
from criptografia_votos import criptografia, chave

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_OWNER = 'seu-usuario'
REPO_NAME = 'seu-repositorio'
FILE_PATH = 'criptografia_votos.txt'

def votar(voto, user_ip):
    votos_criptografados = criptografia(voto, chave)
    content = f"{votos_criptografados}\n"
    content_base64 = base64.b64encode(content.encode('utf-8')).decode('utf-8')

    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Obter o SHA do arquivo existente
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        sha = response.json()['sha']
    else:
        sha = None

    data = {
        'message': 'Adicionar voto',
        'content': content_base64,
        'branch': 'main'
    }
    if sha:
        data['sha'] = sha

    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 201 or response.status_code == 200:
        return f"Voto registrado: {voto}"
    else:
        print(f"Erro ao registrar voto no GitHub: {response.status_code} - {response.text}")
        return "Erro ao registrar voto no GitHub"

if __name__ == '__main__':
    while True:
        voto = input("Insira o nome do seu time ou digite 'sair' para encerrar: ").strip().lower()
        if voto == "sair":
            print("Encerrando o programa.")
            break
        else:
            user_ip = "127.0.0.1"
            print(votar(voto, user_ip))