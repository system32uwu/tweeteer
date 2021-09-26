from .shared import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Post:
    id: int
    idUser: int
    content: str
    createdAt: datetime
    updatedAt: datetime

    likes: int = 0
    comments: list = None
    user: object = None

    def __init__(self, id:int, idUser:int, content:str, createdAt: datetime, updatedAt: datetime):
        self.id = id
        self.idUser = idUser
        self.content = content
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.getUser()
        self.getComments()
        self.getLikes()

    @classmethod
    def all(cls) -> list['Post']:
        statement = """
        SELECT * FROM post
        """
        
        result = db.execute(statement)

        posts = [cls(*row) for row in result]

        return posts

    @classmethod
    def getById(cls, id:int) -> 'Post':
        statement = """
        SELECT * FROM post
        WHERE id = ?
        """

        result = db.execute(statement, [id]).fetchone()

        return cls(*result)

    @classmethod
    def save(cls, idUser:str, content:str) -> 'Post':
        statement = """
        INSERT INTO post (idUser, content)
        VALUES (?,?)
        """

        cursor = db.cursor()

        cursor.execute(statement, [idUser, content])

        db.commit()

        id = cursor.lastrowid

        return cls.getById(id)

    @classmethod
    def deleteById(cls, id:int) -> int:
        statement = """
        DELETE FROM post
        WHERE id = ?
        """

        cursor = db.cursor()

        cursor.execute(statement, [id])

        db.commit()

        return cursor.rowcount

    @classmethod
    def updateById(cls, id:int, content:str) -> int:
        statement = """
        UPDATE post
        SET content = ?
        WHERE id = ?
        """

        cursor = db.cursor()

        cursor.execute(statement, [content, id])

        db.commit()

        return cursor.rowcount

    def getUser(self):
        from .user import User
        
        statement = """
        SELECT user.* FROM user, post
        WHERE user.id = ?
        """

        result = db.execute(statement, [self.idUser]).fetchone()

        self.user = User(*result)

        return self.user

    def getLikes(self) -> int:
        statement = """
        SELECT COUNT(idPost) FROM likes
        WHERE idPost = ?
        """

        result = db.execute(statement, [self.id]).fetchone()[0]
        self.likes = result

        return self.likes

    def likePost(self, idUser:int) -> int:
        statement = """
        INSERT INTO likes (idUser, idPost)
        VALUES (?,?)
        """

        db.cursor().execute(statement, [idUser, self.id])

        db.commit()

        return self.getLikes()

    def getComments(self) -> list['Comment']:
        statement = """
        SELECT * from comments
        WHERE idPost = ?
        """

        result = db.execute(statement, [self.id]).fetchall()
        self.comments = [Comment(*row) for row in result]

        return self.comments

    def commentPost(self, idUser: int, content: str) -> 'Comment':
        return Comment.save(idUser, self.id, content)

    def updateCommentFromPost(self, id: int, content: str) -> int:
        return Comment.updateById(id, content)

    def deleteCommentFromPostById(self, id: int) -> int:
        return Comment.deleteById(id)

@dataclass
class Comment:
    id: int
    idUser: int
    idPost: int
    content: str

    def __init__(self, id, idUser, idPost, content):
        self.id = id
        self.idUser = idUser
        self.idPost = idPost
        self.content = content

    @classmethod
    def save(cls, idUser:str, idPost:int, content:str) -> 'Comment':
        statement = """
        INSERT INTO comments (idUser, idPost, content)
        VALUES (?,?,?)
        """

        cursor = db.cursor()

        cursor.execute(statement, [idUser, idPost, content])

        db.commit()

        id = cursor.lastrowid

        return cls(id, idUser, idPost, content)

    @classmethod
    def deleteById(cls, id:int) -> int:
        statement = """
        DELETE FROM comments
        WHERE id = ?
        """

        cursor = db.cursor()

        cursor.execute(statement, [id])

        db.commit()

        return cursor.rowcount

    @classmethod
    def updateById(cls, id:int, content:str) -> int:
        statement = """
        UPDATE comments
        SET content = ?
        WHERE id = ?
        """

        cursor = db.cursor()

        cursor.execute(statement, [content, id])

        db.commit()

        return cursor.rowcount