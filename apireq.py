from flask import Flask, request
import requests
import uuid
import psyco
from config import apikey

url = f'http://www.omdbapi.com/?apikey={apikey}'
listreq = []

app = Flask(__name__)

@app.route("/request/<caller>", methods=["POST"])
def sender(caller):
    dados_receba = request.get_json()
    informacao = dados_receba['info']

    listreq.append({
        'ticket': str(uuid.uuid4()),
        'type': caller,
        'title': informacao
    })

    if (caller == "title" or caller == "id"):
        call(informacao, caller)

    return caller

@app.route("/call", methods=["GET"])
def call(param, caller):
    print(param + " recebido com sucesso, tipo: " + caller)
    if (caller == "title"):
        caller = "t="
    else:
        caller = "i="
    var_resposta = requests.get(url + caller + param)
    if (var_resposta.status_code == 200):
        print("tudo certo com a requisição.")
        print(var_resposta.text)
        psyco.catcher(var_resposta);
    else:
        print('erro! ' + var_resposta.status_code)



# Search by title

# https://www.omdbapi.com/?apikey=8193de3c&t=the batman


# Search by ID

# https://www.omdbapi.com/?apikey=8193de3c&i=tt1877830


# Search by search parameter

# https://www.omdbapi.com/?apikey=8193de3c&s=jaws&type=movie
