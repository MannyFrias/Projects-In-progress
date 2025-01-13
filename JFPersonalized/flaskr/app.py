from flask import Flask

app = Flask(__name__)


@app.route('/layout.html')
def hello():
    return 'Hello, World!'