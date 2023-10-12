# Asking for the user's name and creating a welcoming message
user_name = input("Hey there! What should we call you?  \n").title()
print("Welcome to our App,", user_name, ".")
print("To set the mood, choose a color:")
print("1. Blue (for a calm and serene mood)")
print("2. Green (for a fresh and vibrant mood)")

# You can also provide a prompt for the user to enter their choice.
mood_color = input("Enter the number corresponding to your choice: ")

# Then, based on their input, you can provide a corresponding message.
if mood_color == "1":
    print("You've chosen Blue. Get ready to relax and unwind!")
elif mood_color == "2":
    print("Green it is! You're in for a fresh and vibrant experience.")
else:
    print("Invalid choice. Try again!")