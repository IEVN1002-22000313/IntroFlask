from flask import Flask, render_template #importar flask,render_template

app=Flask(__name__)

#Creacion de rutas 

@app.route("/")
def index():
    titulo='hola!'
    lista=['luis','manuel','jesus']
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/hola")#@.r tabulador para salir automatico
def hola():#crea otra ruta en el navegador
    return "<h3>saludo desde Hola<h3/>"

@app.route("/user/<string:user>")#uso la diagonal mas un nombre
def user(user):
    return "Hola "+ user

@app.route("/numero/<int:n>")#coloca numero mas un numero
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")#colocas user/un numero entero/nombre
def username(id,username):
    return "ID: {} nombre: {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")# colocamos num1/num2 en decimal
def func(n1,n2):
    return "lasuma es: {}".format(n1+n2)


if __name__ =="__main__":
    app.run(debug=True)#sirve para que haga cambios en el navegador en automatico

