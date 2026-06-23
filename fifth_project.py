with open("contacts.txt","a"):
    contacts=[]
    print("This is a contact saving website")
    print("We give features like add contact, search contact , delete contact ,view contacts ,exit")
    print("1. add contact")
    print("2. search contact")
    print("3. delete contact")
    print("4. view contacts")
    print("5. exit")
    while True:
        a=int(input("Enter your choice:    "))
        if a==1:
            name=[]
            b=input("Enter the name of the contact:   ")
            name.append(b)
            c=int(input("Enter the phone number:    "))
            name.append(c)
            contacts.append(name)
        elif a==2:
            d=input("Enter the contact you want to enter:    ")
            for i in contacts:
                if d in i[0]:
                    print(f"The contact of {i[0]} is found his number is {i[1]}")
                    break
            else:
                print("The contact is not found")
        elif a==3:
            e=input("enter the contact you want to delete:     ")
            for i in contacts:
                if e in i[0]:
                    contacts.remove(i)
                    print("The contact is deleted successfully!")
                    break
            else:
                print(f"The contact {e} is not found")
        elif a==4:
            for i in contacts:
                print(i)
        else:
            break