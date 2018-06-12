from flask import Flask

a = Flask(__name__)

@a.route("/")
def greeting():
    return "Hello, I am May Thu Htun"

@a.route("/tiide")
def tiide():
    return "I am from Computer University Mandalay"

if __name__ == "__main__":
    a.run(debug=True)
