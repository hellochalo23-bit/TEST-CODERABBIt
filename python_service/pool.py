"""A bounded one-connection pool backed by actual in-memory SQLite."""
import atexit
import queue
import sqlite3

class Pool:
    def __init__(self):
        self.available = queue.SimpleQueue()
        self.connection = sqlite3.connect(":memory:")
        self.available.put(self.connection)
        atexit.register(self.connection.close)

    def getconn(self):
        try:
            return self.available.get_nowait()
        except queue.Empty as error:
            raise RuntimeError("POOL_EXHAUSTED after failed report") from error

    def putconn(self, connection):
        self.available.put(connection)

pool = Pool()
