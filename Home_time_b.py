# PART B: SAVING, WITH A RAISE
# Copy your solution from Part A. Modify your program to include the following:
# 1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
# 2. After the 6th month, increase your salary by that percentage. Do the same after the 12th month, the 18th month, and so on.
# Write a program to calculate how many months it will take you to save up enough money for a down payment. Like before, assume that your investments earn a return 
# of r = 0.04 and the required down payment percentage is 25%. Have the user enter the following variables:
# 1. The starting annual salary
# 2. The percentage of salary to be saved
# 3. The cost of your dream home
# 4. The semi-annual salary raise


portion_downpayment = 0.25
current_savings = 0.00
r = 0.04
number_of_months = 1
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the portion of your salary saved, enter as a decimal:"))
total_cost = float(input("Enter the cost of your dream house:"))
semi_annual_raise = float(input("Enter semi-anual raise as a decimal:"))
monthly_salary = annual_salary/12
downpayment = portion_downpayment*total_cost
# While the downpayment is higher than the amount you have saved, each month a portion of your monthly salary and a return rate of 4% of your current savings will be 
# added to your savings. Additionally, every 6 months your monthly salary will increase by a percentage you entered as a decimal.
while downpayment > current_savings:
    if number_of_months % 6 == 0:
        monthly_salary = monthly_salary*(1 + semi_annual_raise)
    current_savings = current_savings + (monthly_salary*portion_saved) + current_savings*r/12
    number_of_months += 1
print(current_savings)
print("Number of months:", number_of_months)