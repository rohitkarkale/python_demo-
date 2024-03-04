import os

path='folder'
try :
    os.remove(path)
    os.rmdir(path)

except FileNotFoundError:
    print("That file not found !")
except PermissionError :
    print("You do not have permission to delete that foolder ")

else :
    print("Your file deleted ")