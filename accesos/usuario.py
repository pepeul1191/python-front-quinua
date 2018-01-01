# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
from config.middleware import login_required

accesos_usuario = Blueprint('accesos_usuario', __name__)

@accesos_usuario.route('/accesos/usuario/listar', methods=['GET'])
@login_required(True)
def listar():
  return json.dumps('xd')
