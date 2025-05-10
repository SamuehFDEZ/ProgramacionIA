from flask import Flask, render_template, request, abort, redirect

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("index.html", nombre="Samuel")

def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        return f'Hola, {nombre}'
    return ''' 
    <form method="post"> 
    Nombre: <input type="text" name="nombre"> 
    <input type="submit" value="Enviar"> 
    </form> 
    '''

@app.route('/usuario', methods=['GET', 'POST', 'PUT', 'DELETE'])
def usuario():
    if request.method == 'GET':
        return "Obteniendo usuario"
    elif request.method == 'POST':
        return "Creando usuario"
    elif request.method == 'PUT':
        return "Actualizando usuario"
    elif request.method == 'DELETE':
        return "Eliminando usuario"


@app.route('/saludo/<nombre>')
def saludo_personalizado(nombre):
    return f'Hola, {nombre}'

@app.route("/articulos/<int:id>")
def mostrar_ariculo(id):
    return f'Articulo con ID: {id}'

@app.route('/buscar')
def buscar():
    query = request.args.get('q', '')
    return f'Buscando: {query}'

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    clave = request.form.get('clave')
    return f'Usuario: {usuario}, Clave: {clave}'

@app.route('/info')
def info():
    user_agent = request.headers.get('User-Agent')
    return f'Usas: {user_agent}'
@app.route('/inicio')
def inicio():
    return redirect('/bienvenida')
@app.route('/admin')
def admin():
    abort(403)  # Forbidden

if __name__ == "__main__":
    app.run(debug=True)