
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