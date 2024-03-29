# *** Task 1 ***

# This simple program reads in the 'DOB.txt' file and prints
# out sections of formated names and birthdates

# Lets get the line separator for the system we are on
from os import linesep

# Will contain lines of names
names = ''
# Will contain lines of birth dates
birthdates = ''

# Open the DOB.txt file in read mode
with open('DOB.txt', 'r') as file:
    # Extract names and birthdates from the lines
    for line in file:
        # {name} is a list of ["first name", "last name"] and 
        # {birth_date} is the rest of the line
        *name, birthdate = line.split(maxsplit=2)
        # Check if we shold add a line separator
        eol = linesep if names else ''
        # ...and construct the strings containg names and birth days
        names += eol + ' '.join(name)
        birthdates += birthdate # note: the

# Print out the names
print("Name")
print(names)
# Print a blank line: just for formatting purposes
print()
# Print out the birth dates
print("Birthdate")
print(birthdates)
