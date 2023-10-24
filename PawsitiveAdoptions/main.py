import requests
import json
from pprint import pprint

logo = """
           __
      (___()'`;     ruff
      /,    /`          ruff 
      //--//
"""


# create a class of Exception for error handling
class NoConnection(Exception):
    pass


def welcome(name):
    print(logo)
    print(f"Welcome to PawsitiveAdoptions.com, {name}!".title())


# Error Handling for Name
def validate_name(name):
    if name.replace(" ", "").isalpha():
       return True
    else:
        print("Invalid name. Please use only alphabetic characters.")
        return False


# display shelter details
def shelter_overview():
    try:
        print("Here is the overview of our dog shelters....\n")
        headers = {'Content-Type': 'application/json'}
        response = requests.get('http://127.0.0.1:5000/shelter', headers=headers)
        if response.status_code == 200:
            data = response.json()
            # pprint(data) to display API as a neat object for easier formatting
            formatted_shelter_data = "\n".join([
                f"Shelter id: {shelter['shelter_id']}\nContact no: {shelter['contact_details']}\nShelter name:"
                f" {shelter['shelter_name']}\nLocation: {shelter['location']}\nNumber of dogs:{shelter['total_dogs']}\n"
                for shelter in data])  # used list comprehension to iterate through each shelter
            print(formatted_shelter_data)
        else:
            raise NoConnection("Unable to connect to our database at the moment")

    except NoConnection as e:
        print(e)
    except Exception as err:
        print(err)


# Adopt a dog
def adopt_a_dog(location, age, size, sex):
    print("Great! Let's find the perfect dog for you to adopt.")
    print(f"Searching for a {size} {sex} {age} dog in {location} ...")
    print(f"The dogs available for adoption that meet your criteria in {location} are:")
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.get(f"http://127.0.0.1:5000/adopt/{location}/{age}/{size}/{sex}", headers=headers, )
        if response.status_code == 200:
            data = response.json()
            pprint(data)
        else:
            raise NoConnection("Unable to connect to our database at the moment")
    except NoConnection as e:
        print(e)
    except Exception as exc:
        print(exc)


# Add new member
def add_new_member(new_member):
    try:
        headers = {"Content-Type": 'application/json'}
        response = requests.post("http://127.0.0.1:5000/new", headers=headers, data=json.dumps(new_member))
        if response.status_code == 200:
            print("We have successfully added your details to our members list")
        else:
            print("Failed to add data")
    except Exception as err:
        print(err)


# User Input Validation for Email
def validate_email(email):
    if " " not in email and "@" in email and "." in email:
        return True
    else:
        print("Invalid email address. Please enter a valid email address.")
        return False


# collect new member details and validate full name and email address
def collect_member_details():
    print("Excellent news, please enter the following details:")
    while True:
        full_name = input("Type in your full name: ").title()
        name_parts = full_name.split()
        if len(name_parts) >= 2 and all(part.isalpha() for part in name_parts):
            break
        else:
            print("Invalid name. Please enter both your first and last name using only alphabetic characters.")

    while True:
        email_address = input(f"Welcome aboard {full_name}, finally, type in your email address: ")
        if validate_email(email_address):
            break

    new_member = {
        "full_name": full_name,
        "email_address": email_address
    }
    return new_member


# Search criteria for dog adoption
def get_dog_details():
    valid_ages = ["puppy", "adult", "senior"]
    valid_sizes = ["small", "medium", "large"]
    valid_sex = ["male", "female"]
    valid_locations = ["London", "Belfast"]
    # User input validation with error messages.
    while True:
        location = input("Where are you looking to adopt from? London or Belfast? ").title()
        if location in valid_locations:
            break
        else:
            print("Invalid input. Please enter London or Belfast ")

    while True:
        age = input("What age group of dog are you looking for? (Puppy, Adult, Senior): ").lower()
        if age in valid_ages:
            break
        else:
            print("Invalid input. Please enter 'Puppy', 'Adult', or 'Senior'.")

    while True:
        size = input("What size of dog are you looking for? (Small, Medium, Large): ").lower()
        if size in valid_sizes:
            break
        else:
            print("Invalid input. Please enter 'Small', 'Medium', or 'Large'.")

    while True:
        sex = input("What gender of dog are you looking for? (Male, Female): ").lower()
        if sex in valid_sex:
            break
        else:
            print("Invalid input. Please enter 'Male' or 'Female'.")

    return location, age, size, sex


# obtaining user's choice
def user_choice():
    action = input("Are you looking to adopt a dog, get an overview of a shelter, or become a member? ("
                   "adopt/overview/member): ").lower()
    if action == "adopt":
        location, age, size, sex = get_dog_details()
        adopt_a_dog(location, age, size, sex)
    elif action == "overview" or action == "shelter":
        shelter_overview()
    elif action == "member":
        new_member_data = collect_member_details()
        add_new_member(new_member_data)
    else:
        print("Invalid choice. Please type 'adopt' or 'overview' or 'member'.")


def try_again():
    choice = input("Do you want to try another option? (yes/no): ").lower()
    if choice == "yes" or choice == "y":
        new_option()
    elif choice == "no" or choice == "n":
        print("Thank you for using PawsitiveAdoptions.com. Goodbye!")
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")
        try_again()


def run():
    name = input("What is your name? ")
    if validate_name(name):
        welcome(name)
        user_choice()
        try_again()


def new_option():
    user_choice()
    try_again()


if __name__ == "__main__":
    run()
