#!/usr/bin/env python
# -*- coding: utf-8 -*-
# app.py
import os
from flask import Flask, request, render_template
from error.views import error
from config.constants import constants
#imports-accesos
from accesos.views import accesos
from accesos.item import accesos_item
from accesos.modulo import accesos_modulo
from accesos.permiso import accesos_permiso
from accesos.rol import accesos_rol
from accesos.sistema import accesos_sistema
from accesos.subtitulo import accesos_subtitulo
from accesos.usuario import accesos_usuario
#imports-agricultores
from agricultores.views import agricultores
#imports-maestros
from maestros.views import maestros
from maestros.departamento import maestros_departamento
from maestros.provincia import maestros_provincia
from maestros.distrito import maestros_distrito
#imports-estaciones
from estaciones.unidad_medida import estaciones_unidad_medida
from estaciones.tipo_estacion import estaciones_tipo_estacion

app = Flask(__name__)
#cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.register_blueprint(error)
#register-agricutlores
app.register_blueprint(agricultores)
#register-accesos
app.register_blueprint(accesos)
app.register_blueprint(accesos_item)
app.register_blueprint(accesos_modulo)
app.register_blueprint(accesos_permiso)
app.register_blueprint(accesos_rol)
app.register_blueprint(accesos_sistema)
app.register_blueprint(accesos_subtitulo)
app.register_blueprint(accesos_usuario)
#register-accesos
app.register_blueprint(maestros)
app.register_blueprint(maestros_departamento)
app.register_blueprint(maestros_provincia)
app.register_blueprint(maestros_distrito)
#register-estaciones
app.register_blueprint(estaciones_unidad_medida)
app.register_blueprint(estaciones_tipo_estacion)

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

@app.after_request
def apply_caching(response):
  response.headers['Server'] = 'Python; Ubuntu; Flask; Werkzeug;'
  return response

if __name__ == '__main__':
	app.secret_key = constants['key']
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run(debug=True, host='0.0.0.0', port=3000)
