from flask import Flask, render_template, request, abort, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email
app = Flask(__name__, template_folder='templates')

@app.route('/login', methods=['GET', 'POST'])
def login():
    mensaje = ""
    if request.method == 'POST':
        nombre = 'Samuel'
        contrasenya = '123456'
        if (request.form.get('nombre') == nombre and
                request.form.get('contrasenya') == contrasenya):
            mensaje = "<p>Bienvenido, Samuel.</p>"
        else:
            mensaje = "<p>Credenciales incorrectas.</p>"
    return render_template("index.html", mensaje=mensaje, nombre=nombre)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(port=8000)