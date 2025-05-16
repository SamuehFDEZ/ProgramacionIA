from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
import joblib
import numpy as np

modelo = joblib.load('banco.joblib')
scaler = joblib.load('scaler.pkl')
encoder = joblib.load('encoder.joblib')
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
    prestAnt = SelectField('previous_loans', choices=[('0', 'Sin impagos'),
                                                      ('1', 'Con impagos')],
                           validators=[DataRequired()])
    hipoPro = SelectField('ownership_MORTGAGE', choices=[('0', 'Renta'),
                                                         ('1', 'Propio'),
                                                         ('2', 'Hipoteca')],
                          validators=[DataRequired()])
    alqPro = SelectField('ownership_RENT', choices=[('0', 'No tiene'),
                                                    ('1', 'Tiene alquiler')],
                         validators=[DataRequired()])
    enviar = SubmitField('Enviar')


@app.route('/', methods=['GET','POST'])
def procesar():
    try:
        form = BbvaForm()
        if form.validate_on_submit():
            # Variables numéricas
            ingresosFloat = float(form.ingresos.data)
            cantidadFloat = float(form.cantidad.data)
            tasaIntPresFloat = float(form.tasaIntPres.data)
            mppIngrespFloat = float(form.mppIngresp.data)

            # Variables categóricas como texto (si fueron codificadas con strings)
            prestAnt = form.prestAnt.data  # string tipo '0' o '1'
            hipoPro = form.hipoPro.data
            alqPro = form.alqPro.data

            # Construir arrays para encoder y scaler
            # Asumiendo que el encoder espera [['0', '2']] (strings)
            datos_cat = np.array([[hipoPro, alqPro]])
            datos_cat_encoded = encoder.fit_transform(datos_cat)

            datos_num = np.array([[ingresosFloat, cantidadFloat, tasaIntPresFloat,
                                   mppIngrespFloat, float(prestAnt)]])  # prestAnt numérico

            # Concatenar numéricas + codificadas
            datos_finales = np.hstack((datos_num, datos_cat_encoded))

            # Escalar (si el scaler fue ajustado después del encoder)
            datos_escalados = scaler.transform(datos_finales)

            prediccion = modelo.predict(datos_escalados)
            resultado = "Aprobado" if prediccion[0] == 1 else "Rechazado"

            return render_template('banco.html', form=form, resultado=resultado)
        return render_template('banco.html', form=form)
    except Exception as e:
        return f"Error en la predicción: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)