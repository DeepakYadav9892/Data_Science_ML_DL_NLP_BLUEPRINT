"""
Docstring for 05_Functions.5.4_
You are building a simple app that registers users.
you want to seperate concerns:getting input, validating it , and saving it .
Task:
Write register_user() tht cals:
.validate_input()
.save_to_db()"""

def get_input():
    print("Getting user input")


def validate_input():
    print("validating user info ")



def save_to_db():
    print("saving to database ")


def registe_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registered successfully")


registe_user()
