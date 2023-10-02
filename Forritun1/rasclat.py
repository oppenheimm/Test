import sys

indexed_term = 25
non_indexed_term = 30

indexed_n_payments = indexed_term * 12
non_indexed_n_payments = non_indexed_term * 12

def get_loan_details():
    principal = float(input("Enter the loan amount: "))
    indexed_ratio = float(input("Enter the percentage of indexed loan (e.g. 30 for 30%): ")) / 100
    non_indexed_ratio = 1 - indexed_ratio

    return principal, indexed_ratio, non_indexed_ratio

def calculate_loan(principal, indexed_ratio, non_indexed_ratio, interest_rate_indexed, interest_rate_non_indexed, inflation_rate):
    indexed_loan = principal * indexed_ratio
    non_indexed_loan = principal * non_indexed_ratio

    indexed_term = 25
    non_indexed_term = 30

    indexed_monthly_rate = (interest_rate_indexed + inflation_rate) / (12 * 100)
    non_indexed_monthly_rate = interest_rate_non_indexed / (12 * 100)

    indexed_n_payments = indexed_term * 12
    non_indexed_n_payments = non_indexed_term * 12

    indexed_monthly_payment = indexed_loan * (indexed_monthly_rate * (1 + indexed_monthly_rate) ** indexed_n_payments) / ((1 + indexed_monthly_rate) ** indexed_n_payments - 1)
    non_indexed_monthly_payment = non_indexed_loan * (non_indexed_monthly_rate * (1 + non_indexed_monthly_rate) ** non_indexed_n_payments) / ((1 + non_indexed_monthly_rate) ** non_indexed_n_payments - 1)


    total_monthly_payment = indexed_monthly_payment + non_indexed_monthly_payment
    total_payment = total_monthly_payment * max(indexed_n_payments, non_indexed_n_payments)

    interest_payment = total_payment - principal

    indexed_interest_payments = []
    indexed_principal_payments = []
    non_indexed_interest_payments = []
    non_indexed_principal_payments = []

    for i in range(max(indexed_n_payments, non_indexed_n_payments)):
        if i < indexed_n_payments:
            indexed_interest_payment, indexed_principal_payment = get_interest_and_principal_payment(indexed_monthly_payment, indexed_loan, indexed_monthly_rate, indexed_n_payments-i)
            indexed_interest_payments.append(indexed_interest_payment)
            indexed_principal_payments.append(indexed_principal_payment)
        else:
            indexed_interest_payments.append(0)
            indexed_principal_payments.append(0)

        if i < non_indexed_n_payments:
            non_indexed_interest_payment, non_indexed_principal_payment = get_interest_and_principal_payment(non_indexed_monthly_payment, non_indexed_loan, non_indexed_monthly_rate, non_indexed_n_payments-i)
            non_indexed_interest_payments.append(non_indexed_interest_payment)
            non_indexed_principal_payments.append(non_indexed_principal_payment)
        else:
            non_indexed_interest_payments.append(0)
            non_indexed_principal_payments.append(0)

    return total_payment, total_monthly_payment, interest_payment, indexed_interest_payments, indexed_principal_payments, non_indexed_interest_payments, non_indexed_principal_payments


def get_loan_details():
    principal = float(input("Enter the loan amount: "))
    indexed_ratio = float(input("Enter the percentage of indexed loan (e.g. 30 for 30%): ")) / 100
    non_indexed_ratio = 1 - indexed_ratio
    inflation_rate = float(input("Enter the inflation rate (e.g. 3.1 for 3.1%): "))

    return principal, indexed_ratio, non_indexed_ratio, inflation_rate

def get_interest_and_principal_payment(monthly_payment, loan, monthly_rate, n_payments):
    interest_payment = loan * monthly_rate
    principal_payment = monthly_payment - interest_payment
    return interest_payment, principal_payment


def main():
    principal, indexed_ratio, non_indexed_ratio, inflation_rate = get_loan_details()

    banks = {
        'arionbanki': {'indexed': 8.34, 'non_indexed': 2.94},
        'landsbankinn': {'indexed': 8.0, 'non_indexed': 2.6},
        'islandsbanki': {'indexed': 8.25, 'non_indexed': 2.65}
    }

    results = {}

    for bank, rates in banks.items():
        total_payment, total_monthly_payment, interest_payment, indexed_interest_payments, indexed_principal_payments, non_indexed_interest_payments, non_indexed_principal_payments = calculate_loan(principal, indexed_ratio, non_indexed_ratio, rates['indexed'], rates['non_indexed'], inflation_rate)
        results[bank] = {
            'total_payment': total_payment,
            'total_monthly_payment': total_monthly_payment,
            'interest_payment': interest_payment,
            'indexed_interest_payments': indexed_interest_payments,
            'indexed_principal_payments': indexed_principal_payments,
            'non_indexed_interest_payments': non_indexed_interest_payments,
            'non_indexed_principal_payments': non_indexed_principal_payments
        }

    best_bank = min(results, key=lambda x: results[x]['total_payment'])
    worst_bank = max(results, key=lambda x: results[x]['total_payment'])

    print("Best bank for this loan: ", best_bank)

    extra_payment = 0
    if not input("Is this your first house loan? (y/n): ").startswith('y'):
        if best_bank == 'arionbanki':
            extra_payment = 64995
        elif best_bank == 'islandsbanki':
            extra_payment = 64900
        elif best_bank == 'landsbankinn':
            extra_payment = 59900

    total_payment = results[best_bank]['total_payment'] + extra_payment

    print("Total payment: ", total_payment)
    print("Monthly payment: ", results[best_bank]['total_monthly_payment'])
    print("Interest payment over the loan term: ", results[best_bank]['interest_payment'])

    print("\nWorst bank for this loan: ", worst_bank)
    print("Total payment: ", results[worst_bank]['total_payment'])
    print("Monthly payment: ", results[worst_bank]['total_monthly_payment'])
    print("Interest payment over the loan term: ", results[worst_bank]['interest_payment'])

    difference = results[worst_bank]['total_payment'] - results[best_bank]['total_payment']
    print(f"\nDifference between the best and worst bank: {difference:.2f} kr.")

    if best_bank in results:
        payments = results[best_bank]
        print(f"\nMonthly payments for {best_bank}:")
        print("Indexed loan:")
        print(f"Monthly payment split: Interest payment = {payments['indexed_interest_payments'][0]:.2f} kr, Principal payment = {payments['indexed_principal_payments'][0]:.2f} kr, Total payment = {payments['indexed_interest_payments'][0]+payments['indexed_principal_payments'][0]:.2f} kr")
        print("Non-indexed loan:")
        print(f"Monthly payments split: Interest payment = {payments['non_indexed_interest_payments'][0]:.2f} kr, Principal payment = {payments['non_indexed_principal_payments'][0]:.2f} kr, Total payment = {payments['non_indexed_interest_payments'][0]+payments['non_indexed_principal_payments'][0]:.2f} kr")

    if extra_payment > 0:
        print(f"\nExtra payment added: {extra_payment:.2f} kr")
        total_payment += extra_payment
        print(f"Total payment with extra payment: {total_payment:.2f} kr")



if __name__ == "__main__":
    main()
