import pyrebase

FIREBASE_KEY = ""

firebaseConfig = {
    "apiKey": FIREBASE_KEY,
    "authDomain": "proyecto-de-grado-7e7d3.firebaseapp.com",
    "databaseURL": "https://proyecto-de-grado-7e7d3-default-rtdb.firebaseio.com",
    "projectId": "proyecto-de-grado-7e7d3",
    "storageBucket": "proyecto-de-grado-7e7d3.appspot.com",
    "messagingSenderId": "588928611789",
    "appId": "1:588928611789:web:2fbb4ffb4bf5b5af6f8084"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

#Retorna una lista de diccionarios que representan cada sesion de juego.
#Las llaves de este diccionario son fecha, con valor de la fecha en que se ejecuto el juego
#y statsf1 cuyo valor es una lista de diccionarios que representan sesiones de juego en la fase 1
def armar_diccionario_sesiones():
    sesiones_list = list()
    sesiones = db.child("sesiones").get()
    for sesion in sesiones.each():
        sesion_dict = dict()
        sesion_dict["fecha"] = sesion.val()["fecha"]
        try:
            if(sesion.val()["statsF1"] != None):
                statsf1 = sesion.val()["statsF1"]
                sesiones_f1 = list()
                for llave_sesion_f1 in statsf1.keys():
                    info_sesion_f1 = statsf1[llave_sesion_f1]
                    sesiones_f1.append(info_sesion_f1)
                sesion_dict["statsf1"] = sesiones_f1
        except:
            sesion_dict["statsf1"] = []
        sesiones_list.append(sesion_dict)
    return sesiones_list

armar_diccionario_sesiones()