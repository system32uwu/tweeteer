from flask import session
from functools import wraps

from flask.json import jsonify
from models.user import User

def requiresAuth(f):
    @wraps(f)
    def decorator(*args,**kwargs):
        token = None
        try:
            token = session['authToken']
        except: # flask out of context error (raises when starting the app)
            pass
        
        if token is None:
            return jsonify({'error': 'not authenticated'}), 401
        else:
            idUser = User.verifyToken(token)
            return f(*args, **kwargs, idUser=idUser)
        
    return decorator