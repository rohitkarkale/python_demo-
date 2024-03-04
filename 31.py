import os

source="text.text"
destination="C:\\Users\\rohit\\Desktop\\text.text"

try:
    if os.path.exists(destination):
        print("There is already file there.")
    else:
        os.replace(destination,source)
        print(source+"was removed")
except FileNotFoundError :
    print(source+"not found")
