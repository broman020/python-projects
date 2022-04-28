# LAB: WORKING WITH LISTS
# Write a program where the user can enter each of his grades after which the program prints out a report card with GPA. 
# Remember to ask the user how many classes he took.


number_of_classes = int(input("How many classes did you take?"))
classes_list = []
grades_list = []
i = 0
# This loop asks for the name of the class and checks if a string was entered. If so, asks for the grade received in that class (only positive numbers can be entered).
while i < number_of_classes:
    while True:
        name_of_class = str(input("What was the name of the class?"))
        if isinstance(name_of_class, str) == True:
            classes_list.append(name_of_class)
            break
        else:
            print("You can only enter names of classes")


    while True:
        grade_of_class = int(input("What whas your grade in that class?"))
        if isinstance(grade_of_class, int) == True and grade_of_class > 0:
            grades_list.append(grade_of_class)
            break
        else:
            print("Input a valid grade value")

    i += 1

print("REPORT CARD")
# This loop prints the class followed by the grade (grades is a string so that it can be joined with the name of the class as they must be of the same type).
# The average of the classes is then calculated and printed.
for x in range(number_of_classes):
    print(classes_list[x] + " - " + str(grades_list[x]))

avg_gpa = sum(grades_list)/number_of_classes
print("Average GPA is " + str(round(avg_gpa,2)))

