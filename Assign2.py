"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

answer = str(input("Is one of the numbers a hypotenuse of a right triangle?: "))

if answer == "yes":
        n_max = max(n1, n2)
        n_min = min(n1, n2)
        A = ((n_max ** 2) - (n_min ** 2)) ** (1/2)
        A = round(A, 1)
        print(A)
elif answer == "no":
    C = ((n1 ** 2) + (n2 ** 2)) ** (1/2)
    C = round(C, 1)
    print(C)
