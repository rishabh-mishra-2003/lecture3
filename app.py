from flask import Flask

app= Flask(__name__)

@app.route("/")
def index():
      return "Hello ld"

@app.route("/<string:name>")   
def rishabh(name):
    return f"hello {name}"   


