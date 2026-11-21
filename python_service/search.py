import atexit
import sqlite3

db = sqlite3.connect(":memory:")
atexit.register(db.close)
db.execute("CREATE TABLE users(username TEXT)")
db.executemany("INSERT INTO users VALUES (?)", [("alice",), ("bob",)])

def find_user(username):
    return db.execute(f"SELECT username FROM users WHERE username = '{username}'").fetchall()
