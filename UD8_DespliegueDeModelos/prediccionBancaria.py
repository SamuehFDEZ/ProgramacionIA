from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
import joblib
import numpy as np

modelo = joblib.load('banco.joblib')
scaler = joblib.load('scaler.pkl')

app = Flask(__name__, template_folder='templates')
app.secret_key = 'clave_secreta'  # Requisito para CSRF
csrf = CSRFProtect(app)

class BbvaForm(FlaskForm):
    ingresos = StringField('income', validators=[DataRequired()])
    cantidad = StringField('amount', validators=[DataRequired()])
    tasaIntPres = StringField('int_rate', validators=[DataRequired()])
    mppIngresp = StringField('percent_income', validators=[DataRequired()])
    prestAnt = StringField('previous_loans', validators=[DataRequired()])
    hipoPro = StringField('ownership_MORTGAGE', validators=[DataRequired()])
    alqPro = StringField('ownership_RENT', validators=[DataRequired()])
    enviar = SubmitField('enviar')


@app.route('/', methods=['GET','POST'])
def procesar():
    try:
        form = BbvaForm()
        if form.validate_on_submit():
            ingresosFloat = float(form.ingresos.data)
            cantidadFloat = float(form.cantidad.data)
            tasaIntPresFloat = float(form.tasaIntPres.data)
            mppIngrespFloat = float(form.mppIngresp.data)
            prestAntFloat = float(form.prestAnt.data)
            hipoProFloat = float(form.hipoPro.data)
            alqProFloat = float(form.alqPro.data)

            datos = np.array([[ingresosFloat, cantidadFloat,tasaIntPresFloat
                                          ,mppIngrespFloat,prestAntFloat,hipoProFloat
                                          ,alqProFloat]])
            datos_escalados = scaler.transform(datos)
            prediccion = modelo.predict(datos_escalados)

            resultado = "Aprobado" if prediccion[0] == 1 else "Rechazado"

            return render_template('banco.html', form=form, resultado=resultado)
        return render_template('banco.html', form=form)
    except Exception as e:
        return f"Error en la predicción: {str(e)}"
if __name__ == "__main__":
    app.run(debug=True)
