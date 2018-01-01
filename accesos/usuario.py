# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

accesos_usuario = Blueprint('accesos_usuario', __name__)

@accesos_usuario.route('/accesos/usuario/listar', methods=['GET'])
def listar():
  r = requests.get(constants['servicios']['accesos'] + 'usuario/listar')
  return r.text

@accesos_usuario.route('/accesos/usuario/logs/<usuario_id>', methods=['GET'])
def logs(usuario_id):
  r = requests.get(constants['servicios']['accesos'] + 'usuario/listar_accesos/' + usuario_id)
  return r.text
