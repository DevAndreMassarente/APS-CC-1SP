import sqlite3
from criptografia_votos import descriptografia, chave

def desencriptografar_votos():
    votos_contados = {}
    conn = sqlite3.connect('votos.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT voto FROM votos')
    votos_criptografados = cursor.fetchall()
    
    for voto_criptografado in votos_criptografados:
        voto = descriptografia(voto_criptografado[0], chave)
        if voto in votos_contados:
            votos_contados[voto] += 1
        else:
            votos_contados[voto] = 1
    
    total_votos = sum(votos_contados.values())
    ranking = sorted(votos_contados.items(), key=lambda item: item[1], reverse=True)
    
    conn.close()
    return votos_contados, total_votos, ranking

if __name__ == '__main__':
    votos_contados, total_votos, ranking = desencriptografar_votos()
    print("RELATÓRIO DE VOTAÇÃO - VOTAÇÃO DE CLUBES")
    print("APS - André - Alberto - Enzo")
    print("RANKING DE VOTOS\n")
    for i, (time, votos) in enumerate(ranking, 1):
        print(f"{i}º - {time}: {votos} votos")
    print(f"\nTOTAL DE VOTOS: {total_votos}")