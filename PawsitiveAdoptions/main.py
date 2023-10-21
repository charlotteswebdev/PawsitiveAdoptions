logo = """
           __
      (___()'`;     ruff
      /,    /`          ruff 
      //--//
"""


def welcome(name):
    print(logo)
    print(f"Welcome to PawsitiveAdoptions.com, {name}!".title())


def get_dog_details():
    valid_ages = ["puppy", "adult", "senior"]
    valid_sizes = ["small", "medium", "large"]
    valid_genders = ["male", "female"]

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
        gender = input("What gender of dog are you looking for? (Male, Female): ").lower()
        if gender in valid_genders:
            break
        else:
            print("Invalid input. Please enter 'Male' or 'Female'.")

##This needs changed
    while True:
        try:
            distance = int(input("How far are you willing to travel to adopt a dog? (Enter distance in miles): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for distance.")

    return age, size, gender, distance

def shelter_choice():
    shelter_choice_p = input("Please decide between our Belfast or London shelter (Belfast/London)").title()
    if shelter_choice_p == "Belfast":
        print("Belfast, it is.")
    elif shelter_choice_p == "London":
        print("London it is.")
    else:
        print("Invalid choice. Please type 'Belfast' or 'London'.")
        shelter_choice()

def give_dog_details():
    valid_ages = ["puppy", "adult", "senior"]
    valid_sizes = ["small", "medium", "large"]
    valid_genders = ["male", "female"]

    while True:
        age = input("What age group is the dog? (Puppy, Adult, Senior): ").lower()
        if age in valid_ages:
            break
        else:
            print("Invalid input. Please enter 'Puppy', 'Adult', or 'Senior'.")

    while True:
        size = input("What size is the dog? (Small, Medium, Large): ").lower()
        if size in valid_sizes:
            break
        else:
            print("Invalid input. Please enter 'Small', 'Medium', or 'Large'.")

    while True:
        gender = input("What gender is the dog? (Male, Female): ").lower()
        if gender in valid_genders:
            break
        else:
            print("Invalid input. Please enter 'Male' or 'Female'.")

    rescue_name_p = input("Thanks, and what is the dog's name: ").title()
    print(f"{rescue_name_p} is most welcome, we will take good care of them.")
    shelter_choice()


##This needs changed
def shelter_overview():
    while True:
        try:
            distance = int(input("What distance are you willing to travel to? (Enter distance in miles): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for distance.")
    print(f"Shelter Overview: Willing to travel within {distance} miles.")


def adopt_dog():
    print("Great! Let's find the perfect dog for you to adopt.")
    age, size, gender, distance = get_dog_details()
    print(f"Searching for a {size} {gender} {age} dog within {distance} miles...")

def rehome_dog():
    print("Alright, please enter the following info of the dog you'd like to rehome:")
    give_dog_details()

def userchoice():
    action = input("Are you looking to adopt a dog, rehome a dog, or get an overview of the shelter? (adopt/rehome/overview): ").lower()

    if action == "adopt":
        adopt_dog()
    elif action == "overview" or action == "shelter":
        shelter_overview()
    elif action == "rehome":
        rehome_dog()
    else:
        print("Invalid choice. Please type 'adopt' or 'overview'.")
        userchoice()


def run():
    name = input("What is your name? ")
    welcome(name)
    userchoice()


if __name__ == "__main__":
    run()
