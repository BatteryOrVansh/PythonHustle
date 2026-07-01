# Define a class named Bank
class Bank:
    # Constructor: Automatically called when object is created
    def __init__(self):
        # Private instance variable
        # Initial balance is set to 5000
        # Double underscore(__) makes it private (name)
        self.__balance = 5000
        
    # Created a method to deposit money into the account
    def deposit(self, amount):
        # Add deposit money account
        self.__balance += amount
    
    # Display the current balance 
    def display_balance(self):
        print(f"Current balance: {self.__balance}")
        
# Create an object of the Bank class
b = Bank()
b.deposit(6000)
b.display_balance()