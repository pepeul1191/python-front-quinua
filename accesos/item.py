# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

accesos_item = Blueprint('accesos_item', __name__)

@accesos_item.route('/accesos/item/listar/<modulo_id>', methods=['GET'])
def listar(modulo_id):
  r = requests.get(constants['servicios']['accesos'] + 'item/listar/' + modulo_id)
  return r.text

@accesos_item.route('/accesos/item/guardar/', methods=['POST'])
def guardar():
  data = request.form['data']
  r = requests.post(constants['servicios']['accesos'] + 'item/guardar?data=' + data)
  return r.text