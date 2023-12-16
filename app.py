from flask import Flask
from flask_wtf.csrf import CSRFProject

app = Flask(__name__)
csrf = CSRFProject(app)

@app.route("/")
def pagina_inicial():
    return "App do Rubens - Deploy final"