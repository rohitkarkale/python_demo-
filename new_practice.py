a=int(input(" Enter the value of a :"))
b=int(input(" Enter the value of b :"))

c=input(" Enter the operand (+,-,*,/) :")

if c== '+' :
    sum=a+b
    print( f" The addition of above two values is :{sum}")
elif c== '-':
    sub=a-b
    print(f" The substraction of above two value is :{sub}")
elif c=='*':
    mul=a*b
    print(f" The multiplication of above two value is :{mul}")
elif c== '/':
    div=a/b
    print(f" The division of above two values is :{div}")

else :
    print(" You entered wrong operand.")
    print(" Bye")
