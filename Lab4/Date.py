import datetime

a = datetime.datetime.today()
b = a - datetime.timedelta(days = 5)
print(b)
print("-----------------------------------")

yesterday = datetime.datetime.now() + datetime.timedelta(days = -1)
today  = datetime.datetime.now()
tomorow = datetime.datetime.now() + datetime.timedelta(days = 1)
print(yesterday)
print(today)
print(tomorow)
print("-----------------------------------")

withoutmil = datetime.datetime.now()
print(withoutmil.strftime("%Y-%m-%d-%S"))

year1 = int(input('Enter a  first year: '))
month1 = int(input('Enter a first month: '))
day1 = int(input('Enter a first day: '))
date1 = datetime.date(year1, month1, day1)

year2 = int(input('Enter a  second year: '))
month2 = int(input('Enter a second month: '))
day2 = int(input('Enter a second day: '))
date2 = datetime.date(year2, month2, day2)

dif = abs(date1 - date2)
print(dif.days * 86400, "seconds difference")