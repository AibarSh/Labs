def my_function(money):
  for x in money:
    print(x)

Currency = ["tenge", "us_dollar", "euro"]
my_function(Currency)

def Empty_func():
    pass

def my_function(x, /): # Positional-Only Arguments
  print(x)

my_function(3) # x = 3 is an error

def my_function(*, x): # Keyword-Only Arguments
  print(x)

my_function(x = 3) # 3 is an error

def my_function(a, b, /, *, c, d): # combining
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8) 

def fibonacci(var1):
  if var1 <= 1: return var1
  else: return fibonacci(var1-1) + fibonacci(var1-2)
print(fibonacci(8))