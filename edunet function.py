#def say_hello():
   # print("Hello Rohit")
#say_hello()
def check_even_list(num_list):
    even_number=[]
    for number in num_list:
        if number%2==0:
            even_number.append(number)
        else:
            pass
    print( even_number)

check_even_list([1,2,3,4,5,6])