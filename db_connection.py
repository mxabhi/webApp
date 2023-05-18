import mysql.connector

DB_NAME = 'coaching_institute'

config = {
  'user': 'root',
  'password': 'abhi',
  'host': '127.0.0.1',
  'database': DB_NAME,
  'raise_on_warnings': True,
}

def connect_to_database():
    conn = mysql.connector.connect(**config)
    return conn

