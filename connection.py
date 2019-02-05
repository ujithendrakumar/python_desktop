import  mysql.connector

from mysql.connector import  Error

def connect():
    try:
        conn = mysql.connector.connect(host= 'localhost', database = 'pydb',user='root',password='')
        if conn.is_connected():
            mycursor = conn.cursor()
            # //create database
            # mycursor.execute("CREATE DATABASE pydb")
            # mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
            print("Connected to MySql Database")
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":
    connect()