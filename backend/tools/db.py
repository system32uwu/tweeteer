import os
import sqlite3

here = os.path.join(os.path.dirname(__file__)) # ~/mateo/repos/tweeteer/backend/tools
dbPath = f'{here}/../tweeteer.db' # ~/mateo/repos/tweeter/backend/tweeteer.db
schemaPath = f'{here}/tweeteer.sql'

def getDb():
    con = sqlite3.connect(dbPath, check_same_thread=False, detect_types=sqlite3.PARSE_DECLTYPES)
    con.execute('PRAGMA FOREIGN_KEYS=ON')
    con.set_trace_callback(print)
    return con

if __name__ == '__main__':
    if os.path.exists(dbPath):
        os.remove(dbPath)

    schema = open(schemaPath, 'r').read()

    getDb().cursor().executescript(schema)