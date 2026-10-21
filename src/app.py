from flask import Flask, jsonify, request #convierte  estructuras de datos a JSON/ request (peticioness attp es 
#un objeto almacena informacion del cliente

from flask_mysqldb import MySQL
from flask_cors import CORS

from config import config #importa las configuraciones de contraseñas 

app = Flask(__name__)

CORS(app)#libreria de comunicacion cliente-servidor

con = MySQL(app)#conexion 

#--------

@app.route("/alumnos",methods=['GET'])
def lista_alumnos():
    try:
        cursor=con.connection.cursor()
        sql="select * from alumnos"
        cursor.execute(sql)
        datos=cursor.fetchall()
        alumnos=[]
        for fila in datos:
            alumno={"matricula":fila[0],"nombre":fila[1],
                    "apaterno":fila[2],"amaterno":fila[3],
                    "correo":fila[4]}
            alumnos.append(alumno)
        return  jsonify({'alumnos':alumnos,'mensaje':'Lista de alumnos',
                         'exito':True})
 
    except Exception as ex:
        return jsonify({"message": "error {}".format(ex),'exito':False})

#------------

def pagina_no_encontrada(error):#funcion hecha por flask para enconttrar errores de url desconocida
    return "<h1>Pagina no encontrada</h1>", 404

if __name__ == "__main__":
    app.config.from_object(config['development'])#Carga las configuraciones del entorno de desarrollo
    #desde el objeto config que importamos del archivo config.py y verifica que haya una conexion
    app.register_error_handler(404, pagina_no_encontrada)#Registra oficialmente la función que creamos arriba. Le indica a la aplicación de Flask que,
    #cada vez que un usuario intente entrar a una URL que no existe
    app.run(host='0.0.0.0', port=5000)#servidor escucha peticiones y usa puerto 5000 ip de la maquina y local host