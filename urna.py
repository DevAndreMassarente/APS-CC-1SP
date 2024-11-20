import sqlite3

DATABASE = 'votos.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    return db

usuario_votou = {}

def votar(voto, user_ip):
    global usuario_votou
    if user_ip in usuario_votou:
        return "Você já votou!"

    db = get_db()
    db.execute('INSERT INTO votos (voto, user_ip) VALUES (?, ?)', (voto, user_ip))
    db.commit()
    db.close()

    usuario_votou[user_ip] = True
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