from middleware.authGuard import requiresAuth
from flask import Blueprint, request, session, jsonify
from models.user import User

userRouter = Blueprint('user', __name__, url_prefix='/user')

@userRouter.get('/<int:id>')
def getUserById(id:int):
    return jsonify(User.getById(id)), 200

@userRouter.post('/')
def saveUser():
    data = request.get_json()
    return jsonify(User.save(data['username'], data['email'], data['password'])), 200

@userRouter.delete('/')
@requiresAuth
def deleteUser(idUser:int):
    session.pop('authToken')
    return jsonify({'affected rows': User.deleteById(idUser)}), 200

@userRouter.put('/')
@requiresAuth
def updateUser(idUser:int):
    data = request.get_json()
    result = User.updateById(idUser, data['username'], data['email'], data['password'])
    return jsonify({'affected rows': result}), 200