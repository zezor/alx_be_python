monthly_income = input("Enter your monthly income: ")
monthly_expense = input("Enter your monthly expenses: ")

monthly_saving = float(monthly_income) - float(monthly_expense)

projected_Savings = (float(monthly_income) * 12) + (float(monthly_income) * 12 * 0.05)

print(f"Your monthly savings are {monthly_saving} ")
print(f"Projected savings after one year, with interest, is: {projected_Savings}.")