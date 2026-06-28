names = ["lizzy", "dapo", "michael"]

for name in names :
    print(name)

names.append("John")
print(names)

names.insert(3, "Michael")

print(names)

#accessing a particualr item item ın python

print(names[3])

second_names = [
    "John",
    "Mary",
    "David",
    "Sarah",
    "Michael",
    "Jessica",
    "Daniel",
    "Ashley",
    "James",
    "Emily",
    "Christopher",
    "Olivia",
    "Matthew",
    "Sophia",
    "Andrew",
    "Isabella",
    "Joseph",
    "Mia",
    "Joshua",
    "Charlotte"
]

#to print a range or a set ına lıst use thıs
print(names[:5]) #this will list the fırst fıve ındex on the list
print(names[4:]) #this will list from index 4 to the end 
print(names[7 : 8]) #this will print from index 7 to 8

#removing item using pop
names.pop(1) #this could also be a string 