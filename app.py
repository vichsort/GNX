from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from config import secret_key

app = Flask(__name__)
app.secret_key = secret_key

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
    caller = request.form.get('caller')   # 'title' ou 'id'
    info = request.form.get('info')       # o texto que o usuário digitou

    if not info:
        flash('Você precisa preencher o campo de busca.', 'warning')
        return redirect(url_for('home'))

    url = f"{APIREQ_BASE}/request/{caller}" # seta a url pra mandar a requisição
    resp = requests.post(url, json={'info': info}) # passa os dados em formato json, simulando um usuário por client

    if resp.ok:
        resultado = resp.json()
        return render_template('index.html', result=resultado)
    else: # alertas periódicos
        if resp.status_code == 502:
            flash('Filme não encontrado no banco de dados IMDb.', 'warning')
        else:
            flash(f"Erro na busca (HTTP {resp.status_code})", 'danger')
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=False, port=5001)
