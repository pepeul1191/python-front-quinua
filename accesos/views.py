# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request, render_template, redirect, session
from config.middleware import csrf_form

accesos = Blueprint('accesos', __name__)

@login.route('/login', methods=['GET'])
def index():
	data = {'mensaje' : False}
	return render_template('login/index.html', constants = constants, data = json.dumps(data))