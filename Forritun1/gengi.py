# import necessary libraries
import math

# define bank interest rates and other variables
banks = {
    'Islandsbanki': {'indexed': 2.65, 'unindexed': 8.25},
    'Arion Banki': {'indexed': 2.94, 'unindexed': 8.76},
    'Landsbanki': {'indexed': 2.6, 'unindexed': 8}
}
inflation = 9.5

# get user input
loan_amount = float(input('Enter the loan amount: '))
payment_type = input('Enter payment type (equal payments or equal installments): ')
index_ratio = float(input('Enter the ratio of indexed to unindexed: '))

# calculate monthly payment for each bank
monthly_payments = {}
for bank, interest_rates in banks.items():
    indexed_interest_rate = interest_rates['indexed']
    unindexed_interest_rate = interest_rates['unindexed']
    indexed_amount = index_ratio * loan_amount
    unindexed_amount = loan_amount - indexed_amount
    indexed_total_interest = (indexed_interest_rate / 100) * indexed_amount
    unindexed_total_interest = (unindexed_interest_rate / 100) * unindexed_amount
    total_interest = indexed_total_interest + unindexed_total_interest
    loan_amount_with_interest = loan_amount + total_interest
    if payment_type == 'equal payments':
        indexed_payment = indexed_amount * ((indexed_interest_rate / 100) + (inflation / 100)) / (12 * 25)
        unindexed_payment = unindexed_amount * (unindexed_interest_rate / 100) / (12 * 30)
    else:
        indexed_payment = indexed_amount * ((indexed_interest_rate / 100) + (inflation / 100)) / (12 * 5)
        unindexed_payment = unindexed_amount * (unindexed_interest_rate / 100) / (12 * 5)
    total_monthly_payment = indexed_payment + unindexed_payment
    monthly_payments[bank] = total_monthly_payment

# find the best and worst bank
best_bank = min(monthly_payments, key=monthly_payments.get)
worst_bank = max(monthly_payments, key=monthly_payments.get)

# calculate total payment and difference between best and worst options
best_monthly_payment = monthly_payments[best_bank]
worst_monthly_payment = monthly_payments[worst_bank]
if payment_type == 'equal payments':
    total_payment_best = best_monthly_payment * 12 * 25
    total_payment_worst = worst_monthly_payment * 12 * 30
else:
    total_payment_best = best_monthly_payment * 12 * 5
    total_payment_worst = worst_monthly_payment * 12 * 5
difference = total_payment_worst - total_payment_best

# print results
print(f"The best bank for the loan is {best_bank}.")
print(f"The monthly payment is {best_monthly_payment:.2f} kr.")
print(f"The total payment is {total_payment_best:.2f} kr.")
print(f"The difference between the best and worst options is {difference:.2f} kr.")
