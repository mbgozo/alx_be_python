#Monthly Income
monthly_income = float(input("Enter your monthly income: "))
#Monthly Expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))
#Monthly Savings after expenditure
monthly_savings = monthly_income - monthly_expenses
#Annual Savings
annual_savings = monthly_savings * 12
print(f"Your monthly savings are ${monthly_savings}")
#Interest Rate
interest = 0.05
#Monthly Savings after 1 year with interest
projected_savings = (annual_savings * interest) + annual_savings
print(f"Projected savings after one year, with interest, is: ${projected_savings}")

# /tmp/correction/5332857174640866405984448069028446271249_5/100739/1424610/python_introduction/finance_calculator.py
#  doesn't contain monthly_savings\s*=\s*(monthly_income\s*-\s*monthly_expenses|float\s*\(\s*monthly_income\s*\)\s*-\s*float\s*\(\s*monthly_expenses\s*\))