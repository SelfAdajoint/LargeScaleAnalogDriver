#!/usr/bin/env python3
# pylint: disable=C0116,C0103,C0115,C0209

from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('./dist', 'index.html')

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory('./dist', filename)

if __name__ == '__main__':
    app.run()
