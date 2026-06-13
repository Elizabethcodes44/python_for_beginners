x = 1
 while x < 6: 
 print(x)
x += 1 ##this will increase x to avoid infinite loop

#break statement
y = 1
while y < 10:
 print(y)
 if y == 6:
  break
 y += 1


#continue statement
y = 1
while y < 10:
 y += 1
 if y == 4:
  continue
 print(y)


#Else statement

i = 1
while i < 6:
 print(i)
 i += 1
else:
 print("it is no longer less than 6")

 #calc
 while True:
  f_num = int(input("fırst number: "))
  s_num = int(input("second number"
        ))
  operator = input