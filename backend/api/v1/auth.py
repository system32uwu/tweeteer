from flask import Blueprint, request, session, jsonify
from models.user import User

authRouter = Blueprint('auth', __name__, url_prefix='/auth')

@authRouter.post('/login')
def login():
    data = request.get_json()
    user, token = User.login(data['email'], data['password'])

    if user is not None and token is not None:
        session['authToken'] = token
        return jsonify(user)
    else:
        return jsonify({
            'error': 'incorrect email or password'
        }), 400

@authRouter.post('/logout')
def logout():
    session.pop('authToken', None)
    return jsonify({"status": "OK"}), 200