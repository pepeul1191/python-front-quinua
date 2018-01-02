# -*- coding: utf-8 -*-
import json
import pysftp
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

estaciones_campo = Blueprint('estaciones_campo', __name__)

@estaciones_campo.route('/agricultores/campo/listar/<asociacion_id>', methods=['GET'])
def listar(asociacion_id):
  r = requests.get(constants['servicios']['agricultores'] + 'campo/listar/' + asociacion_id)
  campos = json.loads(r.text)
  rpta = []
  if len(campos) != 0:
    for campo in campos:
      distrito_id = campo['distrito_id']
      rc = requests.get(constants['servicios']['ubicaciones'] + 'distrito/nombre/' + str(distrito_id))
      campo['distrito'] = rc.text
      rpta.append(campo)
  return json.dumps(rpta)

@estaciones_campo.route('/agricultores/campo/guardar', methods=['POST'])
def guardar():
  data = request.form['data']
  r = requests.post(constants['servicios']['agricultores'] + 'campo/guardar?data=' + data)
  return r.text

@estaciones_campo.route('/agricultores/campo/obtener_ruta_foto/<imagen_id>', methods=['GET'])
def obtener_ruta_foto(imagen_id):
  r = requests.get(constants['servicios']['archivos'] + 'imagen/obtener_ruta_archivo/' + imagen_id)
  return r.text

@estaciones_campo.route('/agricultores/campo/estacion/<campo_id>', methods=['GET'])
def estacion(campo_id):
  r = requests.get(constants['servicios']['estaciones'] + 'estacion/campo/' + campo_id)
  return r.text

@estaciones_campo.route('/agricultores/campo/subir_foto', methods=['POST'])
def subir_foto():
  rpta = 'Error'
  r = requests.get(constants['servicios']['archivos'] + 'imagen/obtener_id')
  id_generado = r.text
  file = request.files['myFile']
  t = file.filename.split('.')
  extension = t[1]
  file.filename = id_generado + '.' + extension
  file.save('/tmp/' + file.filename)
  with pysftp.Connection(constants['servicios']['ftp']['dominio'], username = constants['servicios']['ftp']['usuario'], password = constants['servicios']['ftp']['contrasenia']) as sftp:
    with sftp.cd(constants['servicios']['ftp']['ruta']):
      sftp.put('/tmp/' + file.filename)
      imagen = {
        'id': id_generado,
        #'nombre': 'Corbett', 
        'nombre_generado': id_generado + '.' + extension, 
        'extension': extension,
        'ruta': constants['servicios']['ftp']['ruta'] + id_generado + '.' + extension,
        #:altura => ,
        #:anchura => ,
        #:mime => ,
      }
      r = requests.post(constants['servicios']['archivos'] + 'imagen/crear?data=' + json.dumps(imagen))
      rpta = r.text
  return rpta
