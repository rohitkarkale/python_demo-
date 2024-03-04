pin = 123
ids = "viit"

user_id=input("Enter your used_id")
if user_id==ids:
    user_pin=int(input("Enter your atm pin"))
    if user_pin==pin:
        print("welcome,access granted")
    else :
        print("Wrong pin, try again!")
else :
    print("user not found!")




