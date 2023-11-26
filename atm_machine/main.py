class ATM:

    def __init__(self, pin, balance):
        self.pin = ''
        self.balance = 0
        self.menu()

    def create_pin(self):
        self.pin = input("Enter your PIN: ")
        print("PIN set successfully.")

    def deposit(self):
        pin_prompt1 = input("Enter your PIN: ")
        if pin_prompt1 == self.pin:
            amount = int(input("Enter the amount you want to deposit: "))
            self.balance = self.balance + amount
            print("Deposit Successful.")
        else:
            print("Something went Wrong. Maybe the PIN is incorrect.")

    def withdraw(self):
        pin_prompt = input("Enter your PIN: ")
        if pin_prompt == self.pin:
            amount = int(input("Enter amount you want to withdraw: "))
            if amount < self.balance:
                self.balance -= amount
                print("Withdraw successful.")
            else:
                print("Sorry! Not enough funds to withdraw.")
        else:
            print("Something went wrong. Maybe the PIN is incorrect.")

    def check_balance(self):
        pin_prompt = int(input("Please enter your four digit PIN: "))
        if pin_prompt == self.pin:
            print(f"The available balance in your account is: Rs. {self.balance}.")
        else:
            print("Something went wrong. Maybe the PIN is incorrect.")

    def menu(self):
        user_input = int(input("Hello, Choose an options to proceed:\n"
                               "1. Press 1 to create pin.\n"
                               "2. Press 2 to make deposit.\n"
                               "3. Press 3 to make withdrawal.\n"
                               "4. Press 4 to check balance.\n"
                               "5. Press 5 to exit.\n"
                               "Enter: "))

        while True:
            if user_input == 1:
                self.create_pin()
                break
            elif user_input == 2:
                self.deposit()
                break
            elif user_input == 3:
                self.withdraw()
                break
            elif user_input == 4:
                self.check_balance()
                break
            else:
                print("You didn't choose any valid options. Come back again later.")
                break


nic = ATM('', 0)
while True:
    nic.menu()
