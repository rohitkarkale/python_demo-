# str.format = optional method that gives users
#              more control when displaying output

animal="cow"
item="moon"

print("The "+animal ,"jumped over "+item)
print("The {} jumped over the {}".format(animal,item))
print("The {} jumped over the {}".format("moon","cow"))
print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))

text="The {} jumped over the {}"
print(text.format(animal,item))