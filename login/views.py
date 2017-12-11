# -*- coding: utf-8 -*-
import json
import datetime
from flask import Blueprint, request, render_template, redirect, session
from sqlalchemy.sql import select, and_, func
from config.middleware import login_required
from config.constants import constants
from config.database import engine_accesos
from accesos.models import Usuario

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET'])
def index():
	data = {'mensaje' : False}
	return render_template('login/index.html', constants = constants, data = json.dumps(data))

@login.route('/login/acceder', methods=['POST'])
def acceder():
	usuario = request.form['usuario']
	contrasenia = request.form['contrasenia']
	conn = engine_accesos.connect()
	stmt = select([Usuario]).where(and_(Usuario.usuario == usuario, Usuario.contrasenia == contrasenia)).count()
	rpta = None
	for r in conn.execute(stmt):
		session['estado'] = 'autenticado'
		session['usuario'] = 'XD'
		session['tiempo'] = datetime.datetime.now()
		rpta = r[0]
	if int(rpta) == 1:
		return redirect(constants['BASE_URL'] + 'libros')
	else:
		data = {'mensaje' : True}
		return render_template('login/index.html', constants = constants, data = json.dumps(data))

@login.route('/login/ver', methods=['GET'])
def ver():
	try:
		rpta = 'usuario : ' + session['usuario'] + '</br>' + 'estado : ' + session['estado'] + '</br>' + 'tiempo : ' + str(session['tiempo'])
		return rpta
	except KeyError:
		return 'Unas de las variables de session del usuario no están seteadas', 500

@login.route('/login/salir', methods=['GET'])
def salir():
	session.clear()
	return redirect(constants['BASE_URL'] + 'login')