# Dictionart = A changable unordered collection of unique key value pairs fast because thery are hashing, allow to access
# value quickly

capitals ={"USA":"washington dc",
           "India":"New delhi",
            "china":"beijing "}

print(capitals["India"])
print(capitals.get("japan"))
print(capitals.keys())
print(capitals.items())
capitals.update({"Germany":"Berlin"})
capitals.pop("china")
capitals.clear()
for key,value in capitals.items():
    print(key,value)