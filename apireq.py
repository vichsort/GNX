from flask import Flask, request
import requests
import uuid
import db
from config import apikey

db.generator()

url = f'https://www.omdbapi.com/{apikey}&'
app = Flask(__name__)
listreq = []

@app.route("/request/<caller>", methods=["POST"])
def sender(caller):
    dados_receba = request.get_json()
    informacao = dados_receba.get('info')

    listreq.append({
        'ticket': str(uuid.uuid4()),
        'type': caller,
        'title': informacao
    })

    if caller in ("title", "id"):
        return call(informacao, caller)
    return {'error': 'Caller inválido'}, 400

@app.route("/call", methods=["GET"])
def call(param=None, caller=None):
    if not param or not caller:
        caller = request.args.get('type')
        param = request.args.get('info')

    key = 't' if caller == 'title' else 'i'
    full_url = f"{url}{key}={param}"
    print(f"Chamando OMDb: {full_url}")

    resp = requests.get(full_url)
    if resp.status_code == 200:
        data = resp.json()
        if data.get('Response') == 'True':
            print("Requisição bem-sucedida:", data)
            db.catcher(data)
            return data, 200
        else:
            print(f"OMDb erro: {data.get('Error')}")
            return {'error': data.get('Error')}, 502
    else:
        print(f"HTTP error {resp.status_code}")
        return {'error': 'HTTP ' + str(resp.status_code)}, resp.status_code

if __name__ == '__main__':
    app.run(debug=True)
