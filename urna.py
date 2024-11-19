from criptografia_votos import criptografia, chave
from extras.bot import ativar_bot, desativar_bot

usuario_votou = {}

def votar(voto, user_ip):
    global usuario_votou
    if user_ip in usuario_votou:
        return "Você já votou!"
    
    votos_criptografados = criptografia(voto, chave)
    
    with open('criptografia_votos.txt', 'a', encoding='utf-8') as armazenamento_votos:
        armazenamento_votos.write(votos_criptografados + '\n')
    
    usuario_votou[user_ip] = True
    return f"Voto registrado: {voto}"

if __name__ == '__main__':
    while True:
        voto = input("Insira o nome do seu time ou digite um comando (ativarbot, desativarbot, sair): ").strip().lower()
        if voto == "ativarbot":
            ativar_bot()
            print("Bot ativado.")
        elif voto == "desativarbot":
            desativar_bot()
            print("Bot desativado.")
        elif voto == "sair":
            print("Encerrando o programa.")
            break
        else:
            user_ip = "127.0.0.1" 
            print(votar(voto, user_ip))