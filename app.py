from flask import Flask
from flask_wtf.csrf import CSRFProject

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "App do Rubens - Deploy final"