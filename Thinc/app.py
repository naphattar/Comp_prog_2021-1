from flask import flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, Flask"

if __name__ == "__main__":
    app.run(port = 3000,debug =True)