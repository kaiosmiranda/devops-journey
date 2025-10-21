def total_calc(*price):
    return sum(price)

def show_request(client, *itens, **extra):
    print(f"\nRequest by {client}:")

    if itens:
        print("Itens:", ", ".join(itens))
    else:
        print("None item request")

    if extra:
        print("Extras:")
        for key, value in extra.items():
            print(f" - {key}: {value}")
    else:
        print("No extra")

def menu():
    client = input ("Type your name: ")
    itens = []
    extras = {}
    prices = []

    while True:
        print("\n--- Menu ---")
        print("1 - Add itens")
        print("2 - Add extra")
        print("3 - Calculate total")
        print("4 - Show request")
        print("5 - Out")

        option = input("Choose an option: ")

        if option == "1":
            item = input("Item name: ")
            price = float(input("Item price: "))
            itens.append(item)
            prices.append(price)
            print(f"{item} Added item with price {price}.")
        elif option == "2":
            key = input ("Extra item name (ex: drink, dessert): ")
            value = float(input("Item price: "))
            extras[key] = value
            print(f"Extra {key} = {value} added.")
        elif option == "3":
            print("Total: ", total_calc(*prices))   
        elif option == "4":
            show_request(client, *itens, **extras)
        elif option == "5":
            print("Going out...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    menu()