# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

maestros_provincia = Blueprint('maestros_provincia', __name__)

@maestros_provincia.route('/maestros/provincia/listar/<departamento_id>', methods=['GET'])
def listar(departamento_id):
  r = requests.get(constants['servicios']['ubicaciones'] + 'provincia/listar/' + departamento_id)
  return r.text

@maestros_provincia.route('/maestros/provincia/guardar', methods=['POST'])
def guardar():
  data = request.form['data']
  r = requests.post(constants['servicios']['ubicaciones'] + 'provincia/guardar?data=' + data)
  return r.text