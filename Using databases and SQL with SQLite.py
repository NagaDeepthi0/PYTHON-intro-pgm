# Flowerbox section
###################################################################################################################################################

#  Name :Nagadeepthi Kothapalli
#  Date : 10/06/2024
#  Program Description :This code is designed to read employee and work hour data from CSV files, insert the data into an SQLite database, and generate summary statistics about employee work hours. The script is divided into several functional components for reading, processing, and querying the data. 
##################################################################################################################################################

import sqlite3
import csv

# Function to read employee data from CSV and return as list of tuples
def read_employee_data(file_name):
    with open(file_name, newline='') as file:  # Open the CSV file
        reader = csv.reader(file)  # Create a CSV reader object
        next(reader)  # Skip the header row
        employee_data = [tuple(row) for row in reader]  # Convert rows into tuples and store them in a list
    return employee_data  # Return the list of tuples

# Function to create employee dictionary for easier manipulation
def create_employee_dictionary(employee_data):
    employee_dict = []  # Initialize an empty list to store dictionaries
    for emp in employee_data:  # Iterate over each employee tuple
        employee_dict.append({  # Convert each tuple to a dictionary
            'username': emp[0],
            'first_name': emp[1],
            'last_name': emp[2],
            'year_born': emp[3],
            'pw_length': emp[4],
            'use_special_characters': emp[5],
            'use_numbers': emp[6],
            'age': emp[7],
            'city': emp[8],
            'average_hours': emp[9],
            'least_hours': emp[10],
            'most_hours': emp[11]
        })
    return employee_dict  # Return the list of employee dictionaries

# Function to create SQLite database and tables
def create_database(db_file):
    conn = sqlite3.connect(db_file)  # Connect to the SQLite database (or create it if it doesn't exist)
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands
    
    # Create the employee_data table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee_data (
        username TEXT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        year_born INTEGER,
        pw_length INTEGER,
        use_special_characters TEXT,
        use_numbers TEXT,
        age INTEGER,
        city TEXT,
        average_hours REAL,
        least_hours REAL,
        most_hours REAL
    )
    ''')

    # Create the hours_worked table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hours_worked (
        username TEXT,
        week TEXT,
        hours_worked REAL,
        FOREIGN KEY(username) REFERENCES employee_data(username)
    )
    ''')

    conn.commit()  # Save the changes
    return conn  # Return the connection object for further use

# Function to insert employee data into the database
def insert_employee_data(conn, employee_data):
    cursor = conn.cursor()  # Create a cursor object
    
    for emp in employee_data:  # Iterate over each employee tuple
        cursor.execute('''  
        INSERT OR IGNORE INTO employee_data (
            username, first_name, last_name, year_born, pw_length,
            use_special_characters, use_numbers, age, city, average_hours,
            least_hours, most_hours
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', emp)
    
    conn.commit()  # Save the changes

# Function to insert hours worked data into the database
def insert_hours_worked(conn, file_name):
    cursor = conn.cursor()  # Create a cursor object

    with open(file_name, newline='') as file:  # Open the CSV file for hours worked
        reader = csv.reader(file)  # Create a CSV reader object
        next(reader)  # Skip the header row
        for row in reader:  # Iterate over each row in the file
            username = row[0]  # Username is the first column
            weekly_data = row[1:]  # Remaining columns are hours worked for each week

            for i, hours in enumerate(weekly_data, start=1):  # Iterate over weekly hours data
                week_label = f"Week_{i}"  # Create a week label like Week_1, Week_2, etc.
                try:
                    hours_float = float(hours) if hours else 0.0  # Convert hours to float, defaulting to 0.0 if empty
                except ValueError:
                    hours_float = 0.0  # Set to 0.0 if conversion fails
                
                # Insert the hours worked for the corresponding week
                cursor.execute('''
                INSERT INTO hours_worked (username, week, hours_worked)
                VALUES (?, ?, ?)
                ''', (username, week_label, hours_float))

    conn.commit()  # Save the changes

# Function to execute SQL queries and retrieve summary statistics
def execute_queries(conn):
    cursor = conn.cursor()  # Create a cursor object
    
    # Query: Total hours worked by each employee
    cursor.execute('''
    SELECT e.username, e.first_name, e.last_name, SUM(h.hours_worked)
    FROM employee_data e
    JOIN hours_worked h ON e.username = h.username
    GROUP BY e.username
    ''')
    total_hours = cursor.fetchall()  # Fetch all results
    
    # Query: Average hours worked per week by each employee
    cursor.execute('''
    SELECT e.username, e.first_name, e.last_name, AVG(h.hours_worked)
    FROM employee_data e
    JOIN hours_worked h ON e.username = h.username
    GROUP BY e.username
    ''')
    avg_hours = cursor.fetchall()  # Fetch all results
    
    # Query: Employee with the maximum total hours worked
    cursor.execute('''
    SELECT e.username, e.first_name, e.last_name, SUM(h.hours_worked)
    FROM employee_data e
    JOIN hours_worked h ON e.username = h.username
    GROUP BY e.username
    ORDER BY SUM(h.hours_worked) DESC
    LIMIT 1
    ''')
    max_hours = cursor.fetchone()  # Fetch the result with the highest total hours
    
    # Query: Employee with the minimum total hours worked
    cursor.execute('''
    SELECT e.username, e.first_name, e.last_name, SUM(h.hours_worked)
    FROM employee_data e
    JOIN hours_worked h ON e.username = h.username
    GROUP BY e.username
    ORDER BY SUM(h.hours_worked) ASC
    LIMIT 1
    ''')
    min_hours = cursor.fetchone()  # Fetch the result with the lowest total hours
    
    return total_hours, avg_hours, max_hours, min_hours  # Return all query results

# Function to print the results of the queries in the desired format
def print_results(total_hours, avg_hours, max_hours, min_hours):
    print("Total hours worked by each employee:")  # Print header
    for row in total_hours:  # Print each row of total hours
        print(row)
    
    print("\nAverage hours worked per week by each employee:")  # Print header
    for row in avg_hours:  # Print each row of average hours
        print(row)
    
    print("\nEmployee with the maximum total hours worked:")  # Print header
    print(max_hours)  # Print employee with the max hours
    
    print("\nEmployee with the minimum total hours worked:")  # Print header
    print(min_hours)  # Print employee with the min hours

# Main function to orchestrate the program
def main():
    # Input, process, output model
    
    # Input section
    employee_data_file = 'employee_data_output.csv'  # CSV file containing employee data
    hours_worked_file = 'hours_worked.csv'  # CSV file containing hours worked data
    db_file = 'employee_data.db'  # SQLite database file
    
    # Process section
    employee_data = read_employee_data(employee_data_file)  # Read employee data from CSV
    employee_dict = create_employee_dictionary(employee_data)  # Convert employee data to a dictionary format
    
    # Create database and tables
    conn = create_database(db_file)  # Create or connect to the SQLite database
    
    # Insert data into tables
    insert_employee_data(conn, employee_data)  # Insert employee data into database
    insert_hours_worked(conn, hours_worked_file)  # Insert hours worked data into database
    
    # Execute queries to generate summary statistics
    total_hours, avg_hours, max_hours, min_hours = execute_queries(conn)
    
    # Output section
    print_results(total_hours, avg_hours, max_hours, min_hours)  # Print query results

# This line is required to call the main function
if __name__ == "__main__":  # Ensure the script runs only if executed directly
    main()  # Call the main function
