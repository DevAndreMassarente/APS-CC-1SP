import sys
import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_file

# Adicionar o diretório principal ao sys.path para garantir que os módulos possam ser importados corretamente
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from urna import votar as votar_urna
from desencriptografia_votos import desencriptografar_votos
from autocompletar import times_populares
from cores_times import cores_times

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

@app.route('/')
def index():
    try:
        votou = session.get('usuario_votou', False)
        mensagem = session.get('mensagem', '')
        caminho_relatorio = os.path.join(os.path.dirname(__file__), 'relatorio_votacao.txt')
        if os.path.exists(caminho_relatorio):
            votos_contados, total_votos, ranking = desencriptografar_votos()
            return render_template('resultados.html', votos_contados=votos_contados, total_votos=total_votos, ranking=ranking)
        return render_template('index.html', times=times_populares, votou=votou, mensagem=mensagem)
    except Exception as e:
        return f"Erro ao carregar a página inicial: {e}", 500

@app.route('/votar', methods=['POST'])
def votar_route():
    try:
        voto = request.form['voto']
        user_ip = get_user_ip()
        
        if not voto:
            mensagem = "Por favor, escolha um time antes de votar."
            return render_template('index.html', mensagem=mensagem, times=times_populares, votou=False)
        
        if session.get('usuario_votou', False):
            mensagem = "Você já votou! Seu voto já foi enviado. Obrigado por participar!"
            return render_template('index.html', mensagem=mensagem, times=times_populares, votou=True)
        
        mensagem = votar_urna(voto, user_ip)
        
        session['usuario_votou'] = True
        session['mensagem'] = f"Voto registrado: {mensagem}. Obrigado por participar!"
        
        return redirect(url_for('agradecimento'))
    except Exception as e:
        return f"Erro ao registrar o voto: {e}", 500

@app.route('/nao_tenho_time', methods=['POST'])
def nao_tenho_time_route():
    try:
        user_ip = get_user_ip()
        
        if session.get('usuario_votou', False):
            mensagem = "Você já votou! Seu voto já foi enviado. Obrigado por participar!"
            return render_template('index.html', mensagem=mensagem, times=times_populares, votou=True)
        
        mensagem = votar_urna("Sem time", user_ip)
        
        session['usuario_votou'] = True
        session['mensagem'] = "Voto registrado: Sem time. Obrigado por participar!"
        
        return redirect(url_for('agradecimento'))
    except Exception as e:
        return f"Erro ao registrar o voto: {e}", 500

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    try:
        query = request.args.get('query', '').lower()
        sugestoes = [time for time in times_populares if query in time.lower()]
        return jsonify(sugestoes[:5])
    except Exception as e:
        return jsonify({"erro": f"Erro ao obter sugestões: {e}"}), 500

@app.route('/get_cores_time', methods=['POST'])
def get_cores_time():
    try:
        data = request.get_json()
        time = data.get('time')
        cores = cores_times.get(time, ['transparent', 'transparent'])
        return jsonify({'cores': cores})
    except Exception as e:
        return jsonify({"erro": f"Erro ao obter cores do time: {e}"}), 500

@app.route('/agradecimento')
def agradecimento():
    try:
        mensagem = session.get('mensagem', 'Obrigado por votar! Agradecemos sua participação.')
        return render_template('agradecimento.html', mensagem=mensagem)
    except Exception as e:
        return f"Erro ao carregar a página de agradecimento: {e}", 500

@app.route('/ver_votos')
def ver_votos():
    try:
        caminho_arquivo = os.path.join(os.path.dirname(__file__), 'criptografia_votos.txt')
        if os.path.exists(caminho_arquivo):
            return send_file(caminho_arquivo, as_attachment=True)
        else:
            return "Arquivo de votos não encontrado.", 404
    except Exception as e:
        return f"Erro ao acessar o arquivo de votos: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)