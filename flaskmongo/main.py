from crypt import methods

from flask import Flask, Response, jsonify, request
from flask_cors import CORS

from Controladores.PartidoControlador import PartidoControlador

app = Flask(__name__)
cors = CORS(app)


##############################
##     VARIABLES GLOBALES   ##
##############################
#miControladorPartido = PartidoControlador()
#miControladorCandidato = CandidatoControlador()
#miControladorMesa = MesaControlador()
#miControladorResultado = ResultadoControlador()


####################################
##    PROBAR EL SERVICIO          ##
####################################
@app.route("/", methods=["GET"])
def test():
    json = {}
    json["Hasta aqui Bien "] = "El servidor se esta ejecutando ..."
    return jsonify(json)

#####################################
##      ENDPOINT PARTIDOS          ##
#####################################
@app.route("/partidos", methods=["GET"])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos", methods=["POST"])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=["GET"])
def getPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=["PUT"])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=["DELETE"])
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

 
if __name__ == "__main__":
    app.run(debug=False, port=9000)