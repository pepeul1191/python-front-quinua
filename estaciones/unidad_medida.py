# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

estaciones_unidad_medida = Blueprint('estaciones_unidad_medida', __name__)

@estaciones_unidad_medida.route('/estaciones/unidad_medida/listar', methods=['GET'])
def listar():
  r = requests.get(constants['servicios']['estaciones'] + 'unidad_medida/listar')
  return r.text

@estaciones_unidad_medida.route('/estaciones/unidad_medida/guardar', methods=['POST'])
def guardar():
  data = request.form['data']
  r = requests.post(constants['servicios']['estaciones'] + 'unidad_medida/guardar?data=' + data)
  return r.text

@estaciones_unidad_medida.route('/estaciones/unidad_medida/listar_select', methods=['POST'])
def listar_select():
  r = requests.post(constants['servicios']['estaciones'] + 'unidad_medida/listar_select')
  return r.text