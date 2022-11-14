import variables as v
import psycopg2

def get_conn():
    conn = psycopg2.connect(database="dp", user=v.pgUser, password=v.pgWp, host=v.pgHost, port=v.pgPort )
    return conn