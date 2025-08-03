"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("first",20, "bangramung", "Thailand")  # name, age, city, country
    hobbies = []

    while True:
        choice = input("What do you want choice (1.display, 2.add hobby, 3.remove hobby , 4.edit age , 5.exit):")
        if choice == '1':
            # Your code here
            print("Name:",person[0])
            print(f"Age:",{person[1]})
            print("city:", person[2])
            print("country:",person[3])
            print("Hobby:",hobbies)
        
        elif choice == '2':
            hobby = input('What is your new hobbies:')
            hobbies.append(hobby)

        elif choice == '3':
            hobbies.pop()

        elif choice == '4':
            person_list = list(person) 
            age = input("How old are you?:")
            person_list [1] = age
            person = tuple(person_list)

        elif choice == '5':
            break

    

if __name__ == "__main__":
    personal_info_manager()