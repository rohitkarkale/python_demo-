weight=float(input(" Enter the weight :"))
height=float(input(" Enter the height :"))

bmi=round(weight/height**2)

if bmi<18.5:
    print(f" Your weight is {bmi} and you are underweight.")
elif bmi<25.:
    print(f" Your weight is {bmi} and you are normal weight. ")
elif bmi<30:
    print(f" Your weight is {bmi} and you are overweight.")
elif bmi<35:
    print(f" your weight is {bmi} and you are obese.")
else :
    print(f" Your weight is {bmi} and you are clinically obese.")