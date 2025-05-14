from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def banco():
    return render_template('banco.html')

@app.route('/', methods=['POST'])
def predecir():
    return render_template('banco.html')

if __name__ == "__main__":
    app.run(debug=True)
