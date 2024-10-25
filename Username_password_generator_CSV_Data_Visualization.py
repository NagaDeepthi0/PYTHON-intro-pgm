#flower box section
###################################
#   Name: Nagadeepthi Kothapalli                        
#   Date: 09/23/2024 
#   Program Description: This program automates the management of employee data by reading from a CSV file, generating secure credentials (usernames and passwords) for each employee, and visualizing the distribution of employees across cities using a bar chart.
###################################

import csv  # To handle CSV file operations
import random  # To generate random numbers/characters for passwords

# Function to read employee data from a CSV file and store it as a list of tuples
def read_employee_data(file_path):  
    employee_list = []  # Initialize an empty list to store employee data
    with open(file_path, 'r') as file:  # Open the CSV file in read mode
        reader = csv.reader(file)  # Create a CSV reader object
        next(reader)  # Skip the header row (first row)
        for row in reader:  # Loop through each row in the CSV file
            employee_list.append(tuple(row))  # Append the row as a tuple to the list
    return employee_list  # Return the list of employee tuples

# Function to convert the employee list into a list of dictionaries
def create_employee_dict(employee_list):
    employee_dict_list = []  # Initialize an empty list to store employee dictionaries
    for employee in employee_list:  # Loop through each tuple in the employee list
        employee_dict = {  # Create a dictionary for each employee
            'first_name': employee[0],  # First name from the tuple
            'last_name': employee[1],  # Last name from the tuple
            'year_born': employee[2],  # Year of birth from the tuple
            'pw_length': employee[3],  # Password length from the tuple
            'use_special_characters': employee[4],  # Special character usage from the tuple
            'use_numbers': employee[5],  # Number usage from the tuple
            'age': employee[6],  # Age from the tuple
            'city': employee[7]  # City from the tuple
        }
        employee_dict_list.append(employee_dict)  # Add the dictionary to the list
    return employee_dict_list  # Return the list of employee dictionaries

# Function to build a password based on specified criteria
def build_password(password_length, use_special_characters, use_numbers):
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"  # Letters for password
    SPECIAL_CHARACTERS = "!@#$%^&*()_+-=:;'<>,.?/"  # Special characters for password
    NUMBERS = "0123456789"  # Numbers for password
    count = 0  # Initialize a counter for the password length
    password = ""  # Initialize an empty password string

    # Loop until the desired password length is reached
    while count < password_length:
        random_number = random.randrange(0, 52, 1)  # Generate a random index for ALPHABET
        pwChar = ALPHABET[random_number]  # Get the corresponding character
        password += pwChar  # Add the character to the password
        count += 1  # Increment the counter

        # If special characters are to be used and length is still not reached
        if use_special_characters and count < password_length:
            random_number = random.randrange(0, 22, 1)  # Generate a random index for special characters
            pwChar = SPECIAL_CHARACTERS[random_number]  # Get the corresponding character
            password += pwChar  # Add the character to the password
            count += 1  # Increment the counter

        # If numbers are to be used and length is still not reached
        if use_numbers and count < password_length:
            random_number = random.randrange(0, 10, 1)  # Generate a random index for numbers
            pwChar = NUMBERS[random_number]  # Get the corresponding number
            password += pwChar  # Add the number to the password
            count += 1  # Increment the counter

    return password  # Return the generated password

# Function to build a username based on first name, last name, and year of birth
def build_username(first_name, last_name, year_born):
    username = ""  # Initialize an empty username string
    dup_check_list = []  # Local variable to store duplicate usernames

    # Check if the function has an attribute 'dup_check_list'
    if not hasattr(build_username, 'dup_check_list'):
        build_username.dup_check_list = []  # Initialize as an empty list if not present

    # Create username by taking first letter of first name, last name, and last two digits of birth year
    username = first_name[0].lower() + last_name.lower() + year_born[-2:]

    count = 1  # Initialize a counter for duplicates
    # If the generated username is already in the list, adjust it
    while username in build_username.dup_check_list:
        username = first_name.lower() + last_name[0].lower() + year_born[-2:]  # Adjust username
        count += 1  # Increment counter
        build_username.dup_check_list.append(username)  # Add to the duplicate check list

    return username  # Return the generated username

# Function to create credentials (username and password) for each employee
def create_employee_credentials(employee_dict_list):
    updated_employee_dict_list = []  # List to store updated employee dictionaries
    employee_data_dictionary = {}  # Dictionary to store employee data keyed by username

    # Loop through each employee dictionary in the list
    for employee in employee_dict_list:
        # Generate a username
        username = build_username(employee['first_name'], employee['last_name'], employee['year_born'])
        # Generate a password based on criteria
        password = build_password(int(employee['pw_length']), employee['use_special_characters'], employee['use_numbers'])

        # Add the generated username and password to the employee dictionary
        employee['username'] = username
        employee['password'] = password

        updated_employee_dict_list.append(employee)  # Add updated employee dictionary to the list
        employee_data_dictionary[username] = employee  # Store employee data keyed by username

    return updated_employee_dict_list, employee_data_dictionary  # Return updated list and dictionary

# Function to visualize the employee count per city
def visualize_employee_cities(employee_dict_list):
    import matplotlib.pyplot as plt  # Import matplotlib for plotting
    cities = []  # List to store cities

    # Extract city information from each employee dictionary
    for employee in employee_dict_list:
        for key, value in employee.items():
            if key == 'city':  # If the key is 'city'
                city = value  # Get the city
                cities.append(city)  # Add the city to the list

    city_counts = {}  # Dictionary to store city counts
    for city in cities:  # Loop through the list of cities
        if city in city_counts:
            city_counts[city] += 1  # Increment count if city is already in the dictionary
        else:
            city_counts[city] = 1  # Initialize count if city is not in the dictionary

    # Plot a bar chart for city counts
    plt.bar(city_counts.keys(), city_counts.values())
    plt.xlabel('City')  # X-axis label
    plt.ylabel('Counts')  # Y-axis label
    plt.title('Employee city counts')  # Chart title
    plt.show()  # Display the chart

# Main function to run the program
def main():
    from datetime import date  # Import to get the current date
    import getpass  # Import to get the current system user

    # Path to the employee data file
    file_path = 'employee_data.csv'
    employee_data_dict = {}  # Dictionary to store employee data

    # Step 1: Read employee data from the file
    employee_list = read_employee_data(file_path)

    # Step 2: Convert the list of tuples to a list of dictionaries
    employee_dict_list = create_employee_dict(employee_list)

    # Step 3: Visualize the employee count by city
    visualize_employee_cities(employee_dict_list)

    # Step 4: Generate credentials for each employee
    employee_credentials, employee_data_dictionary = create_employee_credentials(employee_dict_list)

    # Output: Print system user, current date, and employee details
    print(getpass.getuser())  # Print current system user
    print(date.today())  # Print current date

    # Print employee usernames and data
    for user_name, employee_data in employee_data_dictionary.items():
        print(f'Username: {user_name}')
        print(f'Employee data: {employee_data}')
        print("--------------------------------------------------------------")

    # Print all employee credentials
    print(employee_credentials)

# Run the main function when the script is executed
if __name__ == '__main__':
    main()

