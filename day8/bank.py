from abc import ABC, abstractmethod
class Account(ABC):
    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withDraw(self):
        pass

class SavingAccount(Account):
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def deposit(self):
        amount = int(input('Enter money to deposit: '))
        self.__balance += amount
        print("Amount deposited:", amount)

    def withDraw(self):
        amount = int(input('Enter money to withdraw: '))
        if self.__balance < amount:
            print("Not Enough Balance")
            return
        self.__balance -= amount
        print("Amount withdrawn:", amount)

class CurrentAccount(Account):
    def __init__(self, limit):
        self.__balance = 0
        self.withDraw_limit = limit

    def get_balance(self):
        return self.__balance

    def deposit(self):
        amount = int(input('Enter money to deposit: '))
        self.__balance += amount
        print("Amount deposited:", amount)

    def withDraw(self):
        amount = int(input('Enter money to withdraw: '))
        if self.__balance + self.withDraw_limit < amount:
            print("Not Enough Balance")
            return
        self.__balance -= amount
        print("Amount withdrawn:", amount)

class Bank:
    def __init__(self):
        self.owner = input('Enter the name: ')
        self.account_number = int(input('Enter account number: '))
        self.account_type = input('Enter account type (Saving/Current): ')

        if self.account_type == "saving":
            self.account = SavingAccount()
        elif self.account_type == "current":
            self.account = CurrentAccount(5000)

class Manager:
    def get_customer_info(self, bankAccount: Bank):
        print(f"Name: {bankAccount.owner}")
        print(f"Account Number: {bankAccount.account_number}")
        print("Account Type: ", end="")
        if isinstance(bankAccount.account, SavingAccount):
            print("Savings Account")
        else:
            print("Current Account")
        print(f"Balance: {bankAccount.account.get_balance()}")

    def __str__(self):
        return "Manager Object bro"
    
customer={}
while True:
    print('Choices:')
    print('1. Create an account')
    print('2. Deposit money')
    print('3. Withdraw money')
    print('4. View details')
    print('5. Exit')
    c = int(input('Enter your choice: '))

    if c == 1:
        b = Bank()
    elif c==2:
        b.account.deposit()
    elif c == 3:
        b.account.withDraw()
    elif c == 4:
        m = Manager()
        m.get_customer_info(b)
    else:
        print("Invalid choice. Please try again.")
        break
