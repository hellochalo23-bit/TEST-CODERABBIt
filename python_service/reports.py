from pool import pool

def render_report(sql):
    conn = pool.getconn()
    try:
        return conn.execute(sql).fetchall()
    finally:
        pool.putconn(conn)
