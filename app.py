import sys
import os
import sqlite3
from flask import Flask, render_template, request, jsonify, session, redirect, url_for

# Adicionar o diretório principal ao sys.path para garantir que os módulos possam ser importados corretamente
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from urna import votar as votar_urna
from desencriptografia_votos import desencriptografar_votos, descriptografia
from autocompletar import times_populares
from cores_times import cores_times

# Configurar os caminhos para templates e arquivos estáticos
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = os.urandom(24)

# Configurar o banco de dados SQLite
DATABASE = 'votos.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS votos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                voto TEXT NOT NULL,
                user_ip TEXT NOT NULL
            )
        ''')
        db.commit()

@app.before_first_request
def initialize():
    init_db()

def get_user_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        return request.environ['REMOTE_ADDR']
    else:
        return request.environ['HTTP_X_FORWARDED_FOR']

@app.route('/')
def index():
    votou = session.get('usuario_votou', False)
    mensagem = session.get('mensagem', '')
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT voto, COUNT(*) FROM votos GROUP BY voto')
    votos_contados = cursor.fetchall()
    total_votos = sum([voto[1] for voto in votos_contados])
    ranking = sorted(votos_contados, key=lambda x: x[1], reverse=True)
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
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO votos (voto, user_ip) VALUES (?, ?)', (voto, user_ip))
    db.commit()
    
    session['usuario_votou'] = True
    session['mensagem'] = f"Voto registrado: {voto}. Obrigado por participar!"
    
    return redirect(url_for('agradecimento'))

@app.route('/nao_tenho_time', methods=['POST'])
def nao_tenho_time_route():
    user_ip = get_user_ip()
    
    if session.get('usuario_votou', False):
        mensagem = "Você já votou! Seu voto já foi enviado. Obrigado por participar!"
        return render_template('index.html', mensagem=mensagem, times=times_populares, votou=True)
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO votos (voto, user_ip) VALUES (?, ?)', ("Sem time", user_ip))
    db.commit()
    
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
    cores = cores_times.get(time, ['transparent', 'transparent'])
    return jsonify({'cores': cores})

@app.route('/agradecimento')
def agradecimento():
    mensagem = session.get('mensagem', 'Obrigado por votar! Agradecemos sua participação.')
    return render_template('agradecimento.html', mensagem=mensagem)

@app.route('/ver_votos')
def ver_votos():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT voto FROM votos')
    votos_criptografados = cursor.fetchall()
    votos_desencriptados = [descriptografia(voto[0]) for voto in votos_criptografados]
    return render_template('ver_votos.html', votos=votos_desencriptados)

if __name__ == '__main__':
    app.run(debug=True)