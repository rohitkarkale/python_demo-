#if statements = the block of code execute only if condition is true

age=int(input("What is your age ?"))

if age<0:
    print("You have not born yet !")
elif age==100:
    print("You are a century old !")
elif age>=18:
    print("You are an adult now !")
else:
    print("You are child !")