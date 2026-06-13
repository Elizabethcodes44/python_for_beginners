#use variables and if statements to determine what type of weather it is and decide weather a person should stay home , go outside , stay home or carry an umbrella . 

#variables
is_sunny = False
is_rainy = False
is_snowy = True
is_windy = True
if is_sunny:
    print("It's sunny outside. You can go outside and enjoy the weather!")
elif is_rainy:
    print("It's rainy outside. You should stay home or carry an umbrella if you go outside.")
elif is_snowy:  
    print("It's snowy outside. You should stay home or dress warmly if you go outside.")        
elif is_windy:
    print("It's windy outside. You should stay home or dress warmly if you go outside.")
elif is_sunny and is_rainy:
    print("It's sunny and rainy outside. You should stay home or carry an umbrella if you go outside.")
elif is_sunny and is_snowy:
    print("It's sunny and snowy outside. You should stay home or dress warmly if you go outside.")
elif is_sunny and is_windy and not is_rainy and not is_snowy:
    print("It's sunny and windy outside. You can go outside but dress warmly.")
else:
    print("The weather is clear. You can go outside and enjoy the day!")