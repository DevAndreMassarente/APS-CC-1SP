from criptografia_votos import hash, chave

def descriptografia(voto_criptografado, chave=chave):
    voto = [chr((int(voto_criptografado[i:i+2], 16) - chave) % 256) for i in range(0, len(voto_criptografado), 2)]
    return ''.join(voto)

def desencriptografar_votos():
    votos_contados = {}

    try:
        with open('criptografia_votos.txt', 'r', encoding='utf-8') as armazenamento_votos:
            votos_criptografados = armazenamento_votos.readlines()
    except FileNotFoundError:
        return votos_contados, 0, []

    for voto_criptografado in votos_criptografados:
        voto = descriptografia(voto_criptografado.strip())
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