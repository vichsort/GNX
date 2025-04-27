from flask import Flask
import uuid

app = Flask(__name__)

@app.route('/', methods=["GET"])
def pegaItens():
    ID = uuid.uuid4()
    return {
        'ID': ID,
        'raça': 'negão'
    }
