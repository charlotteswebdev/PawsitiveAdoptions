import requests
from pprint import pprint

logo = """
           __
      (___()'`;     ruff
      /,    /`          ruff 
      //--//
"""


def welcome(name):
    print(logo)
    print(f"Welcome to PawsitiveAdoptions.com, {name}!".title())


def shelter_overview():
    try:
        print("Here is the overview of our dog shelters....")
        response = requests.get('http://127.0.0.1:5000/shelter')
        if response.status_code == 200:
            data = response.json()
            pprint(data)
    except Exception as err:
        print(err)


def adopt_a_dog(location, age, size, sex):
    print("Great! Let's find the perfect dog for you to adopt.")
    print(f"Searching for a {size} {sex} {age} dog in {location} ...")
    try:
        response = requests.get(f"http://127.0.0.1:5000/adopt/{location}/{age}/{size}/{sex}")
        if response.status_code == 200:
            data = response.json()
            pprint(data)
    except Exception as err:
        print(err)

#adding member info
def become_member():
    print("Excellent news, please enter the following details:")
    name = input("Type in your full name: ").title()
    email_address = input(f"Welcome aboard {name}, finally, type in your email address: ")
    print("Thanks, your details have been stored in our mailing list 😊")

# Search criteria for dog adoption
def get_dog_details():
    valid_ages = ["Puppy", "Adult", "Senior"]
    valid_sizes = ["Small", "Medium", "Large"]
    valid_sex = ["Male", "Female"]
    valid_locations = ["London", "Belfast"]
#User input validation with error messages.
    while True:
        location = input("Where are you looking to adopt from? London or Belfast? ").title()
        if location in valid_locations:
            break
        else:
            print("Invalid input. Please enter London or Belfast ")
    while True:
        age = input("What age group of dog are you looking for? (Puppy, Adult, Senior): ").title()
        if age in valid_ages:
            break
        else:
            print("Invalid input. Please enter 'Puppy', 'Adult', or 'Senior'.")

    while True:
        size = input("What size of dog are you looking for? (Small, Medium, Large): ").title()
        if size in valid_sizes:
            break
        else:
            print("Invalid input. Please enter 'Small', 'Medium', or 'Large'.")

    while True:
        sex = input("What gender of dog are you looking for? (Male, Female): ").title()
        if sex in valid_sex:
            break
        else:
            print("Invalid input. Please enter 'Male' or 'Female'.")

    return location, age, size, sex

def user_choice():
    action = input("Are you looking to adopt a dog, get an overview of a shelter, or become a member? ("
                   "adopt/overview/member): ").lower()
    if action == "adopt":
        location, age, size, sex = get_dog_details()
        adopt_a_dog(location, age, size, sex)
    elif action == "overview" or action == "shelter":
        shelter_overview()
    elif action == "member":
        become_member()
    else:
        print("Invalid choice. Please type 'adopt' or 'overview'.")
        user_choice()


def run():
    name = input("What is your name? ")
    welcome(name)
    user_choice()


if __name__ == "__main__":
    run()
