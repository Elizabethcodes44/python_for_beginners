#decision based 
#atm withdrawal decision
balance = 5000
withdraw = 3000
if withdraw <= balance:
    print("transaction successful")
else:
    print("insufficient balance")

#login logic
password ="admin12345"
password_input = input("what is your password?")

if password_input == password :
    print( "you have access" )
else:
    print("Access Denied")