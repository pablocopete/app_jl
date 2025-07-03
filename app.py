from flask import Flask, request, jsonify
import requests


app = Flask(__name__)


@app.route("/", methods=["GET"])
def hola():
    return """<h1>FUNCIONA!!!!</h1><p style="color:red!">madafaquer!</p>"""

@app.route("/chiste", methods=["GET"])
def chiste():
    chiste = requests.get("https://official-joke-api.appspot.com/random_joke").json()
    chiste = chiste["setup"] + "\n"+ chiste["punchline"]
    return chiste 


if __name__ == "__main__":
    app.run(debug=True)
