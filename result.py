per=int(input(" Enter the percentage :"))

if per<35:
    print(f" you got {per}% and you are fail.")
elif per<=35 :
    print(f" you got {per}% you are pass.")
elif per<=60:
    print(f" you got {per}% you are in second class.")
elif per<=75:
    print(f" you got {per}% you are in first class.")
else :
    print(f" you got {per}% you are in distinction.")
    print(" Bye")