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

#Exercice 1: Écrivez un programme qui demande à l’utilisateur son nom et affiche un message de salutation.

name = input("What is your name? :")
print("My name is", name)

#Exercice 2: Écrivez un programme qui calcule et affiche la somme de deux nombres saisis par l’utilisateur. ( Vous pouvez gérer les erreurs si vous souhaitez)

number_1 = float(input("choose number:"))
number_2 = float(input("choose number:"))

Total = number_1 * number_2

print("The total is",Total,"!")

#Exercice 3: Écrivez un programme qui affiche les nombres de 1 à 10 en utilisant une boucle.

for i in range(1,11):
    print(i)

#Exercice 4: Écrivez un programme qui demande à l’utilisateur son âge et détermine s’il est majeur ou mineur.

age = float(input("What is your age?: "))

if age < 18:
    print(f"Your age is {age}, so you are a minor")
else:
    print(f"Your age is {age}, so you are an adult")

#Exercices 5: Écrivez un programme qui vérifie si un nombre saisi par l’utilisateur est positif, nul ou négatif.

number = float(input("The number: "))

if number < 0:
    print(f"The number{number} is negative")
elif number > 0:
    print(f"The number{number} is positive")
else:
    print(f"The number is {number}")

#Exercices 6: Écrivez un programme qui calcule et affiche la moyenne de trois nombres saisis par l’utilisateur.

num_1 = float(input("The number 1: "))
num_2 = float(input("The number 2: "))
num_3 = float(input("The number 3: "))

Tot = (num_1 + num_2 + num_3) / 3

print(Tot)

#Exercice 7: Écrivez un programme qui demande à l’utilisateur un rayon et calcule la circonférence d’un cercle. Vous pouvez importer une bibliothèque si vous désirez.

import math
radian = float(input("What is the radian?: "))

Perimeter = 2 * math.pi * radian

print(Perimeter)

#Exercice 8: Écrivez un programme qui affiche les premiers n termes de la table de multiplication d’un nombre saisi par l’utilisateur.

n =int(input("le nombre:"))
i = 0
while i < 12:
    i+=1
    P = n * i
    print(f"{n} X {i} = {P}")

# Exercice 9: Écrivez un programme qui demande à l’utilisateur une année et détermine si elle est bissextile.

A = int(input("Year: "))

if A in range (1000, 3000, 100):
    if A % 4 == 0 and A % 400 == 0:
        print(f"the year {A} is a leap year ")
    else:
        print(f"the year {A} is not a leap year")
else:
    if A % 4 == 0:
        print(f"the year {A} is a leap year ")
    else:
        print(f"the year {A} is not a leap year")

#Exercice 10: Écrivez un programme qui demande à l’utilisateur un nombre et affiche s’il est pair ou impair.

B = int(input("Number: "))

if B != 0 and B % 2 == 0:
    print(f"{B} is even")
elif B == 0:
    print("B equal 0")
elif B <= 0:
    print("B is negative")
else:
    print(f"{B} is odd")

#Exercice 11: Écrivez un programme qui demande à l’utilisateur un mot et affiche le mot inversé.

B = input("Word: ")

T = B[::-1]

print(T)

#Exercice 12: Écrivez un programme qui génère un nombre aléatoire entre 1 et 100,
# puis demande à l’utilisateur de deviner ce nombre. Le programme doit donner des
# indices si la devinette est trop élevée ou trop basse.

import random

C = random.randint(1,101)
Guess = 0
limit = 2

while Guess <= limit:
    D = int(input("Guess: "))
    if D != C:
        Guess += 1
        if D < C:
            print("Your guess is low")
        elif D > C:
                print("Your guess is high")
        else:
            print("Your guess is right")
    else:
        print(f"Congratulations, the guess is actually {C}")
else:
    print("Done")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
