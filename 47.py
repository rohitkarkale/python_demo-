# lambda = function written in 1 line using lambda keyword
#          lambda parameter : expression

#def double(x):
#    return x * 2
#print(double(4))

double= lambda x: x*5
print(double(7))
multiply = lambda x,y : x*y
print(multiply(2,3))
division = lambda x,y : x/y
print(division(10,2))
add = lambda x,y,z : x+y+z
print(add(3,4,5))
full_name = lambda first_name,middle_name,last_name : first_name+middle_name+last_name
print(full_name("Rohit ","Revansiddh ","Karkale"))
age = lambda age :True if age>=18 else False
print(age(1))