#parent class
class person(object):

    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("My idnumber is {} ".format(self.idnumber))

#child class

class Emplyee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary = salary
        self.post =post

        person.__init__(self,name,idnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("idnumber is {}".format(self.idnumber))
        print("post :{}".format(self.post))


a=Emplyee("Rohit",88456,200000,"Intern")

a.display()
a.details()

