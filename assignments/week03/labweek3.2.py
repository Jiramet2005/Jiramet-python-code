    # Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice =='1':
           print("you balance:",balance)
        
        if choice =='2':
            withdraw = float(input("How much do you want to withdaw:"))
            if withdraw <= 0:
                print("Cannot withdraw less than 0")
            else:
                balance = balance - withdraw
                print("Remaining balance:",balance)
        
        elif choice =='3': 
            deposit = float(input("How much money will you deposit? :"))
            if deposit <= 0:
                print("Cannot deposit less than 0")
            else:
                balance = balance + withdraw
                print("you balance now = ",balance)                

        else :
            print("Exit")
            break
else:
    print("Invalid PIN")