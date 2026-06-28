#create a contact manager with dictionary

contact_manager = {"name":"Oluwatosin" , "phone_number": "+23489900000", "address" : "Ijebu Igbo"}

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