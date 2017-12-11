# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request, render_template
from config.middleware import login_required
from config.constants import constants

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET'])
def index():
	data = {'mensaje' : False}
	#context = {'helper' : Helper(), 'data':  json.dumps(data),'menu' : '', 'items' : ''}
	return render_template('login/index.html', constants = constants, data = json.dumps(data))