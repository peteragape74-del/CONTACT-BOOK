#contact book python code
contacts = []

while True:
    print('CONTACT BOOK')
    print('1. Add contact')
    print('2. View contacts')
    print('3. Delete contact')
    print('4. Exit')

    choice = input("Choose an option: ")
    if choice == '1':
        contact = input("Enter contact number: ")
        contact_name = input("Enter contact name: ")
        contacts.append({'Name': contact_name, "phone number": contact})
        print("Contact added.")

    elif choice == '2':
        if not contacts:
            print('Contact book is empty.')
        else:
            print('Contacts:')
            for index, saved_contact in enumerate(contacts, start=1):
                print(f"{index}. {saved_contact['Name']} - {saved_contact['phone number']}")

    elif choice == '3':
        if not contacts:
            print('Contact book is empty.')
        else:
            print('Contacts:')
            for index, saved_contact in enumerate(contacts, start=1):
                print(f"{index}. {saved_contact['Name']} - {saved_contact['phone number']}")

            contact_number = input('Enter the number of the contact to delete: ')
            if contact_number.isdigit() and 1 <= int(contact_number) <= len(contacts):
                deleted_contact = contacts.pop(int(contact_number) - 1)
                print(f"Deleted {deleted_contact['Name']}.")
            else:
                print('Invalid contact number.')

    elif choice == '4':
        print('Goodbye.')
        break

    else:
       print('Invalid option.')
