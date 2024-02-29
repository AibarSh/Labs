import re

txt1 = open("Text.txt", "r")

pattern1 = "ab*"
search = re.findall(pattern1, txt1)
print(search)

pattern2 = "ab{2,3}"
search = re.findall(pattern2,  "abbbbb, ba, abb, a, abb")
print(search)

pattern3 = "[a-z]+_[a-z]+"
search = re.findall(pattern3,  "abbbbb, ba, abb, a, abb, a_bab")
print(search)

pattern4 = "[A-Z][a-z]+"
search = re.findall(pattern4, )
print(search)

pattern5 = "a.*b$"
search = re.findall(pattern5, )
print(search)

pattern6 = '[ ,.]' # use re.sub
search = re.sub(pattern6,':',  )
print(search)

pattern7 = "(?:^|_)([a-z])" # use re.sub
search = re.sub(pattern7, )
print(search)

pattern8 = '[A-Z][^A-Z]*'
search = re.findall(pattern8, )
print(search)

pattern9 = '(?<!^)(?=[A-Z])', ' ' # use re.sub
search = re.sub(pattern9, ' ', )
print(search)

pattern10 = '(?<!^)(?=[A-Z])' # use re.sub
search = re.sub(pattern10, '_', )
print(search)