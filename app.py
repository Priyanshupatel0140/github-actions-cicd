from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello Priyanshu! CI/CD deployment is coming."


if __name__ == "__main__":
    app.run()