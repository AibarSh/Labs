print(5 > 0)
print(10 == 10)
print(11 < 8) 

x = 20
y = 71

if y > x:
  print("b is greater than a")
else:
  print("b is not greater than a") 

print(bool("Bye"))
print(bool(33))

#False vars:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 

class class1():
  def __len__(self):
    return 0

obj = class1()
print(bool(obj))

def func():
  return True
print(func())

if func:
  print("Yes!")
else:
  print("NO?")

a = 200
print(isinstance(a,float))

print( 10 > 9)
#will be True
