# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

accesos_sistema = Blueprint('accesos_sistema', __name__)

@accesos_sistema.route('/accesos/sistema/listar', methods=['GET'])
def listar():
  r = requests.get(constants['servicios']['accesos'] + 'sistema/listar')
  return r.text