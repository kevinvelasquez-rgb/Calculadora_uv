from flask import Flask, request
import random


app = Flask(__name__)

@app.route("/")
def home():
    return '''
<h1> Aplicación Calculadora </h1>

<p> Opciones disponibles: </p>
<ul>

    <li><a href="/suma?a=8&b=12"> Suma </a> </li>
    <li><a href="/resta?num1=10&num2=5"> Resta </a> </li>
    <li><a href="/multiplicacion?val1=4&val2=6"> Multiplicación </a> </li>
    <li><a href="/division?dividendo=20&divisor=4"> División </a> </li>

</ul>

'''
@app.route("/suma")
def ruta_suma():
    a=request.args.get("a", type=float)
    b=request.args.get("b", type=float)
    resultado = a + b
    return f"""
    La suma de los numeros {a} y {b} es: {resultado} 
    <a href="/">Volver al inicio</a>
    """

@app.route("/resta")
def ruta_resta():
    num1=request.args.get("num1", type=float)
    num2=request.args.get("num2", type=float)
    resultado = num1 - num2
    return f"""
    La resta de los numeros {num1} y {num2} es: {resultado} 
    <a href="/">Volver al inicio</a>
    """

@app.route("/multiplicacion")
def ruta_multiplicacion():
    val1=request.args.get("val1", type=float)
    val2=request.args.get("val2", type=float)
    resultado = val1 * val2
    return f"""
    La multiplicación de los numeros {val1} y {val2} es: {resultado} 
    <a href="/">Volver al inicio</a>
    """

@app.route("/division")
def ruta_division():    
    dividendo=request.args.get("dividendo", type=float)
    divisor=request.args.get("divisor", type=float)
    if divisor == 0:
        return """Error: No se puede dividir por cero. <br><br><a href="/">Volver al inicio</a>"""
    resultado = dividendo / divisor
    return f"""
    La división de los numeros {dividendo} y {divisor} es: {resultado} 
    <a href="/">Volver al inicio</a>
    """

#Esto permite actualizar rápidamente los cambios
if __name__ == "__main__":
    app.run(debug=True)