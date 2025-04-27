from flask import Flask
import apireq
import app
import psyco

app = Flask(__name__)

@app.route('/', methods=["GET"])
def chamar():
    print('chamando...')
    apireq.caller()
    print('chamado!')
    return True