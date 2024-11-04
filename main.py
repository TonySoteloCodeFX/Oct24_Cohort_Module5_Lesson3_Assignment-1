from sql_connection import connect_database

connect_db = connect_database()
curser = connect_db.cursor()

def display_all_members():
    '''Displays all members from Members Table''' 
    try:
        query = "SELECT * FROM members"
        curser.execute(query)

        for row in curser.fetchall():
            print(row)
    finally:
        curser.close()
        connect_db.close()

def add_member():
    '''Adds a new member to Members Table.'''
    try:
        full_name = input("Enter Full Name: ")
        age = int(input("Enter Age: "))
        new_member = (full_name, age)

        query = "INSERT INTO members(name, age) VALUES (%s, %s)"

        curser.execute(query, new_member)
        connect_db.commit()
        print(f"{new_member}, has been added successfully.")
    
    finally:
        curser.close()
        connect_db.close()

add_member()
