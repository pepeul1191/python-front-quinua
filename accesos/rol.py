# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

accesos_rol = Blueprint('accesos_rol', __name__)

@accesos_rol.route('/accesos/rol/listar/<sistema_id>', methods=['GET'])
def listar(sistema_id):
  r = requests.get(constants['servicios']['accesos'] + 'rol/listar/' + sistema_id)
  return r.text

@accesos_rol.route('/accesos/rol/guardar', methods=['POST'])
def guardar():
  data = request.form['data']
  r = requests.post(constants['servicios']['accesos'] + 'rol/guardar?data=' + data)
  return r.text

@accesos_rol.route('/accesos/rol/asociar_permisos', methods=['POST'])
def asociar_permisos():
  data = request.form['data']
  r = requests.post(constants['servicios']['accesos'] + 'rol/asociar_permisos?data=' + data)
  return r.text