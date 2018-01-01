# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request, render_template, redirect, session
from config.constants import constants
from config.middleware import csrf_form

estaciones = Blueprint('estaciones', __name__)

@estaciones.route('/estaciones/', methods=['GET'])
def index():
	menu = [
		{'url' : 'accesos/', 'nombre' : 'Accesos'},
    {'url' : 'maestros/', 'nombre' : 'Maestros'},
		{'url' : 'agricultores/', 'nombre' : 'Agricultores'},
		{'url' : 'estaciones/', 'nombre' : 'Estaciones'},
  ]
	items = [
		{"subtitulo":"Opciones", "items":
			[
				{"item":"Gestión de Sensores","url":"estaciones/#/sensores"},
        {"item":"Datos de Sensores","url":"estaciones/#/datos"},
			]
		},
	]
	data = {'titulo_pagina' : 'Gestión Estaciones', 'modulo' : 'Estaciones'}
	return render_template('estaciones/index.html', constants = constants, data = json.dumps(data), menu = json.dumps(menu), items = json.dumps(items))