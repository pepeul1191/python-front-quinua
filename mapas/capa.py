# -*- coding: utf-8 -*-
from bson.json_util import dumps
from flask import Blueprint, request
from config.database import db_peru_gis
from config.middleware import login_required

mapas_capa = Blueprint('mapas_capa', __name__)

@mapas_capa.route('/mapas/capa/carreteras', methods=['GET'])
@login_required(False)
def carreteras():
	rs = db_peru_gis['roads'].find()
	return dumps([dict(r) for r in rs])
	
