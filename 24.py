#args = parameters that pack all argument into tuple useful so that the function can accept varrying amount of argument

def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(add(1,3,4))