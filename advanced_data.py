from sql_connection import connect_database

connect_db = connect_database()
cursor = connect_db.cursor()


def get_members_in_age_range(start_age, end_age):
    '''Prints all members & details between the ages given.'''
    try:
        query = '''
        SELECT * FROM members
        WHERE age BETWEEN %s and %s;
        '''
        cursor.execute(query, (start_age, end_age))
        columns = cursor.column_names

        print("-" * 50)
        print(f"Members between the ages of {start_age} - {end_age}:\n")

        for row in cursor.fetchall():
            row_data = dict(zip(columns,row))

            for column, value in row_data.items():
                print(f"{column}: {value}")
            print("-" * 50)
    finally:
        cursor.close()
        connect_db.close()

get_members_in_age_range(25, 35)
    
