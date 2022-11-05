
import psycopg2

def get_conn():
    conn = psycopg2.connect(database="dp", user="ejamnadas", password="N33nte*", host="35.184.12.134", port="5432" )
    return conn