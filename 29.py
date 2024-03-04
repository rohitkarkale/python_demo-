try :
    with open("test.tx") as file :
       print(file.read())

except FileNotFoundError :
    print("please write a correct file name.")



