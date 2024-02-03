#Lecture task: functions

def calculate_factorial(var1):
    if var1 == 1: return var1
    else: return var1 * calculate_factorial(var1 -1)
print(calculate_factorial(5))


def reverse_string(st1):
    return st1[::-1]
print(reverse_string("Good day World"))


def get_max(var1, var2, var3):
    tpl = (var1, var2, var3)
    return max(tpl)
print(get_max(5, -9, 100))


def is_even(var1):
    if var1 % 2 == 0: return True
    else: return False
print(is_even(7))


def filter_prime(var1):
    list2 = []
    for x in var1:
        if x == 1 or x == 2: 
            list2.append(x)
            continue
        for i in range(2, x):
            if x % i == 0: break
            list2.append(x)
            break
    return list2
    
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(filter_prime(list1))


def find_common_elements(l1, l2):
    s = set(l1).intersection(set(l2))
    l3 = list(s)
    return l3
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [-2, 0, 2, 4, 6, 8, 10, 12, 14, 16]
print(find_common_elements(list1, list2))


def word_frequency(str):
    words = str.split()
    dict = {}
    for word in words:
        cleaned_word = word.strip('.,?!').lower() 
        dict[cleaned_word] = dict.get(cleaned_word, 0) + 1
    return dict
txt = "Python is a popular programming language. Python can be used on a server to create web applications."
print(word_frequency(txt))


def fibonac(var1):
    if var1 <= 1: return var1
    else: return fibonac(var1-1) + fibonac(var1-2)
print("fibonacci nth number:",fibonac(6))

# def calculate_running_average()
# what is a running average?