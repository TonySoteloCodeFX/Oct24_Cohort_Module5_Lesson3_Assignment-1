<h1>Module 5 Lesson 3: Assignments | Applying SQL in Python</h1>
<hr>

<h2><u>1. Gym Database Management with Python and SQL</u></h2>
<br>

<b><i>Objective:</i></b> The aim of this assignment is to reinforce your understanding of Python's interaction with SQL databases, focusing on CRUD (Create, Read, Update, Delete) operations in the context of a gym's membership and workout session management system. You will work with two tables: 'Members' and 'WorkoutSessions'.

<b><i>Problem Statement:</i></b> You are tasked with developing a Python application to manage a gym's database. The database consists of 'Members' and 'WorkoutSessions' tables. Your role is to implement various functions to add, retrieve, update, and delete records in these tables, ensuring data integrity and efficient data handling.

<h5><u>Task 1: Add a Member</u></h5>

<li>Write a Python function to add a new member to the 'Members' table in the gym's database.</li>

```
    # Example code structure
    def add_member(id, name, age):
        # SQL query to add a new member
        # Error handling for duplicate IDs or other constraints
```

<b><i>Expected Outcome:</i></b> A Python function that successfully adds a new member to the 'Members' table in the gym's database. The function should handle errors gracefully, such as duplicate member IDs or violations of other constraints.

<h5><u>Task 2: Add a Workout Session</u></h5>

<li>Develop a Python function to add a new workout session to the 'WorkoutSessions' table for a specific member.</li>

```
    # Example code structure
    def add_workout_session(member_id, date, duration_minutes, calories_burned):
        # SQL query to add a new workout session
        # Error handling for invalid member ID or other constraints
```

<b><i>Expected Outcome:</i></b> A Python function that adds a new workout session to the 'WorkoutSessions' table in the gym's database for a specific member. The function should handle errors gracefully, such as invalid member IDs or violations of other constraints.

<h5><u>Task 3: Updating Member Information</u></h5>

<li>Implement a function to update the age of a member. Ensure that your function checks if the member exists before attempting the update.</li>

```
    # Example code structure
    def update_member_age(member_id, new_age):
        # SQL query to update age
        # Check if member exists
        # Error handling
```

<b><i>Expected Outcome:</i></b> A Python function that updates the age of a member and handles cases where the member does not exist.

<h5><u>Task 4: Delete a Workout Session</u></h5>

<li>Create a Python function to delete a workout session based on its session ID. Include error handling for cases where the session ID does not exist.</li>

```
    # Example code structure
    def delete_workout_session(session_id):
        # SQL query to delete a session
        # Error handling for non-existent session ID
```

<b><i>Expected Outcome:</i></b> A Python function that can delete a workout session using its session ID, with proper error handling for invalid IDs.

<b>Submission Guidelines:</b>

<li>Submit a Python script (.py file) containing all the functions for the tasks.</li>
<li>Include comments in your code to explain your logic and SQL queries.</li>
<li>Ensure your script handles errors gracefully and provides meaningful output.</li>
<hr>

<h2><u>2. Advanced Data Analysis in Gym Management System</u></h2>
<br>

<b><i>Objective:</i></b> The goal of this assignment is to advance your SQL querying skills within Python, focusing on specific SQL functions and clauses like BETWEEN. You will be working with the same gym database as in the previous assignment, comprising the Members and WorkoutSessions tables.

<b><i>Problem Statement:</i></b> As a part of the gym's management team, you need to conduct an in-depth analysis of the membership data. Your task is to develop Python functions that execute advanced SQL queries for distinct department identification, employee count in each department, and age-based employee filtering.

<h5><u>Task 1: SQL BETWEEN Usage</u></h5>

<li><b><i>Problem Statement:</i></b> Retrieve the details of members whose ages fall between 25 and 30.</li>

<li><b><i>Expected Outcome:</i></b> A list of members (including their names, ages, etc) who are between the ages of 25 and 30.</li>

<li><b><i>Example Code Structure:</i></b></li>

```
    def get_members_in_age_range(start_age, end_age):
        # SQL query using BETWEEN
        # Execute and fetch results
```

<b><i>Note:</i></b> The database structure used for this assignment is the same as the previous one, consisting of the Members and WorkoutSessions tables.

<b><i>Submission Guidelines:</i></b>

<li>Submit a Python script (.py file) containing the functions for the specified tasks.</li>

<li>Ensure your code is well-commented to explain the logic and SQL queries used.</li>

<li>Make sure your script includes error handling and provides clear output for each task.</li>
<br>

<b><i>NOTE:</i></b> Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs. If there are classes/objects, make sure they are instantiated and the methods are called.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.