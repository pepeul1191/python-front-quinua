# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

accesos_modulo = Blueprint('accesos_modulo', __name__)

@accesos_modulo.route('/accesos/modulo/listar/<sistema_id>', methods=['GET'])
def listar(sistema_id):
  r = requests.get(constants['servicios']['accesos'] + 'modulo/listar/' + sistema_id)
  return r.text

@accesos_modulo.route('/accesos/modulo/guardar', methods=['POST'])
def guardar():
  data = request.form['data']
  r = requests.post(constants['servicios']['accesos'] + 'modulo/guardar?data=' + data)
  return r.text