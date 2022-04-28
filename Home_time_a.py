# PART A: HOUSE HUNTING
# You have graduated from MIT and now have a great job! You move to the San Francisco Bay Area and decide that you want to start saving to buy a house. 
# As housing prices are very high in the Bay Area, you realize you are going to have to save for several years before you can afford to make the down payment on a house. 
# In Part A we are going to determine how long it will take you to save enough money to make the down payment given the following assumptions:
# 1. Call the cost of your dream home total_cost.
# 2. Call the portion of the cost needed for a down payment portion_down_payment. For simplicity assume that portion_down_payment = 25%.
# 3. Call the amount that you have saved thus far current_savings. You start with a current savings of $0.
# 4. Assume that you invest your current savings wisely, with an annual return of r. Assume that your investments earn a return of r = 4%.
# 5. Assume your annual salary is annual_salary.
# 6. Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment. Call that portion_saved. This variable should be in 
#    decimal form.
# 7. At the end of each month your savings will be increased by the return on your investment plus a percentage of your monthly salary.
# Write a program to calculate how many months it will take you to save up enough money for a down payment. You will want your main variables to be floats so you 
# should cast user inputs to floats.


portion_downpayment = 0.25
current_savings = 0.00
r = 0.04
number_of_months = 1
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the portion of your salary saved, enter as a decimal:"))
total_cost = float(input("Enter the cost of your dream house:"))
monthly_salary = annual_salary/12
downpayment = portion_downpayment*total_cost
print(downpayment)
# As long as you don't have enough money saved up for the downpayment, a portion of your monthly salary as well as a return rate of 4% of your current savings will be 
# added to your savings each month.
while downpayment > current_savings:
    current_savings = current_savings + (monthly_salary*portion_saved) + current_savings*r/12
    number_of_months += 1
print(current_savings)
print("Number of months:", number_of_months - 1)
