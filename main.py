# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(Fabrice):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {Fabrice}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if 'Fabrice'!= __name__ :
    print_hi('PyCharm')
else:
    pass
#150 exercices

#Exercice 1

name = input("What is your name? :")
print("My name is", name)

#Exercice 2

number_1 = float(input("choose number:"))
number_2 = float(input("choose number:"))

Total = number_1 * number_2

print("The total is",Total,"!")

#Exercice 3
for i in range(1,11):
    print(i)

#Exercice 4
age = float(input("What is your age?: "))

if age < 18:
    print(f"Your age is {age}, so you are a minor")
else:
    print(f"Your age is {age}, so you are an adult")

#Exercices 5
number = float(input("The number: "))

if number < 0:
    print(f"The number{number} is negative")
elif number > 0:
    print(f"The number{number} is positive")
else:
    print(f"The number is {number}")

#Exercices 6
num_1 = float(input("The number 1: "))
num_2 = float(input("The number 2: "))
num_3 = float(input("The number 3: "))

Tot = (num_1 + num_2 + num_3) / 3

print(Tot)

#Exercice 7:
import math
radian = float(input("What is the radian?: "))

Perimeter = 2 * math.pi * radian

print(Perimeter)

#Exercice 8

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
