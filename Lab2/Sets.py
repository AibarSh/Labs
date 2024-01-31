thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print(type(thisset))

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) 

print("banana" in thisset) 

thisset.add("orange")
print(thisset) 

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) 

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) 

thisset.remove("banana")
thisset.discard("orange")
# .pop removes a random item
print(thisset) 

thisset.clear()
del thisset

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) # update is the same
print(set3) 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
x.intersection_update(y)
print(z) 
print(x) 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
x.symmetric_difference_update(y)
print(z) 
print(x)