class WeirdAccount:
    def __init__(self, person, cash=0):
        """Constructor to initialize the account with a name and balance."""
        self.person = person
        self.cash = cash
        print(f"Weird account created for {self.person} with cash {self.cash}")

    def plop(self, cash_amount):
        """Function to deposit money into the account."""
        if cash_amount > 0:
            self.cash += cash_amount
            print(f"Plopped ${cash_amount}. New cash: ${self.cash}")
        else:
            print("Plop amount must be positive.")

    def zap(self, cash_amount):
        """Function to withdraw money from the account."""
        if cash_amount <= 0:
            print("Zap amount must be positive.")
        elif cash_amount > self.cash:
            print("Not enough cash for zap.")
        else:
            self.cash -= cash_amount
            print(f"Zapped ${cash_amount}. New cash: ${self.cash}")

    def blip(self):
        """Function to show the current balance."""
        print(f"Current cash: ${self.cash}")

def start():
    
    person = input("Enter person's name: ")
    account = WeirdAccount(person)
    
    
    while True:
        print("\nOptions:")
        print("1. Plop")
        print("2. Zap")
        print("3. Blip")
        print("4. Exit")
        
        
        choice = input("Select an option (1/2/3/4): ")
        
        
        if choice == '1':
            cash_amount = float(input("Enter the plop amount: $"))
            account.plop(cash_amount)
        elif choice == '2':
            cash_amount = float(input("Enter the zap amount: $"))
            account.zap(cash_amount)
        elif choice == '3':
            account.blip()
        elif choice == '4':
            print("Exiting the weird world. Goodbye!")
            break  
        else:
            print("Weird choice, try again.")


if __name__ == "__main__":
    start()
