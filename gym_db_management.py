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

def display_all_workouts():
    try:
        query = "SELECT * FROM workout_sessions"
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

    except ValueError:
        print("Invalid Input. Try again.")
    
    finally:
        curser.close()
        connect_db.close()

def add_workout_session():
    '''Ads a workout session to Workout Session Table.'''
    try:
        member_id = int(input("Enter Member ID: "))
        date = input("Enter Session Date: ")
        duration_minutes = int(input("Enter Session Duration in Minutes: "))
        calories_burned = int(input("Enter Calories Burned: "))
        workout_session = (member_id, date, duration_minutes, calories_burned)

        query = "INSERT INTO workout_sessions(member_id, session_date, session_duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"

        curser.execute(query, workout_session)
        connect_db.commit()
        print(f"{workout_session}, has been added successfully.")

    except ValueError:
        print("Invalid Input. Try again.")

    finally:
        curser.close()
        connect_db.close()

def update_age():
    '''Updates the age of given member.'''
    try:
        name = input("Enter Full Name: ")
        query = "SELECT name FROM members WHERE name = %s"
        curser.execute(query, (name,))

        if curser.fetchone():
            new_age = int(input("Enter Correct Age: "))
            query_2 = "UPDATE members SET age = %s WHERE name = %s"
            curser.execute(query_2, (new_age, name))
            connect_db.commit()
            print(f"The age for {name}, has been updated successfully.")
        else:
            print("This person is not in the database.")
    
    except Exception as e:
        print("Error:", e)

    finally:
        curser.close()
        connect_db.close()

def delete_workout_session():
    '''Deletes a workout session from the Workout Session Table.'''
    try:
        name = input("Enter Full Name: ")
        query = "SELECT member_id FROM members WHERE name = %s"
        curser.execute(query, (name,))
        member = curser.fetchone()

        if member:
            member_id = member[0]
            query2 = "DELETE FROM workout_sessions WHERE member_id = %s"
            curser.execute(query2, (member_id,))
            connect_db.commit()
            print(f"Workout session has been deleted successfully.")
        else:
            print("No workout sessions exist for this member.")

    except Exception as e:
        print("Error:", e)

    finally:
        curser.close()
        connect_db.close()

# update_age()
# display_all_members()
# display_all_workouts()
# add_member()
# delete_workout_session()