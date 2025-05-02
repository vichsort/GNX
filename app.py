from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)

# Endereço onde o apireq está rodando
APIREQ_BASE = 'http://localhost:5000'


@app.route('/')
def home():
    # Exibe o formulário em branco
    return render_template('index.html')


@app.route('/home')
def red_home():
    return redirect(url_for('home'))


@app.route('/buscar', methods=['POST'])
def buscar():
    # Extrai dados do form
    caller = request.form.get('caller')   # 'title' ou 'id'
    info = request.form.get('info')       # o texto que o usuário digitou

    if not info:
        flash('Você precisa preencher o campo de busca.', 'warning')
        return redirect(url_for('home'))

    # Monta e dispara a requisição na APi
    url = f"{APIREQ_BASE}/request/{caller}"
    resp = requests.post(url, json={'info': info})

    if resp.ok:
        # Se tudo deu certo, traz o JSON de resposta
        # pra evitar erros maiores que podem dar
        # dentro da API
        resultado = resp.json()
        return render_template('index.html', result=resultado)
    else:
        # so pra esclarecer, eu esqueci de colocar um '?apikey='
        # uma hora e dai deu um erro de alerta que fez eu cagar
        # nas calças. Dai eu coloquei isso aqui que aprendi com
        # o gustavo guanabara (genio)
        flash(f"Erro na busca (HTTP {resp.status_code})", 'danger')
        return redirect(url_for('home'))

