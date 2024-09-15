from bank_accounts import *

Muzammil = BankAccount(2000, 'Muzammil')
Dave = BankAccount(1000, 'Dave')

Muzammil.getBalance()

Muzammil.deposit(200)

Muzammil.withdraw(200)

Muzammil.transfer(20, Dave)

Dave.getBalance()

Jim = InterestRewardsAccount(200, "Jim")
Jim.getBalance
Jim.deposit(100)

Jim.transfer(100, Muzammil)

Blaze = SavingsAccount(300, "Blaze")
Blaze.getBalance()
Blaze.deposit(200)
Blaze.transfer(10000, Muzammil)
Blaze.transfer(100, Muzammil)


Muzammil.transfer(200, Blaze)
Muzammil.getBalance()

Blaze.getBalance()
