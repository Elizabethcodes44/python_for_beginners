#first homework for week 2
#Smart security system
#Create a smart security system that checks if the user has the keycard,correct password and grants access to admin  accordingly.

#variables
has_keycard = True
password = False
is_admin = False
if (has_keycard and password) or is_admin:
    print("Access granted")
else:
    print("Access denied")
    
#exploring user input with the same security system
keycard = input("Do you have the keycard? (yes/no): ")
password_input = input("Enter the password: ")
is_admin_input = input("Are you an admin? (yes/no): ")

if (keycard == "yes" and password_input == "admin123" ) or is_admin_input == "yes":
    print("Access granted")
else:   print("Access denied")
    
    