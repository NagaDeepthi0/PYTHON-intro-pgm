#import section
from datetime import date
import getpass

#flower box section
###################################
#   Name: Nagadeepthi Kothapalli                        
#   Date: 09/01/2024 
#   Program Description: This program shows us it generates usernames for employees based on their first name, 
#   last name, and year of birth. It stores employee data in a dictionary and provides sorted unique usernames.
###################################

#Variables section
username_list = [] # List is to store the generated usernames
username_sorted_list = [] # List is to store the sorted and unique names
employee_data_dictionary = {} # We use dictionary to store employee data with username as key

#input section
firstname_list = ["Deepthi","Devya","Sunny","Allen","Rishi"] # List of the employee first names are noted
lastname_list = ["Katty","Katty","Roy","Shaik","Reddy"] # List of the employee last names are noted
year_born_list = ["1999","1999","1997","1998","1996"] # List of the employee birth years are noted

#process section
#Providing step-by-step comments on how the program processes the data to generate usernames
all_employee_data_tuple_list = list(zip(firstname_list,lastname_list,year_born_list))
# Here we combine all the listed employee first names, last names and birth years in to tuples

for employee in all_employee_data_tuple_list:
    employee_first_name = employee[0] # Here we are extracting the employee first name
    employee_last_name = employee[1] # Here we are extracting the employee Last name
    employee_year_born = employee[2] ## Here we are extracting the employee birth years

# Here we are generating username using the employee first name, last name and birth years
first_init = employee_first_name[0].lower() # here we get the first initial of the first name and convert it into lowercase
last_name = employee_last_name.lower() # converting last name into lower case
last_digits_of_year = employee_year_born[-2:] # we get last two digits of the birth years

username = first_init+last_name+last_digits_of_year # Concatenate all together here to form the username
username_list.append(username) # Use the generated username and add it the username list
employee_data_dictionary[username] = employee # Store the employee's data in the dictionary with the username as key

# We are set here to remove duplicate usernames and convert it to a list

username_test_set = set(username_list) # Remove duplicates by converting the list of usernames to a set
username_no_dups = list(username_test_set) # Convert the set back to the list

# Here we are sorting the unique usernames

for username in username_no_dups:
    username_sorted_list.append(username) # Each username is added to the sorted list

username_sorted_list.sort() # sort all the usernames alphabetically

#output section

print(date.today()) # Print the current date
print(getpass.getuser()) # Print the current system username
print(all_employee_data_tuple_list) # Print the list of all employee data tuples
print(username_list) # Print the list of generated usernames (including duplicates)
print(username_test_set) # Print the set of unique usernames
print(username_no_dups) # Print the list of unique usernames
print(employee_data_dictionary) # Print the dictionary of employee data keyed by username
print(username_sorted_list) # Print the sorted list of unique usernames