from flask import Blueprint, request, jsonify
from models.user import User

userRouter = Blueprint('user', __name__, url_prefix='/user')

@userRouter.get('/<int:id>')
def getUserById(id:int):
    return jsonify(User.getById(id)), 200

@userRouter.post('/')
def saveUser():
    data = request.get_json()
    return jsonify(User.save(data['username'], data['email'], data['password'])), 200

@userRouter.delete('/<int:id>')
def deleteUser(id:int):
    return jsonify({'affected rows': User.deleteById(id)}), 200

@userRouter.put('/<int:id>')
def updateUser(id:int):
    data = request.get_json()
    result = User.updateById(id, data['username'], data['email'], data['password'])
    return jsonify({'affected rows': result}), 200