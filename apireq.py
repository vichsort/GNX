from flask import Flask, request
import uuid

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

    if (caller == "name"):
        chamarName(informacao)
    elif (caller == "id"):
        chamarId(informacao)
    else:
        print("invalid type")

    return caller

@app.route("/caller/name", methods=["GET"])
def chamarName(param):
    print(param + "insane")

@app.route("/caller/id", methods=["GET"])
def chamarId(param):
    print(param + " smth")




# Search by title

# https://www.omdbapi.com/?apikey=8193de3c&t=the batman


# Search by ID

# https://www.omdbapi.com/?apikey=8193de3c&i=tt1877830


# Search by search parameter

# https://www.omdbapi.com/?apikey=8193de3c&s=jaws&type=movie
