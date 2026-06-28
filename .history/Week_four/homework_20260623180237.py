#create a contact manager with dictionary
contact_manager = {}

user_input = input("Do you want to save or delete contact ? :")
if user_input == "save":
    name = input("what is your name ?:")
    if name in contact_manager:
        print("user already exist")
    else :
        phone_no = input("what is your phone number? :")
        address = input("add your address:")

        name = input("what is your name ? :")

elif user_input == "delete":
    del_contact = "what is the name of the user you want to delete ?"
    if del_contact in contact_manager:
        del contact_manager


contact_manager = {"username": name , "phone_number": phone_no , "user_address": address}


print(contact_manager)

#keys output
for x in contact_manager :
    print(x)


for x in contact_manager:
    print(contact_manager[x])


#now gettıng both keys and values using enumerate

for x, y in enumerate(contact_manager):
    print("key:", y)
    print("value:", (contact_manager[y]))