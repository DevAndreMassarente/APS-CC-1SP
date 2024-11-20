import sqlite3

DATABASE = 'votos.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    return db

def desencriptografar_votos():
    votos_contados = {}

    db = get_db()
    cursor = db.execute('SELECT voto FROM votos')
    votos = cursor.fetchall()
    db.close()

    for voto in votos:
        voto = voto[0]
        if voto in votos_contados:
            votos_contados[voto] += 1
        else:
            votos_contados[voto] = 1

    total_votos = sum(votos_contados.values())
    
    with open('relatorio_votacao.txt', 'w', encoding='utf-8') as relatorio:
        relatorio.write("RELATÓRIO DE VOTAÇÃO - VOTAÇÃO DE CLUBES\n")
        relatorio.write("APS - André - Alberto - Enzo\n")
        relatorio.write("RANKING DE VOTOS\n\n")
        
        ranking = sorted(votos_contados.items(), key=lambda item: item[1], reverse=True)
        for i, (time, votos) in enumerate(ranking, 1):
            relatorio.write(f"{i}º - {time}: {votos} votos\n")
        
        relatorio.write("\nTOTAL DE VOTOS: {}\n".format(total_votos))

    return votos_contados, total_votos, ranking

if __name__ == '__main__':
    votos_contados, total_votos, ranking = desencriptografar_votos()
    print("RELATÓRIO DE VOTAÇÃO - VOTAÇÃO DE CLUBES")
    print("APS - André - Alberto - Enzo")
    print("RANKING DE VOTOS\n")
    for i, (time, votos) in enumerate(ranking, 1):
        print(f"{i}º - {time}: {votos} votos")
    print(f"\nTOTAL DE VOTOS: {total_votos}")