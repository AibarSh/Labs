#variables
x = 6
y = "Dereck"
print(x)
print(y)
x = str(4)    
y = int(4)    
z = float(4) 
print(type(x), type(y))
v = 'red' # same as "red"

print("----------------------------------")

#legal ver names:
myvar = "A"
my_var = "B"
_my_var = "C"
myVar = "D"
MYVAR = "E"
myvar2 = "F"

# illegal ver names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"'

myVariableName = "J" #camel case
MyVariableName = "F" #pascal case
my_variable_name = "K" #snake case

print("----------------------------------")

x, y, z = "O", 35, 54.6
print(x)
print(y)
print(z)
x = y = z = "O"
print(x)
print(y)
print(z)
cars = ["Van", "sedan", "suv"]
x, y, z = cars
print(x)
print(y)
print(z)

print("----------------------------------")

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)
a = 5
t = 6
print( a + t)

print("----------------------------------")

x = "70 Thousand"
def funky():
    global x
    x = 14000
    print( "Flying at",x, "feet")
funky()
print(x)

print("----------------------------------")

car_brand = "Volvo", "Mazda", "Toyota"
print(car_brand)