#!/usr/bin/env python3
# pylint: disable=C0116,C0103,C0115,C0209

#!/usr/bin/env python3

from sanic import Sanic
from sanic.response import file

app = Sanic(__name__)

# @app.middleware('response')
# async def add_cors_headers(request, response):
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Methods'] = 'GET, POST'

@app.route('/')
async def index(request):
    return await file('./dist/index.html')

@app.route('/<filename:path>')
async def serve_file(request, filename):
    return await file(f'./dist/{filename}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6662)

# from flask import Flask, send_from_directory

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return send_from_directory('./dist', 'index.html')

# @app.route('/<path:filename>')
# def serve_file(filename):
#     return send_from_directory('./dist', filename)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=6662)
