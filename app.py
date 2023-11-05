"""This file handles the application logic and is the entrypoint for the application."""


from flask import Flask
from src.controllers.hello_controller import hello_blueprint

app = Flask(__name__)
app.register_blueprint(hello_blueprint, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
