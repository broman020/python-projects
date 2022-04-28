# LAB: WORKING WITH LISTS
# Write a program that asks the user to enter 10 (positive) integers. The program should then print the numbers in sorted order from biggest to smallest.
# To do this, first write a function that takes a list and finds the largest element. It then 1) deletes that element from the list and 2) returns that element.


num_list = []
# This loop allows user to enter up to 10 values and checks if they are positive. If not they are told only to enter positive integers.
for i in range(10):
    while True:
        # User will enter a total of 10 numbers one at a time
        positive_num = int(input("Enter a positive integer:"))
        # Only those integers that are positive will be added to the list
        if positive_num >= 0:
            num_list.append(positive_num)
            break
        else:
            # If a value is negative, user will be told to enter a positive integer.
            print("Values entered must be POSTITIVE INTEGERS")

# This loop ensures values entered are positive integers then proceeds to print the biggest number and remove it from the list to simulate it has been chosen.
while True:
    if all(x >= 0 for x in num_list) == True and all(isinstance(x, int) for x in num_list) == True:
        while len(num_list) > 0:
            print(max(num_list))
            num_list.remove(max(num_list))
            break
    else:
        print("Values entered must be POSITIVE INTEGERS!")

