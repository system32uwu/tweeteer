CREATE TABLE user(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  username TEXT UNIQUE NOT NULL,
  email TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  photoUrl TEXT DEFAULT NULL
);

CREATE TABLE follows(
  user1 INTEGER NOT NULL,
  user2 INTEGER NOT NULL,
  
  PRIMARY KEY(user1, user2),
  FOREIGN KEY(user1) REFERENCES user(id),
  FOREIGN KEY(user2) REFERENCES user(id)
);

CREATE TABLE post(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  idUser INTEGER NOT NULL,
  content TEXT NOT NULL,
  createdAt datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
  updatedAt datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
  
  UNIQUE(id, idUser),
  FOREIGN KEY(idUser) REFERENCES user(id)
);

CREATE TABLE likes(
  idUser INTEGER NOT NULL,
  idPost INTEGER NOT NULL,
  
  PRIMARY KEY(idUser, idPost)
);

CREATE TABLE comments(
  id INTEGER NOT NULL,
  idUser INTEGER NOT NULL,
  idPost INTEGER NOT NULL,
  content TEXT NOT NULL,
  PRIMARY KEY(id, idUser, idPost)
);

CREATE TRIGGER updatePostupdatedAt_Trigger
AFTER UPDATE On post
WHEN old.content <> new.content
BEGIN
   UPDATE post SET updatedAt = CURRENT_TIMESTAMP WHERE post.id = old.id;
END;