#strings
txt = """Bob was walking 
down the hallway."""
# same as txt = '''Bob was walking 
# down the hallway.'''
print(txt)
print(txt[4]) 
for b in "Helicopter":
    print(b)

print(len(txt))
print("down" in txt)

if "walking" in txt:
    print("Yes, 'walking' is present")
if "running" not in txt:
    print("'running' is not in txt")