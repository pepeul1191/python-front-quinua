# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

accesos_usuario = Blueprint('accesos_usuario', __name__)

@accesos_usuario.route('/accesos/usuario/listar', methods=['GET'])
def listar():
  r = requests.get(constants['servicios']['accesos'] + 'usuario/listar')
  return r.text

@accesos_usuario.route('/accesos/usuario/logs/<usuario_id>', methods=['GET'])
def logs(usuario_id):
  r = requests.get(constants['servicios']['accesos'] + 'usuario/listar_accesos/' + usuario_id)
  return r.text

@accesos_usuario.route('/accesos/usuario/obtener_usuario_correo/<usuario_id>', methods=['GET'])
def obtener_usuario_correo(usuario_id):
  r = requests.get(constants['servicios']['accesos'] + 'usuario/obtener_usuario_correo/' + usuario_id)
  return r.text

@accesos_usuario.route('/accesos/usuario/nombre_repetido', methods=['POST'])
def nombre_repetido():
  data = request.form['data']
  r = requests.post(constants['servicios']['accesos'] + 'usuario/nombre_repetido?data=' + data)
  return r.text

@accesos_usuario.route('/accesos/usuario/correo_repetido', methods=['POST'])
def correo_repetido():
  data = request.form['data']
  r = requests.post(constants['servicios']['accesos'] + 'usuario/correo_repetido?data=' + data)
  return r.text

@accesos_usuario.route('/accesos/usuario/guardar_usuario_correo', methods=['POST'])
def guardar_usuario_correo():
  usuario = request.form['usuario']
  r = requests.post(constants['servicios']['accesos'] + 'usuario/guardar_usuario_correo?usuario=' + usuario)
  return r.text

@accesos_usuario.route('/accesos/usuario/listar_sistemas/<usuario_id>', methods=['GET'])
def listar_sistemas(usuario_id):
  r = requests.get(constants['servicios']['accesos'] + 'sistema/usuario/' + usuario_id)
  return r.text

@accesos_usuario.route('/accesos/usuario/guardar_sistemas', methods=['POST'])
def guardar_sistemas():
  data = request.form['data']
  r = requests.post(constants['servicios']['accesos'] + 'usuario/guardar_sistemas?data=' + data)
  return r.text