from flask import Flask, url_for, redirect


def create_app(config):
    app = Flask(__name__)

    @app.route('/')
    @app.route('/static')
    @app.route('/static/')
    def index():
        return redirect(url_for('static', filename='index.html'))

    return app
