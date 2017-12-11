# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from config.constants import constants

error = Blueprint('error', __name__)

@error.route('/error/access/<int:error_id>', methods=['GET'])
def index(error_id):
	error_id = str(error_id)
	data = None
	options = {
		'404' : {'numero' : 404, 'mensaje' : 'Archivo no encontrado', 'descripcion' : 'La página que busca no se encuentra en el servidor', 'icono' : 'fa fa-exclamation-triangle'},
		'501': {'numero' : 501, 'mensaje' : 'Página en Contrucción', 'descripcion' : 'Lamentamos el incoveniente, estamos trabajando en ello.', 'icono' : 'fa fa-code-fork'},
		'5050': {'numero' : 5050, 'mensaje' : 'Acceso restringido', 'descripcion' : 'No cuenta con los privilegios necesarios.', 'icono' : 'fa fa-ban'},
		'5051': {'numero' : 5050, 'mensaje' : 'Acceso restringido', 'descripcion' : 'Necesita estar logueado.', 'icono' : 'fa fa-ban'},
		'8080': {'numero' : 8080, 'mensaje' : 'Tiempo de la sesion agotado', 'descripcion' : 'Vuelva a ingresar al sistema.', 'icono' : 'fa fa-clock-o'}
	}
	if error_id in options:
		data = options[error_id]
	else:
		data = options['404']
	return render_template('error/index.html', constants = constants, data = data)
