# *******************************************************
# Name: [Nagadeepthi kothapalli]
# Date Created: [09-01-2024]
# Description: This program processes user input for a name and Fahrenheit temperature,
# performs string manipulations and temperature conversion, and outputs the results.
# *******************************************************

# Import necessary modules
import datetime # Import the datetime module to work with dates
import getpass # Import the getpass module to retrieve the current system usernameNagadeepthi kothapalli

# Input Section
while True: # Start an infinite loop to handle input validation
    try:
        # Get user input
        name = input("Please enter your name: ")  # Prompt user to input their name
        
        # Ensure input is valid
        if not name: # Check if the input is empty
            raise ValueError("Name cannot be empty.")  # Raise an error if the name is empty
        
        fahrenheit = input("Please enter the temperature in Fahrenheit: ")
        fahrenheit = float(fahrenheit)  # Attempt to convert to float

 # If input is valid, break out of the loop
        break
    
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.") # Print the error message and prompt the user to try again

# Process Section
# Name processing
name_upper = name.upper()  # Convert the name to uppercase
name_lower = name.lower() # Convert the name to lowercase
name_title = name.title() # Convert the name to title case (first letter of each word capitalized)
name_len = len(name) # Calculate the length of the name

# We are creating a message using F-string formatting
name_message_with_fstring = f"Hello {name_title}, your name is {name_len} characters long!"
# we are creating a message by using string concatenation
name_message_with_concatenation = "Hello " + name_title + ", your name is " + str(name_len) + " characters long!"

name_ten_times = name * 10 # Its repeating the name ten times

# Fahrenheit processing
celsius_int = int((fahrenheit - 32) * 5 / 9) # Convert Fahrenheit to Celsius and convert the result to an integer
celsius_float = (fahrenheit - 32) * 5 / 9 # Convert Fahrenheit to Celsius and keep the result as a float

# Output Section
# Get username and today's date
username = getpass.getuser()  
today_date = datetime.date.today()

print(f"Username: {username}") # Print the system username
print(f"Today's Date: {today_date}") # Print today's date
print(f"Name entered by user: {name}") # Print the user's name
print(f"Type of variable that name is: {type(name)}") # Print the data type of the name variable
print(f"Name in uppercase: {name_upper}") # Print the name in uppercase
print(f"Name in lowercase: {name_lower}") # Print the name in lowercase
print(f"Name in title case: {name_title}") # Print the name in title case
print(f"Length of the name: {name_len}")  # Print the length of the name
print(f"Message with f-string: {name_message_with_fstring}") # Print the message created with f-string
print(f"Message with concatenation: {name_message_with_concatenation}") # Print the message created with concatenation
print(f"Celsius float value: {celsius_float} (Type: {type(celsius_float)})") # Print the temperature in Celsius as a float and its type
print(f"Celsius integer value: {celsius_int} (Type: {type(celsius_int)})") # Print the temperature in Celsius as an integer and its type