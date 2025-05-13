from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('nombre')
        clave = request.form.get('contrasenya')

        if usuario == 'Samuel' and clave == '123':
            return render_template('index.html', tUsuario=usuario, tClave=clave)

        return render_template('index.html', tUsuario=usuario, tClave=None)  # Falló login
    return render_template('index.html', tUsuario=None, tClave=None)  # GET


if __name__ == "__main__":
    app.run(debug=True)
    app.run(port=8000)