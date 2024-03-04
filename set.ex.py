set1={'rohit','ram','rohan'}
set2={'satyam','shivam','rohit'}
set3={'satyam','ram'}
#print(set1.union(set2)) # or # print(set1 | set2)
#print(set1.intersection(set2,set3))
#print(set1 & set2)
#print(set1.difference(set2,set3)) #or print(set1-set2)
#set1.difference_update(set2)
#print(set1)
#print(set1.symmetric_difference(set2))
print(set1 ^ set2 ^ set3)