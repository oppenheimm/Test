company_data = {}

# Open the file and read in each line
with open(
    r"C:\Users\Tommi\Forritun Visual stud\final_2021_textfiles\expenses1.txt"
) as file:
    for line in file:
        # Split the line into its components
        company, month, amount = line.strip().split(", ")

        # Add the amount to the company's total
        if company not in company_data:
            company_data[company] = {"total": 0, "months": {}}

        company_data[company]["total"] += int(amount)

        # Add the amount to the company's monthly total
        if month not in company_data[company]["months"]:
            company_data[company]["months"][month] = 0

        company_data[company]["months"][month] += int(amount)

# Print out the results
for company, data in company_data.items():
    print(f"{company}: Total amount = {data['total']}")

    for i in range(1, 13):
        amount = data["months"].get(str(i), 0)
        print(f"\tMonth {i}: {amount}")
