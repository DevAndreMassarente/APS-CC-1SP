senha = 'AndAlbEnzAps123'

def hash(senha):
    hash_value = 0
    for char in senha:
        hash_value = (hash_value * 31 + ord(char)) % (2**32)
    return hash_value

chave = hash(senha)

def criptografia(voto, chave):
    cripto = [(ord(char) + chave) % 256 for char in voto]
    return ''.join(format(char, '02x') for char in cripto)

