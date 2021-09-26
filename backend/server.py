from flask import Flask
from config import Config
from api.router import apiRouter

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(apiRouter)

if __name__ == '__main__':
    app.run()