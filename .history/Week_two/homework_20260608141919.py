#Create a list of fıve fruıts and prınt only the ones that are not apple.

#list of fruits
fruits = ["apple", "banana", "orange", "grape", "kiwi"]

#looping through the list of fruits and printing only the ones that are not apple
for fruit in fruits:
    if fruit != "apple":
        print(fruit)


#assıgnment 2:Loop through a list of drinks and print I love this drink when the item is juice 

#list of drinks
drinks = ["water", "juice", "soda", "tea", "coffee"]

#looping through the list of drinks and printing I love this drink when the item is juice
for drink in drinks:
    if drink == "juice":
        print("I love this drink")

#create a string with your favorite word and print each letter on a new line using a for loop and modify it to skip a letter and print the rest of the letters on a new line

#string with favorite word
favorite_word = "Python"
for letter in favorite_word:
    print(letter)

#modifying the loop to skip a letter and print the rest of the letters on a new line
for Letter in favorite_word:
    if Letter == "o":
        continue
    print(Letter)

#assignment 5: write a loop that prints numbers from 5 to 15

for number in range(5,16):
    print(number)

#assignment 6: print only numbers divisible by 3 between 1 to 30

#looping through the numbers from 1 to 30 and printing only the ones that are divisible by 3

for number in range(1,31):
    if number % 3 == 0:
        print(f"\n{number}")

#assignment 7:create a list of name and print only the names with more than 4 characters

#list of names
names = ["Anna", "Bob", "Charlie", "David", "Eve"]
#looping through the list of names and printing only the ones with more than 4 characters
for name in names:
    if len(name) > 4:
        print(f"list of names with more than 4 characters: {name}")

#assignment 8: loop through a word and count how many tımes the letter "o" appears in the word

#string with a word
word ="book"

#looping through the word and counting how many times the letter "o" appears in the word
count = 0


