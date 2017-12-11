from functools import wraps
from flask import g, request, redirect, url_for
from .constants import constants

def login_required(argumento):
  def real_decorator(function):
    #@wraps(function)
    def wrapper(*args, **kwargs):
      #if g.user is None:
      print(request.args['data'])
      if argumento == 2:
      #return redirect(url_for('login', next=request.url))
        print('ENTRO AL IF!!!')
      return function(*args, **kwargs)
    return wrapper
  return real_decorator

def csrf_form():
  def real_decorator(function):
    #@wraps(function)
    def wrapper(*args, **kwargs):
      if request.form['csrfmiddlewaretoken'] != constants['CSRF'] and constants['ambiente'] != 'test':
        return redirect(constants['BASE_URL'] + 'error/access/5050')
      return function(*args, **kwargs)
    return wrapper
  return real_decorator
