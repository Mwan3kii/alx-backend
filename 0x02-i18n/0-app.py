#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Funtion that renders the html template"""
    return render_template('index.html')
