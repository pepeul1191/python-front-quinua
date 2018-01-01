# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

reportes_reporte = Blueprint('reportes_reporte', __name__)

@reportes_reporte.route('/reporte/datos_dia', methods=['GET'])
def datos_dia():
  sensor_id = request.args.get('sensor_id')
  dia = request.args.get('dia')
  r = requests.get(constants['servicios']['sensores'] + 'reporte/datos_dia?sensor_id=' + sensor_id + '&dia=' + dia)
  return r.text

@reportes_reporte.route('/reporte/max_min_avg_dias', methods=['GET'])
def max_min_avg_dias():
  sensor_id = request.args.get('sensor_id')
  inicio = request.args.get('inicio')
  fin = request.args.get('fin')
  r = requests.get(constants['servicios']['sensores'] + 'reporte/max_min_avg_dias?sensor_id=' + sensor_id + '&inicio=' + inicio + '&fin=' + fin)
  return r.text
