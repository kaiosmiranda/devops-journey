"""
A simple command-line contact management system.

This script allows users to manage a list of contacts by providing a menu-driven
interface. Users can add new contacts, list existing contacts, search for
specific contacts by name, and exit the application. The contact information is
stored in memory and will be lost when the program exits.
"""

contacts = []

while True:
    print("Menu")
    print("1 - Adicionar aos contatos")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Sair")

    options = ["1", "2", "3", "4"]
    x = input("Opção: ")

    if x in options:
        if x == "1":
            name = input("Digite o nome: ").strip()
            phone = input("Digite o número: ").strip()
            contacts.append({"name": name, "phone": phone})
            print("Contato adicionado!")
        elif x == "2":
            if contacts:
                print("\nContatos cadastrados:")
                for contact in contacts:
                    print(f"Nome: {contact['name']}, Número: {contact['phone']}")
            else:
                print("Nenhum contato cadastrado!")
        elif x == "3":
            term = input("Buscar por nome: ").strip().lower()
            found = False
            for z in contacts:
                if term in z["name"].lower():
                    print(f"Encontrado: {z['name']} - {z['phone']}")
                    found = True
                if not found:
                    print("Nenhum contato encontrado!")
        elif x == "4":
            print("Saindo da agenda...")
            break
    else:
        print("Opção indisponível")