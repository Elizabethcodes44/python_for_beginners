#1. Create a list of 6 random numbers. Using a for loop with range(len()), print each number with its index. Then print only numbers greater than 10.

#creating a list of six numbers

numbers = [10, 11, 1, 3, 5, 6]

#using a for loop withrange to print the index and each value

for index in range(len(numbers)) :
        print(f"{index}, {numbers[index]}")

#printing only numbers greater than 10

for number in numbers:
        if number > 10:
                print()
                print(f"number greater than 10: {number}")
        
       

#second homework Using range(), generate numbers from 1 to 50. Print only numbers that are divisible by 4 but  NOT divisible by 8.

#range 1 to 50

for i in range(1, 51):
        print()
        #printing numbers that are divisible by 4 but not divisble by 8 
        if i % 4 == 0 and not i % 8 == 0:
         print(f"numbers divisible by 4 and not divisble by 8: {i}")
         




    