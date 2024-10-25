import csv
file_path = 'employee_data.csv'  # Path to the employee data CSV file

# Name : Nagadeepthi kothapalli
# Date : 09-29-24
# Program Description :Python program is designed to perform several tasks related to employee management, data analysis, and visualization. 
#Employee Data Processing:The program reads employee data from a CSV file (employee_data.csv) and stores it in a list of dictionaries. Each employee record contains details like the first name, last name, year of birth, password length, special character preferences, use of numbers, age, and city.
# Function to plot employee hours
#Username and Password Generation:For each employee, the program generates a unique username and a password based on their details:
def show_employee_hours_plot(employees, hours_high, hours_low, graph_title, graph_x_label, graph_y_label):
    import matplotlib.pyplot as plt  # Import plotting library
    import seaborn as sns  # Import Seaborn for better plotting aesthetics
    graph_title = ""  # Initialize empty graph title (reset later)
    sns.set_style('whitegrid')  # Set plot style to a white grid
    fig, ax = plt.subplots()  # Create figure and axis for plotting
    ax.plot(employees, hours_high, c='red')  # Plot high hours in red
    ax.plot(employees, hours_low, c='blue')  # Plot low hours in blue
    ax.fill_between(employees, hours_high, hours_low, facecolor='blue', alpha=0.1)  # Fill between high and low hours with blue color
    # Format the plot
    ax.set_title(graph_title, fontsize=16)  # Set title font size
    ax.set_ylabel(graph_y_label, fontsize=12)  # Set Y-axis label font size
    ax.set_xlabel(graph_x_label, fontsize=12)  # Set X-axis label font size
    ax.tick_params(axis='both', labelsize=12)  # Set tick parameters for both axes
    plt.show(block=True)  # Display the plot

# Function to read employee data from a CSV file
def read_employee_data(file_path):
    employee_list = []  # Initialize an empty list to store employee data
    with open(file_path, 'r') as file:  # Open the CSV file for reading
        csv_reader = csv.reader(file)  # Create a CSV reader object
        next(csv_reader)  # Skip the header row
        for row in csv_reader:  # Loop through each row in the file
            employee_list.append(tuple(row))  # Append each row as a tuple to the employee list
    return employee_list  # Return the list of employee data

# Function to create a list of dictionaries from employee data
def create_employee_dictionary(employee_list):
    employee_dict_list = []  # Initialize an empty list of employee dictionaries
    for employee in employee_list:  # Loop through each employee record
        employee_dict = {  # Create a dictionary for each employee
            'first_name': employee[0],
            'last_name': employee[1],
            'year_born': employee[2],
            'pw_length': employee[3],
            'use_special_characters': employee[4],
            'use_numbers': employee[5],
            'age': employee[6],
            'city': employee[7]
        }
        employee_dict_list.append(employee_dict)  # Add employee dictionary to list
    return employee_dict_list  # Return the list of employee dictionaries

# Function to generate a password based on parameters
def build_password(password_length, use_special_characters, use_numbers):
    import random  # Import random library for password generation
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"  # Define the alphabet
    SPECIAL_CHARACTERS = "!@#$%^&*()_+-=:;'<>,.?/"  # Define special characters
    NUMBERS = "0123456789"  # Define numbers
    count = 0  # Initialize a counter
    password = ""  # Initialize an empty password
    while count < int(password_length):  # Loop until the password reaches the desired length
        random_number = random.randrange(0, 52, 1)  # Get a random alphabet character index
        pwChar = ALPHABET[random_number]  # Get the character from the alphabet
        password += pwChar  # Add the character to the password
        count += 1
        pwChar = ""
        if use_special_characters and count < int(password_length):  # Add special character if required
            random_number = random.randrange(0, 22, 1)
            pwChar = SPECIAL_CHARACTERS[random_number]
            password += pwChar
            count += 1
            pwChar = ""
        if use_numbers and count < int(password_length):  # Add numbers if required
            random_number = random.randrange(0, 10, 1)
            pwChar = NUMBERS[random_number]
            password += pwChar
            count += 1
            pwChar = ""
    return password  # Return the generated password

