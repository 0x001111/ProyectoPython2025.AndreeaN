#imports
from flask import Flask, render_template, request; 

# empezando a hacer codigo

app = Flask(__name__)
"""
@app.route('/') #decorador para definir la ruta raiz
def principal():
    return "Bienvenido a mi sitio web principal con python"
"""
@app.route('/')
def base():
    return render_template('base.html') #para acceder al base.html

@app.route('/index')
def index():
    return render_template('index.html') #para acceder al index.html

if __name__ == '__main__':
    app.run(debug=True) #esto hace que el servidor se reinicie automaticamente al estar haciendo cambios y así no tener que reiniciar el SV




