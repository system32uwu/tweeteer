class Config(object):
    DEBUG = True
    ENV= 'development'
    TESTING = False
    SESSION_COOKIE_SAMESITE = 'Strict'
    JSON_SORT_KEYS = False
    SECRET_KEY = 'tweeteer-secret' # used to sign and verify jwt tokens
    DATABASE = 'meedikal.db'
    UPLOAD_FOLDER = 'images/'