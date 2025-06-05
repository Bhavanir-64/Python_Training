import number as n
contacts = {}
while True:
    try:
        print("Choices :")
        print("1.Add contact")
        print("2.View all contacts")
        print("3.Delete contact")
        print("4.Find contact")
        print("5.Edit contact")
        print("6.Exit")
        choice = int(input("Enter choice : "))
        if choice == 1:
            n.add_contact(contacts)
        elif choice == 2:
            n.view_contacts(contacts)
            #file=open('day6/data.txt','r+')
            #x=file.write()
            #print(x)
        elif choice == 3:
            n.delete_contact(contacts)
        elif choice == 4:
            n.find_contact(contacts)
        elif choice == 5:
            n.edit_contact(contacts)
        else:
            break
    except:
        print('An error is occured')
    finally:
        print('*****Contacts App*****')