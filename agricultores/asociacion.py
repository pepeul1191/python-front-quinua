# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

agricultores_asociacion = Blueprint('agricultores_asociacion', __name__)

@agricultores_asociacion.route('/agricultores/asociacion/listar', methods=['GET'])
def listar():
  r = requests.get(constants['servicios']['agricultores'] + 'asociacion/listar')
  return r.text

@agricultores_asociacion.route('/agricultores/asociacion/guardar', methods=['POST'])
def guardar():
  data = request.form['data']
  r = requests.post(constants['servicios']['agricultores'] + 'asociacion/guardar?data=' + data)
  return r.text