from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<p> Hola Mundo <p>"



if __name__ == "__main__":
    app.run(debug=True)