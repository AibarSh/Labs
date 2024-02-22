def squared_N(n):
    for i in range(1, n + 1):
        yield i ** 2

num = int(input("Enter the value of N: "))
squared = squared_N(num)
for x in squared:
    print(x)

print("------------------------")

def even_N(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

num = int(input("Enter the value of N: "))
even = even_N(num)
for x in even:
    print(x)

print("------------------------")

def divby3or4(n):
    for i in range(0, n+1):
        if i % 3 == 0:
            if i % 4 == 0:
                yield i

num = int(input("Enter the value: "))
div = divby3or4(num)
for x in div:
    print(x)

print("------------------------")

def squares(a,b):
    for i in range(a, b+1):
        yield i ** 2

num1 = int(input("Enter the value of N1: "))
num2 = int(input("Enter the value of N2: "))
squar = squares(num1, num2)
for x in squar:
    print(x)

print("------------------------")


def to_zero(a):
    o = a+1
    for i in range(a):
        o -= 1
        yield o
    
h = to_zero(15)
for x in h:
    print(x)
        



    
