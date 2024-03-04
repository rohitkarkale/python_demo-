height=int(input(" What is your height in feet :"))
if height>3 :
    print(" You can ride ")
    age=int(input(" WHat is your age :"))
    if age<12 :
     bill=150
     print(' You ticket price is 150 rs.')
     photo=str(input(" do you want photo (Y/N) :"))
    if photo == 'y' or photo =='Y' :
     bill= bill+50
     print(f' Your total bill is {bill}rs')
else :
    print(" cant ride")
    print(" bye ")




