#if True:
 #   print("yes! it was true.")
x=False
if x:
    print("yes! it was true.")
else:
    print("I will be printed in any case wherre {} is not true".format("x"))

loc = "Pune"
if loc=="Banglore":
    print("wlecome to banglore !")
elif loc == "Maharashtra":
    print("Welcome to Maharashtra")
else :
    print("where are you?")