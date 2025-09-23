import random

def test_random():
    #สุ่มเลขระหว่าง 1-10 เก็บไว้ในตัวแปล random_number
    random_number = random.randint(1, 100)
    guessed = int(input("Try to guess the number.:"))
    if random_number == guessed:
        print("You guessed correctly.")
    if random_number < guessed:
        print("Too much")
    if random_number > guessed:
        print("Too low")
    print(random_number) 
    

test_random()