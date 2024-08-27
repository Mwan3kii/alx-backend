#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Set languages and babel defaults"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Funtion that renders the html template"""
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """Get locale from request with the decorator"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
