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

#Exercice 13: Écrivez un programme qui calcule et affiche les premiers n termes de la suite de Fibonacci.

n = int(input("number: "))
a=0
b=1
for i in range(n):
    a,b = b,a + b
    print(a,)

#Exercice 14: Écrivez un programme qui demande à l’utilisateur une chaîne de caractères et compte le nombre de voyelles dans cette chaîne.

r = input("Str: ")
voyelles = "eyioaEIOYA"
count = 1
for c in r:
    if c in voyelles:
        count+=1
print(count)

#Exercice 15: Écrivez un programme qui vérifie si une chaîne de caractères est un palindrome (elle se lit de la même manière de gauche à droite et de droite à gauche).

A = input("Str: ")
B = A[::-1]

if A == B:
    print("the words is a palindrome")
else:
    print("the words is not a palindrome")

#Exercice 16: Écrivez un programme qui affiche tous les nombres premiers entre 1 et 100.

def is_number(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
for number in range(1,101):
    if is_number(number):
        print(number, end=" ")

#Exercice 17: Écrivez un programme qui demande à l’utilisateur une phrase et compte le nombre de mots dans cette phrase.

A = input("the sentence: ")

B = A.split()

print(len(B))

#Exercice 18: Écrivez un programme qui génère un triangle de nombres comme suit

n = int(input("the number: "))
for i in range(1,n):
    for u in range(1,i):
        print(u, end="")
    print(i)

#Exercice 19: Écrivez un programme qui demande à l’utilisateur une liste de nombres et affiche la somme de ces nombres.

def somme(u):
    _u = 0
    for i in u:
        _u += i
    print(_u)

u = []

for i in range(3):
    o = int(input("number: "))
    u.append(o)
print(u)

print(somme(u))

#Exercice 20: Écrivez un programme qui demande à l’utilisateur une série de nombres et affiche le plus grand nombre saisi.

List = []
Limit_of_number = int(input("Limit: "))
set=0
for i in range(Limit_of_number):
    The_number = int(input("Please, enter a number: "))
    b.append(The_number)
    set+=1
print(List)

Max_list = max(List)

print(Max_list)

#Exercice 21: Écrivez un programme qui affiche les premiers n termes de la séquence de puissances de 2: 1,2,4,8,16,...

Index = int(input("num: "))

for i in range(Index):
    Suit = 2 ** i
    i+=1
    print(Suit)

#Exercice 22: Écrivez un programme qui demande à l’utilisateur une liste de nombres et affiche le plus petit nombre saisi.

List = []

for i in range(3):
    number = float(input("Give a number: "))
    List.append(number)
    i+=1
print(List)

Min_List = min(List)

print(Min_List)

#Exercice 23: Écrivez un programme qui affiche la table de multiplication de tous les nombres de 1 a 10

for i in range(1,11):
    for u in range(13):
        p = i * u
        print(f"{i} X {u} = {p}")
        u += 1
    print()

#Exercice 24: Écrivez un programme qui demande à l’utilisateur une liste de mots et affiche le mot le plus long saisi.

List = []

number_words = int(input("Number: "))

for i in range(number_words):
    words = input("the words: ")
    List.append(words)
    i+=1
print(List)

max_list = float("-inf")
for o in List:
    if len(o) > max_list:
        max_list = len(o)
        T = o
print(T)

#Exercice 25: Écrivez un programme qui demande à l’utilisateur une liste de nombres et affiche la moyenne de ces nombres.

List_number = input("Numbers: ")
u = List_number.split()
e = 0
for s in u:
    p = float(s)
    e = e + p
print(e / len(u))

#Exercice 26: Écrivez un programme qui demande à l’utilisateur un nombre et affiche la table de multiplication pour ce nombre de 1 à 10.

number = int(input("the number: "))
print(f"Multiplication table of {number} is:")
for i in range(11):
    p = number * i
    print(f"{number} X {i} = {p}")
    i += 1
print()

#Exercice 27: Écrivez un programme qui demande à l’utilisateur une phrase et affiche le nombre de mots dans cette phrase

Sentence = input("the sentence: ")

words = Sentence.split()

print(len(words))

#Exercice 28: Écrivez un programme qui génère un carré de nombres comme suit: 12345 12345 12345

Numbers = int(input("Num: "))
for k in range(1, Numbers + 1):
    for i in range(1, Numbers + 1):
        print(i, end="")
    print()

#Exercice 29: Écrivez un programme qui demande à l’utilisateur un nombre et affiche s’il est premier ou non. Utilise def pour utiliser une function.

def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number <= 5:
        return True
    elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
        return False


number = int(input("The number: "))

if is_prime(number):
    print(f"the number {number} is a prime number")
else:
    print(f"the number {number} is a not prime number")


#Exercice 30: Écrivez un programme qui vérifie si une chaîne de caractères est un pangramme (contient toutes les lettres de l’alphabet au moins une fois).

chain = input("chain: ")

letters = "qwertyuiopasdfghjklzxcvbnm"

limit = 0
Count = True

for letter in letters:
    if letter in chain and len(chain) >= len(letters):
        continue
    elif not letter in chain or len(chain) > len(letters):
        print(f"the letter {letter} is not in the chain or the chain is short")
    elif not letter in chain or len(chain) < len(letters):
        print(f"the letter {letter} is not in the chain")
    limit+=1
print("Pangramme")





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
