# logical operator (and,or,not) = used to check if two or more condition statements are true or false
temp=int(input("What's the temprature today ?"))

if temp>=0 and temp<30:
    print("The temprature is good today !")
    print("You can go outside.")
elif temp<0 or temp>30:
    print("The temprature is not good today!")
    print("You can not go outside.")