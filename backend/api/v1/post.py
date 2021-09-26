from flask import Blueprint, jsonify, request
from models.post import Post

postRouter = Blueprint('post', __name__, url_prefix='/post')

@postRouter.get('/all')
def getAllPosts():
    return jsonify(Post.all()), 200

@postRouter.get('/<int:id>')
def getPostById(id:int):
    return jsonify(Post.getById(id)), 200

@postRouter.post('/')
def savePost():
    data = request.get_json()
    return jsonify(Post.save(data['idUser'], data['content'])), 200

@postRouter.delete('/<int:id>')
def deletePost(id:int):
    return jsonify({'affected rows': Post.deleteById(id)}), 200

@postRouter.put('/<int:id>')
def updatePost(id:int):
    data = request.get_json()
    return jsonify({'affected rows': Post.updateById(id, data['content'])}), 200

@postRouter.post('/like/<int:id>/<int:idUser>')
def likePost(id:int, idUser:int):
    p = Post.getById(id)
    return jsonify({'likes': p.likePost(idUser)})

@postRouter.post('/comment/<int:id>/<int:idUser>')
def commentPost(id:int, idUser:int):
    data = request.get_json()
    p = Post.getById(id)
    return jsonify(p.commentPost(idUser, data['content']))