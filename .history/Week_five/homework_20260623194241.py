#Homework for week 5

#A function that prints hello world
def hello_world():
    #printing hello world
    print("hello world")

#calling the function
hello_world()

# a function that prints username

def user_name(name):
    #I gave ıt a name parameter so ı can use an input 
    print(f"your name is {name}")
#declaring the input 
user_name(input("what is your name ?:"))

#A function that prints numbers from 1 to ten

def print_numbers():

    #using for loop
    for x in range(1, 11):
       print (x)

#calling the function
print_numbers()

#function that prints all even numbers from 1 -20

def even_numbers():
    for x in range(1, 21):
        if x % 2 == 0 :
            print(x)
even_numbers

    
   