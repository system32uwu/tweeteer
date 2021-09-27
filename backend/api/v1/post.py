from flask import Blueprint, jsonify, request
from middleware.authGuard import requiresAuth
from models.post import Post
from models.user import User

postRouter = Blueprint('post', __name__, url_prefix='/post')

@postRouter.get('/all')
def getAllPosts():
    return jsonify(Post.all()), 200

@postRouter.get('/<int:id>')
def getPostById(id:int):
    return jsonify(Post.getById(id)), 200

@postRouter.post('/')
@requiresAuth
def savePost(idUser:int):
    print(idUser)
    data = request.get_json()
    return jsonify(Post.save(idUser, data['content'])), 200

@postRouter.delete('/<int:id>')
@requiresAuth
def deletePost(id:int, idUser:int):
    userPosts = User.getById(idUser).getPosts()
    if id in userPosts:
        return jsonify({'affected rows': Post.deleteById(id)}), 200
    else:
        return jsonify({'error': 'you cannot delete this post'}), 403

@postRouter.put('/<int:id>')
@requiresAuth
def updatePost(id:int, idUser:int):
    userPosts = User.getById(idUser).getPosts()
    if id in userPosts:
        data = request.get_json()
        return jsonify({'affected rows': Post.updateById(id, data['content'])}), 200
    else:
        return jsonify({'error': 'you cannot update this post'}), 403

@postRouter.post('/like/<int:id>')
@requiresAuth
def likePost(id:int, idUser:int):
    p = Post.getById(id)
    return jsonify({'likes': p.likePost(idUser)})

@postRouter.post('/comment/<int:id>')
@requiresAuth
def commentPost(id:int, idUser:int):
    data = request.get_json()
    p = Post.getById(id)
    return jsonify(p.commentPost(idUser, data['content'])), 200