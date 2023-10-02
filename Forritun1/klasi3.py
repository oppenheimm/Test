class Account:
    def __init__(self, balance):
        self._balance = balance

    def balance(self):
        return self._balance

    def __str__(self):
        return "Balance: {:.2f}".format(self._balance)


class SavingsAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def update_balance(self):
        self._balance = (self._balance * 1.05) + (self._balance * 0.1)


class DebitAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def update_balance(self):
        self._balance = self._balance * 1.02


#########


def print_accounts(accounts):
    for account in accounts:
        print(account)
    print()


def update_accounts(accounts):
    for account in accounts:
        account.update_balance()


sav1 = SavingsAccount(1000)
deb1 = DebitAccount(1000)
sav2 = SavingsAccount(2000)
deb2 = DebitAccount(4000)

accounts = [sav1, deb1, sav2, deb2]
print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)
