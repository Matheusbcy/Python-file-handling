import os


def add_contact():
    name = input("Enter the name of the contact:\n ")
    address = input("Enter the address of the contact:\n ")
    phone = input("Enter the phone number of the contact:\n ")

    contact = f"Nome: {name}\nEndereço: {address}\nTelefone: {phone}\n"

    with open("dados/contatos.txt", "a", encoding="UTF-8") as file:
        file.write(contact)


def view_contact():
    if not os.path.exists("dados/contatos.txt"):
        print("Lista de contatos esta vazia")
        return
    with open("dados/contatos.txt", "r", encoding="UTF-8") as file:
        contacts = file.read()

    print("Lista de contatos")
    print(contacts)
    
def delete_contact():
    if not os.path.exists("dados/contatos.txt"):
        print("Lista de contatos esta vazia")
        return
    with open("dados/contatos.txt", "w", encoding="UTF-8") as file:
        file.write("")
        