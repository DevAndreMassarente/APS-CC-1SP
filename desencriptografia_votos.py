from criptografia_votos import chave

def desencriptografar_votos():
    votos_contados = {}

    def descriptografia(voto_criptografado, chave):
        cripto = bytes.fromhex(voto_criptografado)
        voto = ''.join(chr((char - chave) % 256) for char in cripto)
        return voto

    try:
        with open('criptografia_votos.txt', 'r', encoding='utf-8') as armazenamento_votos:
            votos_criptografados = armazenamento_votos.readlines()
    except FileNotFoundError:
        return votos_contados, 0, []

    for voto_criptografado in votos_criptografados:
        voto = descriptografia(voto_criptografado.strip(), chave)
        if voto in votos_contados:
            votos_contados[voto] += 1
        else:
            votos_contados[voto] = 1

    total_votos = sum(votos_contados.values())

    ranking = sorted(votos_contados.items(), key=lambda item: item[1], reverse=True)

    return votos_contados, total_votos, ranking

if __name__ == '__main__':
    votos_contados, total_votos, ranking = desencriptografar_votos()
    print("RELATÓRIO DE VOTAÇÃO - VOTAÇÃO DE CLUBES")
    print("APS - André - Alberto - Enzo")
    print("RANKING DE VOTOS\n")
    for i, (time, votos) in enumerate(ranking, 1):
        print(f"{i}º - {time}: {votos} votos")
    print(f"\nTOTAL DE VOTOS: {total_votos}")