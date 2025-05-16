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
    ingresos = StringField('income', validators=[DataRequired()],
                           render_kw={"placeholder": "15.000 – 150.000"})
    cantidad = StringField('amount', validators=[DataRequired()],
                           render_kw={"placeholder": "1.000 – 100.000"})
    tasaIntPres = StringField('int_rate', validators=[DataRequired()],
                              render_kw={"placeholder": "5.5 - 13.0 - 20.0"})
    mppIngresp = StringField('percent_income', validators=[DataRequired()],
                             render_kw={"placeholder": "15.0, 30.0, 45.0"})
    prestAnt = StringField('previous_loans', validators=[DataRequired()],
                           render_kw={"placeholder": "0 = sin impagos, 1 = con impagos"})
    hipoPro = StringField('ownership_MORTGAGE', validators=[DataRequired()],
                          render_kw={"placeholder": "0 = renta, 1 = propio, 2 = hipoteca"})
    alqPro = StringField('ownership_RENT', validators=[DataRequired()],
                         render_kw={"placeholder": "0 = no tiene, 1 = tiene alquiler"})
    enviar = SubmitField('Enviar')



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