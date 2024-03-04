#scope = The region that a variable is recognized
#        A variable is only available from inside the region it is created.
#        A global and locally scoped versions of a variable can be created
name="Rohit"  #global scope (available inside and outside )
def display_name():
    name="Karkale"   #local scope (available only inside )
    print(name)
display_name()
print(name)