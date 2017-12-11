from functools import wraps
from flask import g, request, redirect, url_for, session
from .constants import constants

def login_required(argumento):
  def real_decorator(function):
    def wrapper(*args, **kwargs):
      try:
        estado = session['estado']
        if argumento != True and session['estado'] != 'autenticado':
          return redirect(constants['BASE_URL'] + 'error/access/5050')
      except KeyError:
        return redirect(constants['BASE_URL'] + 'error/access/5050')
      return function(*args, **kwargs)
    return wrapper
  return real_decorator

def csrf_form():
  def real_decorator(function):
    def wrapper(*args, **kwargs):
      if request.form['csrfmiddlewaretoken'] != constants['CSRF'] and constants['ambiente'] != 'test':
        return redirect(constants['BASE_URL'] + 'error/access/5050')
      return function(*args, **kwargs)
    return wrapper
  return real_decorator
