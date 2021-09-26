import sqlite3
from flask import Blueprint
from flask.json import jsonify
from api.v1.user import userRouter
from api.v1.post import postRouter
from api.v1.auth import authRouter

apiRouter = Blueprint('api', __name__, url_prefix='/api') #http://localhost:5000/api

v1Router = Blueprint('v1', __name__, url_prefix='/v1') #http://localhost:5000/api/v1

apiRouter.register_blueprint(v1Router) # http://localhost:5000/api/v1

v1Router.register_blueprint(userRouter) # http://localhost:5000/api/v1/user
v1Router.register_blueprint(postRouter) # http://localhost:5000/api/v1/post
v1Router.register_blueprint(authRouter) # http://localhost:5000/api/v1/auth

@apiRouter.errorhandler(sqlite3.IntegrityError)
def integrityError(e: sqlite3.IntegrityError):
    err = str(e)
    
    if 'UNIQUE' in err:
        return jsonify({
            "error": "record already exists",
            "fields": str(e).split(": ")[1]
        }), 400
    elif 'NOT NULL' in err:
        return jsonify({
            "error": "missing mandatory fields (can't be null)",
            "fields": str(e).split(": ")[1]
        }), 400
    elif 'FOREIGN KEY' in err:
        return jsonify({"error": "referenced foreign key(s) don't exist"}), 400
    else:
        return jsonify({"error": err}), 400

@apiRouter.errorhandler(KeyError)
def keyError(e: KeyError):
    return jsonify({
        "error": "missing required fields",
        "fields": str(e)
    }), 400

@apiRouter.errorhandler(TypeError)
def typeError(e: TypeError):
    return {"error": "resource not found"}, 404