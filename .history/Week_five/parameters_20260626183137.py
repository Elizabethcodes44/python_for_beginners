def add_nums(a,b,c,d,e):
    return a + b + c + d + e
add = add_nums(2,4,5,6,7)
print:(add)

#we use the * to unpack the items of the nums list
nums = [3,4,5,6,7]
print(*nums)
print(add_nums(*nums))

def add(x,y):
    return x + y
x = int(input("enter first number")) 
y = int(input("enter second number")) 
o = int(input("enter operator")) 

if "+" == o:
    result = add(x,y)