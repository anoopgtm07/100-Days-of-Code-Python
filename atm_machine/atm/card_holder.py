class Cardholder:

    def __init__(self, card_num, pin, firstname, lastname, balance):
        self.card_num = card_num
        self.pin = pin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    # Getter Methods

    def get_cardnumber(self):
        return self.card_num

    def get_pin(self):
        return self.pin

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_balance(self):
        return self.balance

    # Setter Values

    def set_cardnumber(self, new_value):
        self.card_num = new_value

    def set_pin(self, new_value):
        self.pin = new_value

    def set_firstname(self, new_value):
        self.firstname = new_value

    def set_lastname(self, new_value):
        self.lastname = new_value

    def set_balance(self, new_value):
        self.balance = new_value

    def print_out(self):
        print("Card Number #: ", self.card_num)
        print("Pin: ", self.pin)
        print("Firstname: ", self.firstname)
        print("Lastname: ", self.lastname)
        print("Balance: ", self.balance)