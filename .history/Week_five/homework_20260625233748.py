#Homework for week 5

#importing date time library to get the current year 
from datetime import datetime

#A function that prints hello world
def hello_world():
    #printing hello world
    print("hello world")

#calling the function
hello_world()

# a function that prints username

def user_name():
    #use input to get username
    name = input("what is your name?: ")
    #print username
    print(f"your name is {name}")
#call the function
user_name()

#A function that prints numbers from 1 to ten

def print_numbers():

    #using for loop
    for x in range(1, 11):
       print (f"These are numbers 1 to 10 {x}")

#calling the function
print_numbers()

#function that prints all even numbers from 1 -20

def even_numbers():
    #using for loop and range 
    for x in range(1, 21):
        #using if statements to get even numbers
        if x % 2 == 0 :
            
            print(f"These are even numbers{x}")
#calling the functions
even_numbers()

#Write a function that prints the multiplication number of 5

def multiplication_number():

    #usıng for loop to determıne the numbers we are multıplyıng by 5 
    for x in range (1, 13):

        #now multıply each loop by 5 
        print(5, "x", x, "=", 5 * x)

multiplication_number()

#A function that prints sum of numbers from 1 to 50




#Write a function that prints whether a number (hardcoded inside the function) is even or odd.

def even_or_odd():
    #hardcoded number
    number = 2
    #using conditional statements 
    if number % 2 == 0:
        print()
        print(f"{number} is an even number")
    else:
        print()
        print(f"{number} is an odd number")
#calling the function
even_or_odd()


#Write a function that prints a simple pattern of stars (*).


#write a function that prints current year 

def current_year():
    #getting the current date time from the datetime library
    date= datetime.now()
    print()
    #printed the current date to check that it works
    print(date)
    #getting results for the current year
    print(f"this is the current year {date.year}")
    #calling the current_year function 
current_year()

#write a function that prints the square of numbers from 1 to 10.
def square_of_numbers():
    #looping through the numbers
    for x in range(1,11):
        print(x )


    



    
   