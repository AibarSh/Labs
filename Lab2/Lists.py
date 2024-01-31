#Lists
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))
list1 = ["abc", 34, True, 40, "male"]
#<class 'list'> 
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
anotherlist = list(("apple", "banana", "cherry", "apple", "cherry"))

print("---------------------------------------------")
# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
#     List is a collection which is ordered and changeable. Allows duplicate members.
#     Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#     Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#     Dictionary is a collection which is ordered** and changeable. No duplicate members.

print("---------------------------------------------")

#List accesses
print(thislist[1]) # first item
print(thislist[-1]) # last item, -2 second last item
print(thislist[2:5]) # range
print(thislist[:4])
print(thislist[3:])
print(thislist[-4:-1])

print("---------------------------------------------")

#List item change
thislist[0] = "blackcurrant"
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 
thislist[1:3] = ["watermelon"]
print(thislist) 

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "pineapple")
print(thislist)

print("---------------------------------------------")

#Add items to the list

thislist2 = ["car","bus","truck"]
thislist2.append("motorcycle")
print(thislist2)
thislist2.insert(1, "plane")
print(thislist2)
objects = ["Cone", "Barrier", "Board"]
thislist2.extend(objects)
print(thislist2)
thistuple = ("Gnome", "Lawn", "Hose")
thislist2 = ["car","bus","truck"]
thislist2.extend(thistuple)
print(thislist2)

print("---------------------------------------------")

#remove list items

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

print("---------------------------------------------")

#Loop lists

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

for i in range(len(thislist)):
  print(thislist[i]) 

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

[print(x) for x in thislist] 

print("---------------------------------------------")

#List comprehension

metals = ["Iron", "Vismut", "Aluminium", "Steel", "Copper"]
newlist = []
for x in metals:
  if "m" in x:
    newlist.append(x)
print(newlist) 

newlist = [x for x in metals if x != "Copper"] 
print(newlist) 

newlist = [x for x in range(10) if x < 5] 

newlist = [x if x != "Iron" else "Magnesium" for x in metals] 
newlist = [x.lower() for x in metals] 
print(newlist)

print("---------------------------------------------")

#List sort
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

print("---------------------------------------------")

#List copy

lis = ['o','p','i','u','m']
lis2 = list(lis) 
print(lis2)

print("---------------------------------------------")

#List merge

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)

# for x in list2:
#   list1.append(x)

# list3 = list1 + list2

print(list1) 