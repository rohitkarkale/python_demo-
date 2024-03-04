# Higher order function = Function that either
#                        1) accept a function as an argument or return function

def loud(text):
    return text.upper()

def quit(text):
    return text.lower()

def hello(func):
    text=func("rohit")
    print(text)

hello(loud)
hello(quit)
