from flask import Flask
import uuid

# Tem que implementar um negocio nessa api aqui: https://omdapi.com
# o usuário faz uma requisição que diz à nossa API que ela tem que requisitar nessa omd se tem o filme pedido lá
# caso não tiver, o sistema retorna 404 
# no banco de dados armazenamos as informações retornadas do JSON da API.

app = Flask(__name__)

@app.route('/', methods=["GET"])
def pegaItens():
    ID = uuid.uuid4()
    return {
        'ID': ID,
        'raça': 'negão'
    }
