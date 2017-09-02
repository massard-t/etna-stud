#!/usr/bin/env python
# coding: utf-8
"""
Main app file for etna-stud
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)  # pylint: disable=invalid-name


@app.route('/')
def index():
    """Test route"""
    return 'Test'


@app.route('/index')
def base_index():
    """Index route"""
    return render_template('index.html')


def main():
    """Runs the server"""

    app.run(host='127.0.0.1', port=8080, debug=True)

if __name__ == '__main__':
    main()
