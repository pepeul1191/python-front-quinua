# -*- coding: utf-8 -*-
import json
import requests
from flask import Blueprint, request, redirect, session
from config.constants import constants

agricultores_campo = Blueprint('agricultores_campo', __name__)