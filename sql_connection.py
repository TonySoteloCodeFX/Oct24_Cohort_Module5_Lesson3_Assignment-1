import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = 'fitness_center_db'
    user = 'root'
    password = "Isaiah3117"
    host = '127.0.0.1'

    try:
        # connecting to database 
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        print("Connected to Fitness Center Database successfully.")
        return conn
    
    except Error as e:
        # handle any connection errors 
        print(f"Error: {e}")
        return None