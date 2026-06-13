#1. Create a list of 6 random numbers. Using a for loop with range(len()), print each number with its index. Then print only numbers greater than 10.

#creating a list of six numbers

numbers = [10, 11, 1, 3, 5, 6]

#using a for loop withrange to print the index and each value

for index in range(len(numbers)) :
        print(f"{index}, {numbers[index]}")

#printing only numbers greater than 10

for number in numbers:
        if number > 10:
                print(f"number greater than 10: {number}")
        
       

#second homework Using range(), generate numbers from 1 to 50. Print only numbers that are divisible by 4 but  NOT divisible by 8.

#




    