# Function to build a username
def build_username(first_name, last_name, year_born):
    username = ""  # Initialize an empty username
    dup_check_list = []  # List to check for duplicate usernames
    if not hasattr(build_username, 'dup_check_list'):  # If no duplicate list exists, create one
        build_username.dup_check_list = []
    username = first_name[0].lower() + last_name.lower() + year_born[-2:]  # Build username from first letter of first name, last name, and year
    count = 1
    while username in build_username.dup_check_list:  # Check if username is a duplicate
        username = first_name.lower() + last_name[0].lower() + year_born[-2:]  # If duplicate, adjust username
        count += 1
    build_username.dup_check_list.append(username)  # Add the username to the duplicate list
    return username  # Return the created username

# Function to generate employee credentials (username and password)
def create_employee_credentials(employee_dict_list):
    updated_employee_dict_list = []  # List to store updated employee data with credentials
    employee_data_dictionary = {}  # Dictionary to store employee data mapped to username
    for employee in employee_dict_list:  # Loop through each employee dictionary
        employee_data = list(employee)  # Convert employee dictionary to list
        first_name = employee_data[0]  # Extract employee first name
        last_name = employee_data[1]  # Extract employee last name
        year_born = employee_data[2]  # Extract employee year of birth
        pw_length = employee_data[3]  # Extract password length
        use_special_characters = employee_data[4]  # Extract special character flag
        use_numbers = employee_data[5]  # Extract number usage flag
        username = build_username(first_name, last_name, year_born)  # Build username
        password = build_password(pw_length, use_special_characters, use_numbers)  # Build password
        employee_data.append(username)  # Append username to employee data
        employee_data.append(password)  # Append password to employee data
        updated_employee_dict_list.append(employee)  # Add updated employee data to list
        employee_data_dictionary[username] = employee_data  # Add employee data to dictionary using username as key
    return updated_employee_dict_list, employee_data_dictionary  # Return the updated employee list and dictionary

# Function to read hours worked data from CSV file
def get_hours_worked_csv_data():
    hours_worked = 'hours_worked.csv'  # Define the file name
    try:
        with open(hours_worked, newline='') as csvfile:  # Open the hours worked CSV file
            csv_reader = csv.reader(csvfile)  # Create a CSV reader object
            data = [row for row in csv_reader]  # Read and store all data rows
            return data  # Return the data
    except FileNotFoundError:  # Handle the case where the file is not found
        print(f'Sorry the file {hours_worked} does not exist.')

# Function to fetch book information from Google Books API
def get_book_info(query):
    import requests  # Import requests library for HTTP requests
    import json  # Import JSON library to handle API responses

    endpoint = f'https://www.googleapis.com/books/v1/volumes'  # Google Books API endpoint
    params = {"q": query, "maxResults": 1}  # Define query parameters for the API request
    response = requests.get(endpoint, params=params).json()  # Send the request and parse the JSON response
    for book in response["items"]:  # Loop through each book in the API response
        volume = book["volumeInfo"]  # Extract book info
        title = volume["title"]  # Get the book title
        industryIDs = volume["industryIdentifiers"]  # Get industry identifiers (ISBN)
        ISBN_info = industryIDs[0]  # Get first ISBN info
        ISBN_number = ISBN_info["identifier"]  # Extract the ISBN number
        ISBN_type = ISBN_info["type"]  # Extract the type of ISBN
        authors = volume["authors"]  # Extract authors list
        author = authors[0].replace("()", "")  # Clean the author name
        isbn = ISBN_type + ": " + ISBN_number  # Create the full ISBN info

        return title, author, isbn  # Return the title, author, and ISBN info

# Function to write employee data to a CSV file
def write_employee_data_dictionary_to_csv(employee_data_dictionary):
    with open('employee_data_output.csv', 'w', newline='') as csvfile:  # Open file for writing
        fieldnames = ['username', 'first_name', 'last_name', 'year_born', 'pw_length', 'use_special_charaters', 'use_numbers', 'age', 'city', 'average_hours', 'least_hours', 'most_hours']  # Define CSV column headers
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # Create a CSV DictWriter object
        writer.writeheader()  # Write the header row
        for username, employee_data in employee_data_dictionary.items():  # Loop through each employee in the dictionary
            writer.writerow({  # Write employee data row
                'username': username,
                'first_name': employee_data[0],
                'last_name': employee_data[1],
                'year_born': employee_data[2],
                'pw_length': employee_data[3],
                'use_special_charaters': employee_data[4],
                'use_numbers': employee_data[5],
                'age': employee_data[6],
                'city': employee_data[7],
                'average_hours': employee_data[10][0],
                'least_hours': employee_data[10][1],
                'most_hours': employee_data[10][2]
            })

