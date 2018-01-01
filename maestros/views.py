# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request, render_template, redirect, session
from config.constants import constants
from config.middleware import csrf_form

maestros = Blueprint('maestros', __name__)

@maestros.route('/maestros/', methods=['GET'])
def index():
	menu = [
		{'url' : 'accesos/', 'nombre' : 'Accesos'},
    {'url' : 'maestros/', 'nombre' : 'Maestros'},
		{'url' : 'agricultores/', 'nombre' : 'Agricultores'},
		{'url' : 'estaciones/', 'nombre' : 'Estaciones'},
  ]
	items = [
		{"subtitulo":"Ubicaciones", "items":
			[
				{"item":"Departamentos, Provincias y Distritos","url":"maestros/#/ubicaciones"},
			]
		},
    {"subtitulo":"Archivos", "items":
			[
				{"item":"Extensiones","url":"maestros/#/extensiones"},
			]
		},
    {"subtitulo":"Estaciones", "items":
			[
				{"item":"Unidades de Medida","url":"maestros/#/unidad_medida"},
        {"item":"Tipos de Estaciones","url":"maestros/#/tipo_estacion"},
			]
		},
	]
	data = {'titulo_pagina' : 'Gestión Maestros', 'modulo' : 'Maestros'}
	return render_template('maestros/index.html', constants = constants, data = json.dumps(data), menu = json.dumps(menu), items = json.dumps(items))