#Lambda
x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) 

def myfunc(n):
  return lambda a : a / n

divdoubler = myfunc(2)
divtripler = myfunc(3)

print(divdoubler(11))
print(divtripler(11))

#ex1
a = lambda y: y
print(a(9))