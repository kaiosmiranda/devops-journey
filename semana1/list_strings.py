"""
Demonstrates basic list and string manipulations in Python.

This script performs two main tasks:
1. Checks for the presence of a user-inputted name within a predefined list of
   names and prints whether the name was found.
2. Takes a user-inputted sentence and performs several operations:
   - Counts the total number of letters (excluding spaces).
   - Counts the occurrences of the letter 'a' (case-insensitively).
   - Prints the entire sentence in uppercase.
"""

names = ["Kaio", "Kamilly", "Elaine", "Ana", "Adriano"]

x = input("Digite um nome: ")
# Deve se usar o in para percorrer uma lista
if x in names:
    print(x, "Está na lista")
else:
    print(x, "Não está na lista!")

y = input("Digite uma frase: ")
# Tira os espaços para contar 
nSpaces = y.replace(" ", "")

print("Quantidade de letras =", len(nSpaces))
# Move tudo para minusculo antes de contar
print("Quantidade de 'a' =", y.lower().count("a"))
print("Frase em maiúscula: ", y.upper())