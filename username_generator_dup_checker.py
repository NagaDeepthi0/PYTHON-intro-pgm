from datetime import date  # Importing the 'date' module to work with date functions (though it's not used in the current code)
import getpass    # Importing 'getpass' to securely handle user input (such as passwords) (also not used in current code)

#################################################################################################################################################
# Name : Nagadeepthi Kothapalli
# Date : 09-08-24
# Program Description : This program collects user data to create unique usernames for a network based on the user's first name, last name, and year of birth.
#################################################################################################################################################

# Variables section

first_name = " "   # Placeholder variable for storing the first name, initialized to a blank string
last_name = " "    # Placeholder variable for storing the last name, initialized to a blank string
year_born = " "    # Placeholder variable for storing the year of birth, initialized to a blank string
is_this_correct = " "  # Placeholder to confirm if the entered user details are correct
username_list = []  # An empty list to store the generated usernames
username_sorted_list = []  # An empty list to store the sorted version of `username_list`
employee_data_dictionary = {}  # A dictionary to store employee data, keyed by their usernames
all_employee_data_tuple_list = []  # A list to store tuples containing all employee data

yes_list = ['yes', 'y', 'yes']  # List of acceptable inputs that represent 'Yes' (case-insensitive)

# Input section

print('Enter the information below to create a username for network')  # Prompting the user to start entering data

# Outer loop continues until we have collected 5 sets of employee data
while len(all_employee_data_tuple_list) < 5:  
    while len(first_name) < 2:  # Ensures first name is at least 2 characters long before accepting
        first_name = input("Enter your first name: ")  # Prompts user to input their first name

    while len(last_name) < 2:  # Ensures last name is at least 2 characters long before accepting
        last_name = input("Enter your last name: ")  # Prompts user to input their last name

    year_born = input("Enter the full year you were born: ")  # Prompts user to input their year of birth
    
    while len(year_born) < 4:  # Ensures the year of birth is 4 characters long
        year_born = input("Enter the full year you were born: ")  # Re-prompts user if the year is incomplete
    
    # Displays the entered details for the user to confirm
    print("You entered " + first_name + " " + last_name + " " + year_born + ". Is this correct?")  
    is_this_correct = input("Yes or No: ")  # Takes confirmation input from the user
    
    if(is_this_correct in yes_list):  # If the input is a 'Yes' or its equivalent
        employee_data = (first_name, last_name, year_born)  # Creates a tuple with employee data
        all_employee_data_tuple_list.append(employee_data)  # Adds this tuple to the employee data list
        
        # Resets the input variables for the next employee
        first_name = " "
        last_name = " "
        year_born = " "
    else:  # If the user says 'No', re-prompt for inputs
        first_name = " "
        last_name = " "
        year_born = " "
        continue  # Restart the loop to enter data again

# Process section

# Looping through each employee's data to generate usernames
for employee in all_employee_data_tuple_list:  
    employee_first_name = employee[0]  # Extracts the first name from the employee tuple
    employee_last_name = employee[1]  # Extracts the last name from the employee tuple
    employee_year_born = employee[2]  # Extracts the year of birth from the employee tuple
    
    first_init = employee_first_name[0].lower()  # Gets the first initial of the first name and converts to lowercase
    last_name = employee_last_name.lower()  # Converts the last name to lowercase
    last_digits_of_year = employee_year_born[2:]  # Extracts the last two digits of the birth year
    
    # Generates a username by concatenating first initial, last name, and last two digits of birth year
    username = first_init + last_name + last_digits_of_year  
    
    if username in username_list:  # Checks if the generated username is already in the list
        # If the username already exists, generate a new one by combining the full first name, first initial of last name, and last two digits of year
        username = employee_first_name.lower() + employee_last_name[0:1].lower() + last_digits_of_year  
        username_list.append(username)  # Adds the new unique username to the list
    else:  
        username_list.append(username)  # Adds the username to the list if it's not already there
    
    employee_data_dictionary[username] = employee  # Adds the employee data to the dictionary with the username as key
    
    username_sorted_list = username_list.sort()  # Sorts the list of usernames in-place

# Output section

# Prints the list of all employee data tuples
print(all_employee_data_tuple_list)  
# Prints the dictionary containing usernames and corresponding employee data
print(employee_data_dictionary)  
# Prints the list of generated usernames
print(username_list)  
# Prints the sorted list of usernames (though `sort()` doesn't return anything, so it will print None)
print(username_sorted_list)  
