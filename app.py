import sys
import os
import unicodedata
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from urna import votar
from desencriptografia_votos import desencriptografar_votos
from autocompletar import times_populares
from cores_times import cores_times

# Adicionar o diretório principal ao sys.path para garantir que os módulos possam ser importados corretamente
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Configurar os caminhos para templates e arquivos estáticos
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = os.urandom(24)

def get_user_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    else:
        return request.environ['HTTP_X_FORWARDED_FOR']

def normalizar_nome(nome):
    return unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII').replace(' ', '').lower()

@app.route('/')
def index():
    votou = session.get('usuario_votou', False)
    mensagem = session.get('mensagem', '')
    votos_contados, total_votos, ranking = desencriptografar_votos()
    return render_template('index.html', times=times_populares, votou=votou, mensagem=mensagem, total_votos=total_votos, ranking=ranking)

@app.route('/votar', methods=['POST'])
def votar_route():
    voto = request.form['voto']
    user_ip = get_user_ip()

    if not voto:
        mensagem = "Por favor, escolha um time antes de votar."
        return render_template('index.html', mensagem=mensagem, times=times_populares, votou=False)

    if session.get('usuario_votou', False):
        mensagem = "Você já votou! Seu voto já foi enviado. Obrigado por participar!"
        return render_template('index.html', mensagem=mensagem, times=times_populares, votou=True)

    mensagem = votar(normalizar_nome(voto), user_ip)

    session['usuario_votou'] = True
    session['mensagem'] = f"Voto registrado: {mensagem}. Obrigado por participar!"

    return redirect(url_for('agradecimento'))

@app.route('/nao_tenho_time', methods=['POST'])
def nao_tenho_time_route():
    user_ip = get_user_ip()

    if session.get('usuario_votou', False):
        mensagem = "Você já votou! Seu voto já foi enviado. Obrigado por participar!"
        return render_template('index.html', mensagem=mensagem, times=times_populares, votou=True)

    mensagem = votar("Sem time", user_ip)

    session['usuario_votou'] = True
    session['mensagem'] = "Voto registrado: Sem time. Obrigado por participar!"

    return redirect(url_for('agradecimento'))

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('query', '').lower()
    sugestoes = [time for time in times_populares if query in time.lower()]
    return jsonify(sugestoes[:5])

@app.route('/get_cores_time', methods=['POST'])
def get_cores_time():
    data = request.get_json()
    time = data.get('time')
    cores = cores_times.get(normalizar_nome(time), ['transparent', 'transparent'])
    return jsonify({'cores': cores})

@app.route('/agradecimento')
def agradecimento():
    mensagem = session.get('mensagem', 'Obrigado por votar! Agradecemos sua participação.')
    return render_template('agradecimento.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)