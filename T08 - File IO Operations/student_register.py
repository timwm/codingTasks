# File: student_register.py
# *** Task 2 ***

# This simple program prompts the user for the number of students being registered,
# asks for their ID numbers, and writes them to a text file named 'reg_form.txt'
# with a dotted line after each ID number


def create_registration_form():
    # Ask the user how many students are registering
    num_students = int(input("Please enter the number of students registering: "))

    # Open the file in write mode
    with open('reg_form.txt', 'w') as file:
        # Loop for the specified number of students
        for i in range(1, num_students + 1):
            # Ask the user to enter the next student ID number
            student_id = input(f"Enter Student ID for Student #{i}: ")
            # Write the student ID to the file
            file.write(f"{student_id}\n{'.'*30}\n")

    print(f"Registration form created successfully in 'reg_form.txt'.")


# This line checks if this program is run directly and is not being imported
if __name__ == "__main__":
    create_registration_form()
