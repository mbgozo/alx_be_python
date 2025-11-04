#Monthly Income
income = int(input("Enter your monthly income: "))
#Monthly Expenses
expenses = int(input("Enter your total monthly expenses: "))
#Monthly Savings after expenditure
savings = income - expenses
#Annual Savings
annual_savings = savings * 12
print(f"Your monthly savings are ${savings}")
#Interest Rate
interest = 0.05
#Savings after 1 year with interest
si = (annual_savings * interest) + annual_savings
print(f"Projected savings after one year, with interest, is: ${si}")

