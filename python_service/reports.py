from pool import pool

def render_report(sql):
    conn = pool.getconn()
    rows = conn.execute(sql).fetchall()
    pool.putconn(conn)
    return rows
