from .shared import db
from datetime import datetime, timedelta
from config import Config
import jwt
from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    email: str
    password: str
    photoUrl: str = None
    
    posts: list = None
    
    def __init__(self, id:int,username:str, email:str, password:str, photoUrl:str=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.photoUrl = photoUrl
        self.getPosts()

    @classmethod
    def getById(cls, id:int) -> 'User':
        statement = """
        SELECT * FROM user 
        WHERE id = ?
        """

        result = db.execute(statement, [id]).fetchone()

        return cls(*result)
    
    @classmethod
    def getByUsername(cls, username:str) -> 'User':
        statement = """
        SELECT * FROM user 
        WHERE username = ?
        """

        result = db.execute(statement, [username]).fetchone()
        
        return cls(*result)

    @classmethod
    def save(cls, username:str, email:str, password:str) -> 'User':
        statement = """
        INSERT INTO user (username, email, password)
        VALUES (?,?,?)
        """

        cursor = db.cursor()

        cursor.execute(statement, [username, email, password])

        db.commit()

        id = cursor.lastrowid

        return cls(id, username, email, password)

    @classmethod
    def deleteById(cls, id:int) -> int:
        statement = """
        DELETE FROM user
        WHERE id = ?
        """

        cursor = db.cursor()

        cursor.execute(statement, [id])

        db.commit()

        return cursor.rowcount

    @classmethod
    def updateById(cls, id:int, username:str, email:str, password:str) -> int:
        statement = """
        UPDATE user
        SET username = ?, email = ?, password = ?
        WHERE id = ?
        """

        cursor = db.cursor()

        cursor.execute(statement, [username, email, password, id])

        db.commit()

        return cursor.rowcount

    @classmethod
    def login(cls, email:str, password:str):
        statement = """
        SELECT * FROM user 
        WHERE 
        email = ? AND password = ?
        """

        result = db.execute(statement, [email, password]).fetchone()
        
        if result is None:
            return None, None
        else:
            user = cls(*result)

            now = datetime.utcnow()

            payload = {
                'iat': now,
                'exp': now + timedelta(days=7),
                'sub': user.id
            }

            token = jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")

            return user, token

    @classmethod
    def verifyToken(cls, token:str) -> int: # return the id of the user
        payload = jwt.decode(token,Config.SECRET_KEY, algorithms=["HS256"])
        return payload['sub']

    def getPosts(self):
        statement = """
        SELECT id FROM post 
        WHERE idUser = ?
        """

        result = db.execute(statement, [self.id]).fetchall()
        
        self.posts = [r[0] for r in result]

        return self.posts

# example of sql injection vulnerable code:
# @classmethod
#     def login(cls, email:str, password:str):

#         statement = f"""
#         SELECT * FROM user 
#         WHERE 
#         email = '{email}' AND password = '{password}'
#         """