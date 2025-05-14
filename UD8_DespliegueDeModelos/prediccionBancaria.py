from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__, template_folder='templates')
app.secret_key = 'clave_secreta'  # Requisito para CSRF
csrf = CSRFProtect(app)

class BbvaForm(FlaskForm):
    ingresos = StringField('income', validators=[DataRequired()]),
    cantidad = StringField('amount', validators=[DataRequired()]),
    tasaIntPres = StringField('int_rate', validators=[DataRequired()]),
    mppIngresp = StringField('percent_income', validators=[DataRequired()]),
    prestAnt = StringField('previous_loans', validators=[DataRequired()]),
    hipoPro = StringField('ownership_MORTGAGE', validators=[DataRequired()]),
    alqPro = StringField('ownership_RENT', validators=[DataRequired()]),
    enviar = SubmitField('enviar')


@app.route('/', methods=['GET','POST'])
def procesar():
    form = BbvaForm()
    if form.validate_on_submit():
        return f"Recibido: {form.ingresos} - {form.alqPro}"
    return render_template('banco.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
