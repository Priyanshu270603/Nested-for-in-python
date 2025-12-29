def format_name(first_name, middle_name):
    return first_name.capitalize() + " " + middle_name.capitalize()


while True:
    first_name = input("Please enter your first name: ").strip()
    if first_name:
        break
    print("first name is required.")

while True:
    middle_name = input("Please enter your middle name: ").strip()
    if middle_name:
        break
    print("Middle name is required.")

full_name = format_name(first_name, middle_name)

print("Your name is: ", full_name)