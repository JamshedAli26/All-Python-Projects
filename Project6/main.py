max_lines = 3
max_bet = 100
min_bet = 1
def deposit():
    while True:
        amount = input("What would you like to deposit ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please Enter a number")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(max_lines) + ")? ")
        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= max_lines:
                    break
            else:
                print("Please Enter a valid number of lines.")
        else:
            print("Please Enter a number.")

        return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            
            if min_bet <= amount <= max_lines:
                    break
            else:
                print(f"Amount must be between ${min_bet} - ${max_bet}.")
        else:
            print("Please Enter a number.")

    return amount
   
   
def main():
    balance = deposit()
    lines = get_number_of_lines()
    # print(balance, lines)
    bet = get_bet()
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. total bet is equal to {total_bet}")

main()