class CheckingAccount:
    def __init__(self,name,address,account_number):
        self._name = name
        self._address = address
        self._account_number = account_number
        self._balance = 0.0
        
    def deposit(self, amount):
        self._balance += amount
            
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient Funds")
        self._balance -= amount
        
    def get_balance(self):
        return self._balance
 
checking = CheckingAccount("Alec Lang", "123 Circle Drive", "1234")
            
checking.deposit(1000.0)
checking.withdraw(500.0)
checking.deposit(250.0)
            
print("Balance: $", checking.get_balance())
