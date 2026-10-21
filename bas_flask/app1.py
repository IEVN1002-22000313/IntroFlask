from flask import Flask, render_template,request #importar flask,render_template request regresa valores


app=Flask(__name__)

#Creacion de rutas 

@app.route("/")
def index():
    titulo='hola!'
    lista=['luis','manuel','jesus']
    return render_template("index.html",titulo=titulo,lista=lista)

"""@app.route("/distancia")#ruta de distancia
def distancia():
    return render_template("distancia.html")
"""

#Crear ruta para distancia entre dos puntos 
@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    x1 = ""
    y1 = ""
    x2 = ""
    y2 = ""
    res = ""
    if request.method == "POST":
        x1 = float(request.form.get("x1"))#transformamos de una vez los numeros a flotantes
        y1 = float(request.form.get("y1"))
        x2 = float(request.form.get("x2"))
        y2 = float(request.form.get("y2"))
        # distancia entre dos puntos d = raiz((x2 - x1)^2 + (y2 - y1)^2)
        res = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

    return render_template("distancia.html", x1=x1, y1=y1, x2=x2, y2=y2, res=res)


#ruta para operas basicas 
@app.route("/operasbas",methods=["GET","POST"])#ruta de operabas
def operasbas():
    n1=0
    n2=0
    res=0
    operacion=""
    if request.method=="POST":
        n1=request.form.get("n1")
        n2=request.form.get("n2")
        if request.form.get("operacion")=="suma":
            res = float(n1) + float(n2)



    return render_template("operasbas.html", n1=n1,n2=n2,res=res)

#----CINEPOLIS-----

@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():
    nombre = ""
    cantidadCompradores = ""
    cantidadBoletos = ""
    tarjetaCineco = "No"
    totalPagar = 0
    error = ""

    if request.method == "POST":
        nombre = request.form.get("nombre")
        cantidadCompradores = int(request.form.get("cantidadCompradores") or 0)
        cantidadBoletos = int(request.form.get("cantidadBoletos") or 0)
        tarjetaCineco = request.form.get("tarjetaCineco")

        # Regla: Máximo 7 boletas por comprador
        maximoPermitido = cantidadCompradores * 7

        if cantidadBoletos > maximoPermitido:
            error = f"No se pueden comprar más de {maximoPermitido} boletas para {cantidadCompradores} persona(s) (máximo 7 por comprador)."
        else:
            # Precio base por boleta
            precioBoleta = 12000
            subtotal = cantidadBoletos * precioBoleta

            # 1. Descuento por cantidad de boletas
            descuentoCantidad = 0
            if cantidadBoletos > 5:
                descuentoCantidad = 0.15  # 15% de descuento
            elif cantidadBoletos in [3, 4, 5]:
                descuentoCantidad = 0.10  # 10% de descuento
            else:
                descuentoCantidad = 0     # 0% para 1 o 2 boletas

            totalConDescuento = subtotal - (subtotal * descuentoCantidad)

            # 2. Descuento adicional por Tarjeta Cineco (10% adicional)
            if tarjetaCineco == "Si":
                totalPagar = totalConDescuento - (totalConDescuento * 0.10)
            else:
                totalPagar = totalConDescuento

    return render_template(
        "cinepolis.html",
        nombre=nombre,
        cantidadCompradores=cantidadCompradores,
        cantidadBoletos=cantidadBoletos,
        tarjetaCineco=tarjetaCineco,
        totalPagar=totalPagar,
        error=error
    )

#---TERMINA CINEPOLIS---

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

