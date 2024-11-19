import sqlite3
from criptografia_votos import criptografia, chave

def votar(voto, user_ip):
    votos_criptografados = criptografia(voto, chave)
    
    conn = sqlite3.connect('votos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO votos (voto, user_ip) VALUES (?, ?)', (votos_criptografados, user_ip))
    conn.commit()
    conn.close()
    
    return f"Voto registrado: {voto}"

if __name__ == '__main__':
    while True:
        voto = input("Insira o nome do seu time ou digite 'sair' para encerrar: ").strip().lower()
        if voto == "sair":
            print("Encerrando o programa.")
            break
        else:
            user_ip = "127.0.0.1" 
            print(votar(voto, user_ip))