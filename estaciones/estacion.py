# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

estaciones_estacion = Blueprint('estaciones_estacion', __name__)

@estaciones_estacion.route('/estaciones/estacion/listar', methods=['GET'])
def listar():
  r = requests.get(constants['servicios']['estaciones'] + 'estacion/listar')
  return r.text

@estaciones_estacion.route('/estaciones/estacion/guardar', methods=['POST'])
def guardar():
  data = request.form['data']
  r = requests.post(constants['servicios']['estaciones'] + 'estacion/guardar?data=' + data)
  return r.text

@estaciones_estacion.route('/estaciones/estacion/sensor/<estacion_id>', methods=['GET'])
def sensor(estacion_id):
  r = requests.get(constants['servicios']['estaciones'] + 'sensor/listar/' +  estacion_id)
  return r.text