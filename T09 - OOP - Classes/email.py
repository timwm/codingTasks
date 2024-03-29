# File: email.py

# This is a simple email simulation program which allows populating, reading
# and listing emails in an inbox. It implements a menu driven interface

class Email:
    # Class variable
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        # Instance variables
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Class method to mark the email as read
    def mark_as_read(self):
        self.has_been_read = True


# Variable to store email objects
inbox = []

# Function to populate the inbox with sample emails
def populate_inbox(email_address, subject_line, email_content):
    global inbox
    inbox.append(Email(email_address, subject_line, email_content))

# Function to list emails in the inbox
# @param    {unread}    None|Bool    Provides a hint wether to dispay all, unread or read emails
#     None  - list both read and unread eamils
#     False - list only read emails
#     True  - list only unread emails
def list_emails(unread=None):
    global inbox
    kind = "" if unread is None else "Unread" if unread else "Read" # What kind of listing the user wants
    placeholder = "Your inbox is empty." if unread is None else f"You don't have any {kind} emails."

    print()
    print("Your {}{}Inbox:".format(kind, " " if kind else "").center(64))
    print("=" * 64)
    
    for i, email in enumerate(inbox):
        has_been_read = email.has_been_read

        if unread is None:
            status = "Read" if has_been_read else "Unread"
            placeholder = ''
            print(f"{i} [{status}] {email.subject_line}")

        elif unread is not has_been_read:
            placeholder = ''
            print(f"{i} {email.subject_line}")

    print(placeholder.center(64))

# Function to read a selected email and mark it as read
# @param    {index}    None|int    Index of the email to retrieve from the inbox
#    None - Passing None will display a menu and prompt the user to provide an index
def read_email(index=None):
    global inbox
    inbox_size = len(inbox)

    if not inbox_size:
        print()
        print("You don't have any emails yet :(".center(64))
        return

    last_email_index = inbox_size - 1
    # Range string of the valid indices that will be displayed to the user
    inbox_range = ("0-" if last_email_index else "") + f"{last_email_index}"

    # Implement a recursion using a while loop to reduce the posibility of a stack overflow
    # incases where the inbox is very large
    while True:
        while index is None:  # We need to display the menu
            print()
            print('=' * 64)
            print(f"[{inbox_range}] - index of email to read")
            print("M - Goto [M]enu")

            index = input("Enter your choice: ")

            if index == "M":  # Go back to the main menu
                return
            
            index = int(index)

            # Check if the user provided a valid index else redisplay the menu
            if index < 0 or index > last_email_index:
                print('*' * 64)
                print(f"Invalid index. Must be in the range: [{inbox_range}]")
                print('*' * 64)

                index = None
                continue
            break

        if 0 <= index < inbox_size:  # Display the details of the email the user wants to read
            email = inbox[index]

            print()
            print(f"Email #{index} Details:".center(64))
            print('+' * 64)
            print(f"From: {email.email_address}")
            print(f"Subject: {email.subject_line}")
            print(f"Content: {email.email_content}")

            # Remember to mark this email as read
            email.mark_as_read()
            print()
            print(f"Email from {email.email_address} marked as read.")

            index = None  # Set this to reprompt the user with the menu
            continue

        # The user provided an invalid index
        print("{}\nInvalid index. Please choose a valid index in the range: [{inbox_range}]\n{}".format(
            '*' * 64, '*' * 64, inbox_range=inbox_range
        ))


# This line checks if this program is run directly and is not being imported
if __name__ == "__main__":
    # Used to prepopulate the inbox
    email_seed = [
        ("sender1@example.com", "Welcome to HyperionDev!", "Content of the first email"),
        ("sender2@example.com", "Great work on the bootcamp!", "Content of the second email"),
        ("sender3@example.com", "Your excellent marks!", "Content of the third email")
    ]

    # Populate the inbox with sample emails
    for email in email_seed:
        populate_inbox(*email)

    # List emails in the inbox
    list_emails()

    # Sample menu for the user
    while True:
        print()
        print(f"Main Menu:".center(64))
        print('=' * 64)
        print("1. Read an email")
        print("2. View Unred emails")
        print("3. Quit application")

        choice = input("Enter your choice: ")

        if choice == "1":
            read_email()
        elif choice == "2":
            list_emails(unread=True)
        elif choice == "3":
            print("\nExiting application. Goodbye!")
            break
        else:
            print("{}\nDidn't quite get that. Please enter a valid option.\n{}".format(
                '*' * 64, '*' * 64
            ))
