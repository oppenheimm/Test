# Author: tomas bragi thorvaldsson
# Date: 3/26/2023
# Project: assignment_06_03
# Acknowledgements: inspo ur mjög svipuðu dæmi a chegg

class Account:
    def __init__(self, balance):
        self.balance = balance
        
    def update_balance(self):
        pass
        
    def __str__(self):
        return f'Balance: {self.balance:.2f}'

class SavingsAccount(Account):
    INTEREST = 0.05
    BONUS = 0.10
    
    def update_balance(self):
        interest = self.balance * self.INTEREST
        bonus = self.balance * self.BONUS
        self.balance += interest + bonus

class DebitAccount(Account):
    INTEREST = 0.02
    
    def update_balance(self):
        interest = self.balance * self.INTEREST
        self.balance += interest
