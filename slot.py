# Pyhton slot machine 
import random
import time 

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results
def print_row(row):
    print("-------------")
    print(" | ".join(row))
    print("-------------")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 2
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 4
        elif row[0] == '🔔':
            return bet * 8
        elif row[0] == '⭐':
            return bet * 15
    return 0
def main():
    balance = 100

    print("------------------------")
    print("Welcome to Python slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("------------------------") 

    while balance > 0:
        print(f"Your balance: ${balance}")
        bet = input("Place your bet amount:  ")
        if not bet.isdigit():
            print("Please enter a valid number!")
            continue
        bet = int(bet)
        if bet <= 0:
            print("the amount must be greater than 0")
            continue
        if bet > balance:
            print("Insufficient funds!")
            continue
       
        balance -= bet
        row = spin_row()
        print("Spinning...  \n")
        time.sleep(3)
        print_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Unfortunately, you lost this round")
        balance += payout
        
        play_again = input("Do you want to spin again? (Y/N):  ").upper()
        if play_again != 'Y':
            break
        
    print("-------------------------------------------")
    print(f"GAME OVER! Your final balance is {balance}")
    print("-------------------------------------------")

if __name__ == "__main__":
    main() 