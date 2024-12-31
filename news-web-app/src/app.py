from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from routes import auth, news

app.register_blueprint(auth.bp)
app.register_blueprint(news.bp)

if __name__ == '__main__':
    app.run(debug=True)