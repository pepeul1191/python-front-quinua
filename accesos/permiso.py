# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

accesos_permiso = Blueprint('accesos_permiso', __name__)

@accesos_permiso.route('/accesos/permiso/listar/<sistema_id>', methods=['GET'])
def listar(sistema_id):
  r = requests.get(constants['servicios']['accesos'] + 'permiso/listar/' + sistema_id)
  return r.text

@accesos_permiso.route('/accesos/permiso/listar_asociados/<sistema_id>/<rol_id>', methods=['GET'])
def listar_asociados(sistema_id, rol_id):
  r = requests.get(constants['servicios']['accesos'] + 'permiso/listar_asociados/' + sistema_id + '/' + rol_id)
  return r.text

@accesos_permiso.route('/accesos/permiso/guardar', methods=['POST'])
def guardar():
  data = request.form['data']
  r = requests.post(constants['servicios']['accesos'] + 'permiso/guardar?data=' + data)
  return r.text