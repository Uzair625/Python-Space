class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        print(id(self))
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
            Hello, how would you like to proceed?
            1. Enter 1 to create a pin
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
            5. Enter 5 to Exit.
            6.ID Check of Self Construtor
            """)

            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check_balance()
            elif user_input == '5':
                print("Bye \U0001F44B")
                exit()
            # elif user_input == '6':
            #     print(id(User))
            else:
                print()


    def create_pin(self):
        print("Enter Your Pin... \U0001F512")
        self.pin = input()
        print("Pin Set Successfully \U0001F44C")

    def deposit(self):
        temp = input("Enter Your Pin..")
        if temp == self.pin:
            amount = int(input("Enter the Amount: "))
            self.balance += amount
            print("Deposit Successfully \U0001F4B0")
        else:
            print("Invalid Pin \U0001F625")

    def withdraw(self):
        temp = input("Enter the Pin..")
        if temp == self.pin:
            print("Enter the Amount.. \U0001F4B2")
            amount = int(input("Enter the Amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdraw Successfully Done \U0001F4B8")
            else:
                print("Insufficient Amount... \U0001F625")
        else:
            print("Invalid Pin \U0001F625")

    def check_balance(self):
        temp = input("Enter the Pin..")
        if temp == self.pin:
            print(f"Your Balance: {self.balance}")
        else:
            print("Invalid Pin \U0001F625")


# if __name__ == "__main__":
print("Welcome to the Bank ATM System Sir...")
User = Atm()

# z = id(User)
# print(z)