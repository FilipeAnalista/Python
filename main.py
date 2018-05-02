from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

app= Flask(__name__)

@app.route('/')
def index():
    return render_templete("index.html")

@app.route('/cadastro', methods=['POST'])
def cadastro():
    cliente = MongoClient('localhost', 27017)

    banco = cliente.Pedidos

    usuarios = banco.Usuarios

    dados = request.get_json(silent=True, force=True)

    if usuario_id:
        resultado = {
            "Resultado": {
                "Status": True,
                "Mensagem": "dados cadastrados com sucesso."
            },
            "Object_id": usuario_id.inserted_id
        }

        return jsonify (resultado)
    else:
        resultado = {
            "Resultado":{
                "Status": False,
                "Mensagem": "dados cadastrados com sucesso."
            },
            "Object_id": None
        }
        return jsonify (resultado)
if __name__ == "__main__":
    app.run(debug = True)
