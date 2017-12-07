#!/usr/bin/env python
# -*- coding: utf-8 -*-
# app.py
import os
from flask import Flask, request, render_template

app = Flask(__name__)
#cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.errorhandler(404)
def not_found(e):
    return 'Error: Recurso no encontrado', 404

@app.errorhandler(500)
def server_error(e):
    return render_template('error/500.html'), 500

@app.route('/')
def index():
	return 'Error : URI vacía'

@app.route('/test/conexion')
def test_conexion():
	return 'Ok'

@app.route('/login')
def home():
	return render_template('login/index.html')

@app.after_request
def apply_caching(response):
    response.headers['Server'] = 'Python; Ubuntu; Flask; Werkzeug;'
    return response

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=3000)
