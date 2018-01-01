# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

maestros_departamento = Blueprint('maestros_departamento', __name__)

@maestros_departamento.route('/maestros/departamento/listar', methods=['GET'])
def listar():
  r = requests.get(constants['servicios']['ubicaciones'] + 'departamento/listar')
  return r.text

@maestros_departamento.route('/maestros/departamento/guardar', methods=['POST'])
def guardar():
  data = request.form['data']
  r = requests.post(constants['servicios']['ubicaciones'] + 'departamento/guardar?data=' + data)
  return r.text