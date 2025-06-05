def add_contact(contacts):
    name = input("Enter Contact Name :")
    mobile = int(input("Enter mobile number :"))
    contacts[name] = mobile
    file=open('day6/data.txt','a')
    file.write(f'{name}-{mobile}\n')

def view_contacts(contacts):
    for contact in contacts:
        file=open('day6/data.txt','r')
        file.readlines()
        name, mobile = contact.split(",")
        print(f"Name: {name}, Phone: {mobile}")

def delete_contact(contacts):
    name_to_delete = input("Enter contact name to delete :")
    del contacts[name_to_delete]
    print("deleted contact " , name_to_delete)
    file=open('day6/data.txt','a')
    file.write(f'{name_to_delete}\n')

def find_contact(contacts):
    name = input("Enter name to search : ")
    found = False
    for i in contacts:
        if name in i:
            print(f"{i} => {contacts[i]}")
            found = True
    if not found:
        print("contact is not Found!!!")
    file=open('day6/data.txt','a')
    file.write(f'{name}\n')

def edit_contact(contacts):
    name_to_edit = input("Enter contact name to edit :")
    number = int(input("Enter new number: "))
    contacts[name_to_edit] = number
    print(name_to_edit)
    file=open('day6/data.txt','a')
    file.write(f'{number}\n')