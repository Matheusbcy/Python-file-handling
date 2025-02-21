from agenda import add_contact, delete_contact, view_contact


def main():
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Delete Contact")
        print("4. Exit")
        option = int(input("Choose an option: "))
        if option == 1:
            add_contact()
        elif option == 2:
            view_contact()
        elif option == 3:
            delete_contact()
        elif option == 4:
            break
        else:
            print("Invalid option")


main()
