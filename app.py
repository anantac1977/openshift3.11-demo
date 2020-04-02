import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/Simple Request Message')
def hello():
    return 'Simple Response Message'

if __name__ == "__main__":
    app.run()
