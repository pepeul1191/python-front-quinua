# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

maestros_distrito = Blueprint('maestros_distrito', __name__)

@maestros_distrito.route('/maestros/distrito/listar/<provincia_id>', methods=['GET'])
def listar(provincia_id):
  r = requests.get(constants['servicios']['ubicaciones'] + 'distrito/listar/' + provincia_id)
  return r.text

@maestros_distrito.route('/maestros/distrito/guardar', methods=['POST'])
def guardar():
  data = request.form['data']
  r = requests.post(constants['servicios']['ubicaciones'] + 'distrito/guardar?data=' + data)
  return r.text