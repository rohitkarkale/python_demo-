size=input(" What size of pizza you want (S/M/L) :")
if size == 's' or size == 'S':
    bill = 100
    pepporoni = input(" do you want pepporoni on pizzza (Y/N)?")
    if pepporoni=='y' or pepporoni=='Y':
        bill=bill+40
        cheese=input(" do you want cheese on pizza (Y/N) ?")
    if cheese=='y' or cheese=='Y':
        bill=bill+20
        print(f" your total bill is {bill}")
    else :
        print(f" your total bill is {bill}")