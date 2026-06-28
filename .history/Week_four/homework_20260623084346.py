#create a contact manager with dictionary

name = input("what is your name ? :")
phone_no = input("what is your phone number? :")

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