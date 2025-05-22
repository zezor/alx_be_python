monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your monthly expenses: "))

monthly_saving = monthly_income - monthly_expense

projected_Savings = (monthly_saving * 12) + (monthly_saving * 12 * 0.05)

print(f"Your monthly savings are {monthly_saving} ")
print(f"Projected savings after one year, with interest, is: {projected_Savings}.")