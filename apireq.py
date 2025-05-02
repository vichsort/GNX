from flask import Flask, request
import requests
import db
from config import apikey

db.generator() # chama o gerador do banco

url = f'https://www.omdbapi.com/?apikey={apikey}&'
app = Flask(__name__)

@app.route("/request/<caller>", methods=["POST"])
def sender(caller):
    # "CALLER" é responsável por chamar e
    # adquirir as informações passadas para
    # enviar com uma outra função estes
    # aspectos pro banco de dados. 
    # dentro dela pegamos o JSON e o tipo
    # de requisição (titulo ou id) que esta
    # sendo realizada. 

    dados_receba = request.get_json()
    informacao = dados_receba.get('info') # só o que importa

    if caller in ("title", "id"): 
        # se for um dos dois aceitos vai lançar pro bd
        return call(informacao, caller)
    return {'error': 'Caller inválido'}, 400

@app.route("/call", methods=["GET"])
def call(param=None, caller=None):
    # "CALL", realiza então a chamada/ponte
    # entre o banco de dados e o codigo em
    # flask. Pra nao dar erro por padrão (algo
    # que me estressou muito escrevendo essa
    # parte) define já como None.
 
    if not param or not caller:
        # só pra garantir...
        caller = request.args.get('type')
        param = request.args.get('info')

    key = 't' if caller == 'title' else 'i'          # operador ternario ridiculo (js >>>)
    full_url = f"{url}{key}={param}"                 # imagino que isso não seja seguro

    resp = requests.get(full_url)                    # realiza o GET na API
    if resp.status_code == 200:
        data = resp.json()
        if data.get('Response') == 'True':
            print("Requisição bem-sucedida:", data)  # printa no console
            db.catcher(data) # aqui a magica acontece
            return data, 200
        else:
            print(f"OMDb erro: {data.get('Error')}") # quando o erro é no omdb
            return {'error': data.get('Error')}, 502
    else:
        print(f"req erro: {resp.status_code}")       # quando o erro é meu
        return {'error': 'HTTP ' + str(resp.status_code)}, resp.status_code
