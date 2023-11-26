from card_holder import Cardholder


def print_menu():
    print("Please choose from the options below: ")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Check Balance")
    print("4. Exit")


Card_holder = Cardholder()


def deposit():
    try:
        deposit_amount = float(input("How much Rs. would you like to deposit: "))
        Card_holder.set_balance(Card_holder.get_balance() + deposit_amount)
        print(f"Thank you for your money. Your new balance is: {Card_holder.get_balance()}")
    finally:
        print("Invalid Input.")


def withdraw():
    try:
        withdrawal_amount = float(input("How much Rs. would you like to withdraw: "))
        if withdrawal_amount < Card_holder.get_balance():
            Card_holder.set_balance(Card_holder.get_balance() - withdrawal_amount)
            print(f"Here is your Rs. {Card_holder.get_balance()} ")
        else:
            print("Sorry not enough fund.")
    finally:
        print("Invalid input.")


def check_balance():
    print(f"Your available balance is: {Card_holder.get_balance()}")


if __name__ == "__main__":
    current_user = Card_holder("", "", "", "", "")

    list_of_users = [Card_holder(123456789, 1234, 'Anup', 'Gautam', 100.20),
                     Card_holder(321654987, 9874, 'Ajit', 'Gautam', 150.25),
                     Card_holder(987654321, 3216, 'Ashish', 'Gautam', 250.36),
                     Card_holder(789456123, 3214, 'Prakash', 'Gautam', 500),
                     Card_holder(987456321, 9876, 'Kabita', 'Gautam', 1000)]

    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please enter your Debit Card Number: ")
            debitMatch = [holder for holder in list_of_users if holder.card_num == debitCardNum]
            if len(debitMatch) > 0:
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized. Please try again.")
        finally:
            print("Card number not recognized. Please try again.")

    while True:
        try:
            userPin = int(input("Please enter your PIN: ").strip())
            if current_user.get_pin() == userPin:
                break
            else:
                print("Invalid PIN. Please try again.")
        finally:
            print("Invalid PIN. Please try again.")

    print(f"Welcome {current_user.get_firstname()}.")
    option = 0
    while True:
        print_menu()
        try:
            option = int(input())
        finally:
            print("Invalid input. Please try again.")

        if option == 1:
            deposit()
        elif option == 2:
            withdraw()
        elif option == 3:
            check_balance()
        elif option == 4:
            break
        else:
            option = 0
    print("Thank You. Have a nice day.")
