# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request, render_template, redirect, session
from config.constants import constants
from config.middleware import csrf_form

agricultores = Blueprint('agricultores', __name__)

@agricultores.route('/agricultores/', methods=['GET'])
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
				{"item":"Gestión de Responsables","url":"agricultores/#/responsable"},
        {"item":"Gestión de Asociaciones","url":"agricultores/#/asociacion"},
			]
		},
	]
	data = {'titulo_pagina' : 'Gestión Agricultores', 'modulo' : 'Agricultores'}
	return render_template('agricultores/index.html', constants = constants, data = json.dumps(data), menu = json.dumps(menu), items = json.dumps(items))