from functools import wraps
from flask import g, request, redirect, url_for

def login_required(argumento):
  def real_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
      #if g.user is None:
      if argumento == 2:
      #return redirect(url_for('login', next=request.url))
        print('ENTRO AL IF!!!')
      return function(*args, **kwargs)
    return wrapper
  return real_decorator
