# ----------- CONSTANTS --------------

CANADA_TAXRATE = 0.26

DENMARK_BASE_TAXRATE = 0.0
DENMARK_TAX_INCREASE = 0.10
DENMARK_INCOME_STEPS = 1000

NORWAY_TAX_LOWER = 0.10
NORWAY_TAX_HIGHER = 0.40
NORWAY_TAX_THRESHOLD = 3000

USA_TAX_1 = 0.12
USA_THRESHOLD_1 = 1500
USA_TAX_2 = 0.25
USA_THRESHOLD_2 = 6000
USA_TAX_3 = 0.38
USA_THRESHOLD_3 = 10000
USA_TAX_4 = 0.15

VERBOSE = False

# ----------- MAIN --------------

income = int(input('Income: '))

while income > 0:

    # -------- Canada
    canada_tax = CANADA_TAXRATE * income
    minimum_tax = canada_tax

    # -------- Denmark
    denmark_tax = 0
    current_taxrate = DENMARK_BASE_TAXRATE
    remaining_income = income
    while remaining_income > DENMARK_INCOME_STEPS:
        denmark_tax += DENMARK_INCOME_STEPS * current_taxrate
        current_taxrate += DENMARK_TAX_INCREASE
        remaining_income -= DENMARK_INCOME_STEPS
    denmark_tax += remaining_income * current_taxrate

    if denmark_tax < minimum_tax:
        minimum_tax = denmark_tax

    # --------- Norway
    norway_tax = 0
    if income > NORWAY_TAX_THRESHOLD:
        norway_tax += NORWAY_TAX_THRESHOLD * NORWAY_TAX_LOWER
        norway_tax += (income - NORWAY_TAX_THRESHOLD) * NORWAY_TAX_HIGHER
    else:
        norway_tax += income * NORWAY_TAX_LOWER

    if norway_tax < minimum_tax:
        minimum_tax = norway_tax

    # ---------- USA
    usa_tax = 0
    if income > USA_THRESHOLD_3:
        usa_tax += income * USA_TAX_4
    elif income > USA_THRESHOLD_2:
        usa_tax += income * USA_TAX_3
    elif income > USA_THRESHOLD_1:
        usa_tax += income * USA_TAX_2
    else:
        usa_tax += income * USA_TAX_1

    if usa_tax < minimum_tax:
        minimum_tax = usa_tax


    # --------- Results
    lowest_tax_countries = ''
    if canada_tax == minimum_tax:
        lowest_tax_countries += 'Canada '
    if denmark_tax == minimum_tax:
        lowest_tax_countries += 'Denmark '
    if norway_tax == minimum_tax:
        lowest_tax_countries += 'Norway '
    if usa_tax == minimum_tax:
        lowest_tax_countries += 'USA '


    if VERBOSE:
        print('Canada:', canada_tax)
        print('Denmark:', denmark_tax)
        print('Norway: ', norway_tax)
        print('USA:    ', usa_tax)


    print('Lowest tax:', minimum_tax)
    print(lowest_tax_countries)

    income = int(input('Income: '))