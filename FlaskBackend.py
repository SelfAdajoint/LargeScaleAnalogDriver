#!/usr/bin/env python3
# pylint: disable=C0116,C0103,C0115,C0209

from flask import Flask, send_from_directory
from flask_restx import Api

app = Flask(__name__)
api = Api(app)

@api.route('/')
def index():
    return send_from_directory('./dist', 'index.html')

@api.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('./dist', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6662)
