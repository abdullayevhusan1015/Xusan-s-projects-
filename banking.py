# Pyhton banking program 
# show balance 
# Deposit 
# Withdraw 

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount you want it to be deposited in dollars:  "))
    if amount < 0:
        print("Invalid amount, the amount should be greater than 0")
        return 0 
    elif amount == "":
        print("Please enter the amount")
    else:
        return amount
    
def withdraw():
    amount = float(input("Enter the amount to be withdrawn:  "))
    if amount > balance:
        print("Insufficient funds")
        return 0 
    elif amount < 0: 
        print("The amount must be greater than 0")
        return 0 
    else:
        return amount

balance = 0 
is_running = True 

while is_running:
    print("Banking program")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")  
    choice = input("Enter your choice (1-4):  ")
    
    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("this is invalid choice, please try again")

print("Thank you for your interest in our program. Have a nice day")