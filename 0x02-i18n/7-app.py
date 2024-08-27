#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz import UnknownTimeZoneError

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return render_template('7-index.html')


@babel.localeselector
def get_locale():
    """Get locale from request with the decorator"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Returns user ditionary or none if id cant be found"""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """Use get user to find users and set global"""
    g.user = get_user()


@babel.timezoneselector
def get_timezone() -> str:
    """Find timezone in url parameter from user settings"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass
    if g.user and g.user.get('timezone'):
        timezone = g.user['timezone']
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == '__main__':
    app.run(debug=True)
