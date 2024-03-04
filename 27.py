try :
    numerator=int(input("Enter any numerator : "))
    denominator=int(input("Enter any denominator : "))
    result=numerator / denominator
    print(result)
except ZeroDivisionError as e  :
    print(e)
    print("You can not divide by zero idiot !")
except ValueError as e :
    print(e)
    print("You can only divide by number ")
except Exception :
    print("something went wrong :(")
finally :
    print("This will execute everytime")