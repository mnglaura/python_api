import requests
import sqlite3




def post_user_function(first_name, last_name):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    try:
        sql = ("INSERT INTO users (first_name,last_name) VALUES (?, ?)")
        c.execute(sql,(first_name, last_name))
        conn.commit() 

    finally:
        conn.close()




