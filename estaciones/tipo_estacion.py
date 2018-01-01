# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

estaciones_tipo_estacion = Blueprint('estaciones_tipo_estacion', __name__)

@estaciones_tipo_estacion.route('/estaciones/tipo_estacion/listar', methods=['GET'])
def listar():
  r = requests.get(constants['servicios']['estaciones'] + 'tipo_estacion/listar')
  return r.text

@estaciones_tipo_estacion.route('/estaciones/tipo_estacion/guardar', methods=['POST'])
def guardar():
  data = request.form['data']
  r = requests.post(constants['servicios']['estaciones'] + 'tipo_estacion/guardar?data=' + data)
  return r.text