# Main function to execute the program
def main():
    from datetime import date  # Import date library to get current date
    import getpass  # Import getpass to get the username of the person running the script

    work_dates_list = []  # Initialize list to store work dates
    work_hours_high = []  # Initialize list to store high hours worked
    work_hours_low = []  # Initialize list to store low hours worked
    employee_names = []  # Initialize list to store employee names
    graph_x_label = "Employees"  # Set X-axis label for the graph
    graph_y_label = "Hours worked"  # Set Y-axis label for the graph

    # Input: Prompt user to enter a book title for information lookup
    print("Enter a title to a classic book to see details on that book:")
    query = input("What is your favourite classical book? : ")  # Take user input

    # Process: Get hours worked from CSV file and format data
    r_hours = get_hours_worked_csv_data()  # Retrieve hours worked data from CSV
    header_row = r_hours[0]  # Get the header row from the data
    for day in header_row:  # Loop through the header to extract work dates
        if "Week Ending" not in day:  # Ignore columns that mention "Week Ending"
            work_dates_list.append(day)  # Add valid work dates to the list
    graph_title = "Employee Low and High Hours Worked for " + work_dates_list[0] + " to " + work_dates_list[-1]  # Set graph title with work dates
    employee_list = read_employee_data('employee_data.csv')  # Read employee data from the file
    employee_updated_list, employee_data_dictionary = create_employee_credentials(employee_list)  # Create credentials for employees
    for username in employee_data_dictionary.keys():  # Loop through employee usernames
        hours_worked_list = []  # Initialize list for hours worked
        hours_worked_list_converted = []  # List to store converted hours (as float)
        r_hours = get_hours_worked_csv_data()  # Read hours worked data again
        for hours in r_hours:  # Loop through hours worked data
            if hours[0] == username:  # Match the row to the correct employee
                hours_worked_list = list(hours)  # Store hours worked for the employee
                hours_worked_list.pop(0)  # Remove the first element (username)
                for hour in hours_worked_list:  # Loop through each hour worked
                    hours_worked_list_converted.append(float(hour))  # Convert hour to float and add to list
        if len(hours_worked_list):  # Check if hours worked list is non-empty
            avg_hours = sum(hours_worked_list_converted) / len(hours_worked_list_converted)  # Calculate average hours worked
            min_hour = min(hours_worked_list_converted)  # Find the minimum hours worked
            max_hour = max(hours_worked_list_converted)  # Find the maximum hours worked
            work_hours_stats = [avg_hours, min_hour, max_hour]  # Store average, min, and max hours in a list
        employee_data_dictionary[username].append(work_hours_stats)  # Append work hours stats to employee data
    for username, employee_data in employee_data_dictionary.items():  # Loop through employee data to extract details for the plot
        employee_name = employee_data[0] + " " + employee_data[1][0]  # Create employee display name
        work_low = employee_data[10][1]  # Get the lowest hours worked
        work_high = employee_data[10][2]  # Get the highest hours worked
        employee_names.append(employee_name)  # Add employee name to list
        work_hours_low.append(work_low)  # Add lowest hours to list
        work_hours_high.append(work_high)  # Add highest hours to list
    write_employee_data_dictionary_to_csv(employee_data_dictionary)  # Write the updated employee data to CSV
    title, author, isbn = get_book_info(query)  # Get book info based on user query

    # Output: Print various information to the console
    print(getpass.getuser())  # Print the username of the person running the script
    print(date.today())  # Print the current date
    print("------------------------------------------------------------------------------------------------------")
    for username, employee_data in employee_data_dictionary.items():  # Loop through and display employee information
        print(username)
        print(employee_data[0] + " " + employee_data[1] + " was born in " + employee_data[2])
        print("I am " + str(employee_data[6]) + " years old.")
        print("I live in " + employee_data[7])
        print(f'Average hours {str(employee_data[10][0])}')
        print(f'The least hours worked was {str(employee_data[10][1])}')
        print(f'The most hours worked was {str(employee_data[10][2])}')
        print("---------------------------------------------------------------------------------------------")
    print(employee_updated_list)  # Print the list of updated employee data
    print(employee_data_dictionary)  # Print the employee data dictionary
    print('---------------------------------------------------------------------------------------------------')
    print(f'{title} by {author} | {isbn}')  # Print the book title, author, and ISBN
    show_employee_hours_plot(employee_names, work_hours_low, work_hours_high, graph_title, graph_x_label, graph_y_label)  # Display the plot

# Entry point to run the program
if __name__ == '__main__':
    main()  # Call the main function to start the program
