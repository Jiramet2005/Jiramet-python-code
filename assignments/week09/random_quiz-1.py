"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
#แบบง่ายที่ทำเอง
"""
import random

def test_random():
    #สุ่มเลขระหว่าง 1-10 เก็บไว้ในตัวแปล random_number
    random_number = random.randint(1, 7)
    for i in range(6):
        guessed = int(input(f"Try to guess the number (Attempt {i+1}/6): "))
        if random_number == guessed:
            print("You guessed correctly.")
            break 
        elif random_number < guessed:
            print("Too much")
        elif random_number > guessed:
            print("Too low")
        print(random_number) 
    
test_random()
"""
#ตามอาจาร์
import random
def test_random():
    print("=== SIMPLE GUESSING GAME ===")
    print("Guess my number between 1 and 20!")
    print("You habe 6 attempts.")

    random_number = random.randint(1,10)
    for i in range(6):
        guessed = int(input(f"Try to guess the number (Attempt {i+1}/6): "))
        if random_number == guessed:
            print(f"You guessed correctly.{i+1} attempt")
            break 
        elif random_number < guessed:
            print("Too much")
        elif random_number > guessed:
            print("Too low")
        print(random_number) 
test_random()