#Create a list of fıve fruıts and prınt only the ones that are not apple.

#list of fruits
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
if fruits[0] == "apple":
    fruits.pop(0)
print(fruits)