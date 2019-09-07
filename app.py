import os

from flask import Flask

app = Flask(__name__)


def create_app(test_config=None):

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
