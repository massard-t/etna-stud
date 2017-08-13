#!/usr/bin/env python
# coding: utf-8
"""
Main app file for etna-stud
"""
from flask import Flask

def main():
    app = Flask(__name__)

    app.run(host='127.0.0.1', port=8080, debug=True)

if __name__ == '__main__':
    main()
