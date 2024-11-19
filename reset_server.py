import os

def reset_server():
    # Excluir arquivos de criptografia e resultado
    for arquivo in ['criptografia_votos.txt', 'relatorio_votacao.txt']:
        if os.path.exists(arquivo):
            os.remove(arquivo)
    print("Arquivos de criptografia e resultado excluídos. O servidor foi resetado.")

if __name__ == '__main__':
    reset_server()
