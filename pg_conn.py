
import psycopg2

def get_conn():
    conn = psycopg2.connect(database="dp", user="ejamnadas", password="xxxx*", host="xxxx", port="xxxx" )
    return conn