total = 0
count = 0

num = int(input("Type a number to total: "))
while num != 0:
    total = total + num # Tem duas opções para somar, tanto essa como a de baixo.
    count += 1     # Assim quando precisar somar um número a ele, basta ultilizar a de cima ou a de baixo

    num = int(input("Type a number to total: "))

if count > 0:
    average = total / count

    print("Total = ", total)
    print("Average = ", average)
else:
    print("Invalid number")
#





