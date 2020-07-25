import requests
import sqlite3
import webbrowser

def convertTuple(tup): 
    alist = list(tup)
    return alist


def post_user_function(first_name, last_name):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    try:
        sql = ("INSERT INTO users (first_name,last_name) VALUES (?, ?)")
        c.execute(sql,(first_name, last_name))
        conn.commit() 

    finally:
        conn.close()


def get_user(first_name):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    f = open('success.html', 'w')

    try:
        c.execute("SELECT * FROM users WHERE first_name=?", (first_name,))
        rows = c.fetchall()
        if rows is not None:
            for row in rows:         
                print(row)
                r = convertTuple(row)
                for x in range(len(r)):
                    f.write(r[x])
                    f.write(" ")
        
      

    finally:
        conn.close()
        f.close()


    return '/success.html'


