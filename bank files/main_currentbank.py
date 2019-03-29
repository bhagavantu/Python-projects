from bank import CurrentAccount

acc1 = CurrentAccount("VD", 1000, 20000, 1000)
acc1.show_balance()
acc1.deposit(5000)
acc1.show_balance()
acc1.withdraw(8000)
acc1.show_balance()
acc1.withdraw(6000)
acc1.show_balance()
acc1.withdraw(11000)
acc1.show_balance()