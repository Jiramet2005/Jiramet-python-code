monthly_income = float(input(" User's monthly income in THB:"))
rent = float(input(" Monthly rent/housing cost:"))
food = int(input(" Monthly food budget in THB: "))
transportation = float(input("Monthly transportation expenses:"))
entertainment = int(input(" Monthly entertainment budget:"))
emergency = float(input(" Percentage to save for emergency (e.g., 10.5):"))
investment = float(input("Percentage to invest (e.g., 15.0)"))

Fixed = rent + transportation
total_variable = food + entertainment
total_expenses = Fixed + total_variable
Renmaining = monthly_income - total_expenses
Emergency_Fund = monthly_income * (emergency/100)
investment_Amoount = monthly_income * (investment/100)
Available_for_Savinge = Renmaining - Emergency_Fund - investment
Expense_Ratio = (total_expenses / monthly_income)*100

print("=== MONTHLY BUDGET REPORT ===")

print("income:",monthly_income)
print("Fixed Expenses:",Fixed)
print("variable Expenses:",total_variable)
print("Total Expenses:",total_expenses)
print("Remaining:",Renmaining)

print("===SAVINGS BREAKDOWN===")
print("Emergency Fund (10%):",Emergency_Fund)
print("Investment(15%):",investment_Amoount)
print("Availavle for Savings:",Available_for_Savinge)

print("===ANALYSIS===")
print("Expense Ration:",Expense_Ratio)