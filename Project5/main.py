
print("Welcome to Contact List")

contacts = {}
print("1-add:\n2-delete:\n3-Update:\n4-View:\n5-Search Contact\n6-Count Contact\n7-Exit:")
while True:
    # print("1-add:\n2-delete:\n3-Update:\n4-View:\n5-Search Contact\n6-Count Contact\n7-Exit:")
    choices = int(input("Enter your choice here: "))
    print(choices)
    if choices == 1:
        name = input("Enter contact name: ")
        if name in contacts:
            print(f"Contact name {name} is already exists!")
        else:
            age = input("Enter contact age: ")
            email = input("Enter contact email: ")
            num = input("Enter contact number: ")
            contacts[name] = {'age':int(age), 'email':email, 'num':num}
            print(f"Contact name {name} has been created successfully.")
            print(contacts)

    elif choices == 2:
        name = input("Enter contact name for delete: ")
        if name in contacts:
            del contacts[name]
            print(f"The contact {name} has been deleted successfully.")
        else:
            print("The Contact not found")

    elif choices == 3:
        name = input("Enter contact name for update: ")
        if name in contacts:
            email = input("Enter update email: ")
            num = input("Enter update number: ")
            contacts[name] = {'Name':name, 'Email':email, 'Num': num}
            print("Contact has been updated successfully..")
        else:
            print("Contact not found")

    elif choices == 4:
        name = input("Enter contact name to view: ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}\n Mobile_No: {num}\n Email: {email}")
        else:
            print("Contact no found")
    
    elif choices == 5:
        search_name = input("Enter contact name to search: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - \nName:{name}\nAge:{age}\nMobile Number:{num}\nEmail:{email}")
                found = True
        if not found:
            print("No contact found with that name")
    
    elif choices == 6:
        print(f"Total contact in your book is: {len(contacts)}")

    elif choices == 7:
        print("Good bye...")
        break
    
    else:
        print("Invalid input")
