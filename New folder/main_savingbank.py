from bank import SavingsAccount

acc1 = SavingsAccount("VD", 1000, 10000, 1000)
acc1.show_balance()
acc1.deposit(5000)
acc1.show_balance()
acc1.withdraw(8000)
acc1.show_balance()
acc1.withdraw(6000)
acc1.show_balance()