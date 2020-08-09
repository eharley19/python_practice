from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/home")
def home():
    return "Hello this is the main page <h1>HELLO</h1>"


@app.route("/index")
def index():
    return jsonify(heading="Michael's Coding Class")


if __name__ == "__main__":
    app.run()
