height=int(input(" Enter the height in feet :"))
if height>3:
    print("You can ride")
    age=int(input(" What is your age :"))
    if age<12:
     print(" Pay 150 rs.")
    elif age<=18:
      print("pay 200 rs.")
    else :
     print(" pay 500 rs.")
else :
    print(" you can't ride")