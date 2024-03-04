# Set = collection which is unordered, unindexed, and no duplicate value

utensile = {"fork","knife","spoon"}
dishes={"cup","bowl","plate"}
#utensile.add("chaku")
#print(utensile.remove("spoon"))
utensile.update(dishes)
print(dishes.difference(utensile))
#for x in dishes :
 #   print(x)