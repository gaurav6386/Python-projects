
class BankAccount:
    """ Class definition modeling the behavior of a simple bank account """
   
    def __init__(self, fee_paid,initial_balance):
        """Creates an account with the given balance."""
        self.initial_balance=initial_balance        
        self.fee_paid = fee_paid
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.initial_balance += amount
       
    def withdraw(self, amount):
        """
        Withdraws the amount from the account. Each withdrawal resulting 
        in a negative balance also deducts a penalty fee of 5 dollars
        from the balance.
        """
       
        self.initial_balance -= amount
        if self.initial_balance < 0:
            self.fee_paid +=5
            self.initial_balance -= self.fee_paid
        else:
            pass
        
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.initial_balance
       
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fee_paid

my_account = BankAccount(0,10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5)
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50)
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
print my_account.get_balance(), my_account.get_fees()
        