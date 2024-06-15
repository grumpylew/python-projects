import random
import time

# Specify Slot Machine parameters (Global Constant)
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,  # most valuable
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 8,
    "B" : 6,
    "C" : 4,
    "D" : 2  
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
    return winnings

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        while symbol_count > 0:
            all_symbols.append(symbol)
            symbol_count -= 1

    columns = []                            # Final columns of slot machine [], [], []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]    # Make a Copy
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

# Transpose the result
def print_slot_machine(columns):
    # Loop through each column and print first value
    # print(columns)
    for index in range(COLS):
        for i, column in enumerate(columns):
            if i != 2:
                print(column[index], end = " | ")
            else:
                print(column[index], end = "")
        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        try:
            # Try to convert to float
            amount = int(amount)
            # Check if amount is positive
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{str(MAX_LINES)})? ")
        try:
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be between 1 and 3")
        except ValueError:
            print("Please enter a valid number.")
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        try:
            # Try to convert to float
            amount = int(amount)
            # Check if amount is positive
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        except ValueError:
            print("Please enter a valid number.")
    return amount   

def game(balance):
    lines = get_number_of_lines()
    time.sleep(1)

    while True:
        bet = get_bet()
        total_bet = lines * bet
        
        if total_bet > balance:
            print(f"You do not have enough balance. Top up ${abs(balance - total_bet)} to play. ")
            make_deposit = input("Press ENTER to make a deposit. (q to quit)")
            if make_deposit == 'q':
                break
            else:
                balance += deposit()
        else:
            balance -= total_bet
            break

    time.sleep(1) 
    print(f"You are betting ${bet} on {lines} lines.")
    time.sleep(2)
    print(f"Total bet is equal to: ${total_bet}. You have a balance of ${balance}.")
    print("")
    time.sleep(1)
    print("Generating slots...")
    time.sleep(3)
    generate_slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(generate_slots)
    time.sleep(2)
    print("Checking winnings...")
    time.sleep(3)
    winnings = check_winnings(generate_slots, lines, bet, symbol_value)
    print("")
    if winnings != 0:
        print(f"******** You won: ${winnings} !!! ********")
    else:
        print("Try your luck next time! :(")
    print("")
    return balance + winnings

def main():
    balance =  deposit()
    time.sleep(1)
    while balance >= 0:
        balance = game(balance)
        time.sleep(1)
        print(f"Your current balance is ${balance}.")
        time.sleep(1)
        spin = input("Press ENTER to spin. (q to quit)")
        if spin == 'q':
            break
    
main()