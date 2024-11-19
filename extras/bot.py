import sys
import os
import threading
import time
import random

# Adicionar o diretório principal ao sys.path para garantir que os módulos possam ser importados corretamente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from criptografia_votos import criptografia, chave
from extras.autocompletar import times_populares

bot_ativo = False

def executar_bot():
    global bot_ativo
    while bot_ativo:
        time.sleep(1e-11)  # Ajuste o tempo de espera conforme necessário
        voto_aleatorio = random.choice(times_populares)
        votos_criptografados = criptografia(voto_aleatorio, chave)
        with open('criptografia_votos.txt', 'a', encoding='utf-8') as armazenamento_votos:
            armazenamento_votos.write(votos_criptografados + '\n')
        print(f"Voto simulado: {voto_aleatorio}")

def ativar_bot():
    global bot_ativo
    bot_ativo = True
    threading.Thread(target=executar_bot).start()

def desativar_bot():
    global bot_ativo
    bot_ativo = False

if __name__ == '__main__':
    ativar_bot()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        desativar_bot()
        print("Bot desativado.")