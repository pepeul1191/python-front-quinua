# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

agricultores_responsable = Blueprint('agricultores_responsable', __name__)

@agricultores_responsable.route('/agricultores/responsable/listar', methods=['GET'])
def listar():
  r = requests.get(constants['servicios']['agricultores'] + 'responsable/listar')
  return r.text

@agricultores_responsable.route('/agricultores/responsable/guardar', methods=['POST'])
def guardar():
  data = request.form['data']
  r = requests.post(constants['servicios']['agricultores'] + 'responsable/guardar?data=' + data)
  return r.text

@agricultores_responsable.route('/agricultores/responsable/buscar', methods=['GET'])
def buscar():
  responsable = request.args.get('responsable')
  r = requests.get(constants['servicios']['agricultores'] + 'responsable/buscar?responsable=' + responsable)
  return r.text