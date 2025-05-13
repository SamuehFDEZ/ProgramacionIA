from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def index():
    return render_template('404.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    tUsuario = None
    tClave = None

    if request.method == 'POST':
        tUsuario = request.form.get('nombre')
        clave = request.form.get('contrasenya')

        if tUsuario == 'Samuel' and clave == '123':
            tClave = clave  # Solo se asigna si es válida

    return render_template('index.html', tUsuario=tUsuario, tClave=tClave)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
