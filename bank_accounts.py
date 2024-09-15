# OPP Project. Bank Account Creation with Inheritance and Error Handling with Exceptions.

class BalanceException(Exception):
    pass

# Class BankAccount created with initial attributes of name and account name


class BankAccount:
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount '{self.name}', created.\nBalance = £{
              self.balance:.2f}"
              )

# Defined a method of showing balance

    def getBalance(self):
        print(f"\n {self.name} balance = £{self.balance:.2f}.")

# Defined a method of deposoting money

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\n\nDeposit Complete. '{
              self.name}' balance = £{self.balance:.2f}."
              )

# Defined Exception to ensure only viable transactions happen

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account {
                                   self.name} only has a balance of £{self.balance:.2f}."
                                   )

# Defined Exception to ensure only available money can be withdrawn

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f"\nWithdrawal Complete. '{
                self.name}' balance = £{self.balance:.2f}."
            )
            self.getBalance

        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}.")

# Defined Exception to ensure only available money can be transferred

    def transfer(self, amount, account):
        try:
            print(f"\n************ Beginning Transfer...🚀...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(
                f"\n************ Beginning Transfer...🚀...\nTransfer Complete! ✅.\n'{
                    self.name}' balance = £{self.balance:.2f}.\n***********"
            )
        except BalanceException as error:
            print(f'\nTransfer Interrupted. ❌{error}')

# Created a new class of bank account which inherits properties from parent 'Bank Account'class but gives 5% interest


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print(f"\nDeposit Complete. ✅")
        self.getBalance

# Created a new class of bank account which inherits properties from 'InterestRewardsAccount'class but overrides


class SavingsAccount(InterestRewardsAccount):
    # using init here because fee is not available in the parent class.
    def __init__(self, initialAmount, accountName):
        # super is used to call methods of parent's class inside a child class. Helps as we do not have to rewrite the same initialization logic in the child class
        super().__init__(initialAmount, accountName)
        self.fee = 5

# Defined method to ensure only available money can be withdrawn

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print(f"\nWithdraw Completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error} ❌")
