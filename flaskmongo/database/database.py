from pymongo import MongoClient
import json
import certifi

ca = certifi.where()

##################
# caragar el archivo de configuracion #
#######################################
def loadConfigFile():
    with open("database/config.json") as f:
        data = json.load(f)
    return data

    ######################################
    #      funcion de conexion           #
    ######################################
def dbConnection():
    dataconfig = loadConfigFile()
    try:
        #coneccion atlas
        client = MongoClient(dataConfig['MONGO_URI_SERVER'], tlsCAFile = ca)
        #coneccion local
        client = MongoClient(dataConfig['MONGO_URI_LOCAL'], dataConfig['LOCAL_PORT'])
        db = client["regiselecciones"]
    except ConnectionError:
        print("Error de conexion con la base de datos")
    return db
