# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

accesos_subtitulo = Blueprint('accesos_subtitulo', __name__)

@accesos_subtitulo.route('/accesos/subtitulo/listar/<modulo_id>', methods=['GET'])
def listar(modulo_id):
  r = requests.get(constants['servicios']['accesos'] + 'subtitulo/listar/' + modulo_id)
  return r.text

@accesos_subtitulo.route('/accesos/subtitulo/guardar/', methods=['POST'])
def guardar():
  data = request.form['data']
  r = requests.post(constants['servicios']['accesos'] + 'subtitulo/guardar?data=' + data)
  return r.text