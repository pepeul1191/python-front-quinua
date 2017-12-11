# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request
from config.database import engine_accesos, session_accesos
from sqlalchemy.sql import select, text, and_
from .models import Usuario
from config.middleware import login_required

accesos_usuario = Blueprint('accesos_usuario', __name__)

@accesos_usuario.route('/accesos/usuario/listar', methods=['GET'])
@login_required(True)
def listar():
  conn = engine_accesos.connect()
  stmt = """
    SELECT U.id AS id, U.usuario AS usuario, A.momento AS momento, U.correo AS correo
    FROM usuarios U INNER JOIN accesos A ON U.id = A.usuario_id
    GROUP BY U.usuario ORDER BY U.id
  """
  return json.dumps([dict(r) for r in conn.execute(stmt)])
