import random
import emoji

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "7️⃣": 4,
    "🍒": 5,
    "🍉": 6,
    "🍍": 8
}

symbol_value = {
    "7️⃣": 77,
    "🍒": 8,
    "🍉": 6,
    "🍍": 4
}


def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="\n")


def deposit():
    while True:
        amount = input("What would you like to deposit ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter an amount greater than 0")
        else:
            print("Enter valid number")

    return amount


def get_number_of_line():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINE) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINE:
                break
            else:
                print("Enter a number of line between 1 and " + str(MAX_LINE))
        else:
            print("Enter valid number")

    return lines


def get_bet():
    while True:
        bet = input("How much do you want to bet? $")
        if bet.isdigit():
            bet = int(bet)
            if bet > MAX_BET:
                bet = MAX_BET
                print("Your bet is $" + str(bet))
                break
            elif bet < MIN_BET:
                bet = MIN_BET
                print("Your bet is $" + str(bet))
                break
            else:
                print("Your bet is $" + str(bet))
                break

        else:
            print("Enter valid number")

    return bet



def game(balance):
    lines = get_number_of_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You do not have enough")
        else:
            break

    print(f"You are betting ${bet} on {lines} line. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"you won on ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"current balance is: ${balance}")
        spin = input("Press enter to spin (q to quit)")
        if spin == "q":
            break
        balance += game(balance)
    print(f"You left with ${balance}")

main()
