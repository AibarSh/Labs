import math

a = float(input("Enter degree:"))
print("Radians:", math.radians(a))

base1 = float(input("base 1 of trapezoid:"))
base2 = float(input("base 2 of trapezoid:"))
height = float(input("Height of the trapezoid:"))
if base1 > base2:
    A = (base2 + (base1-base2)/2) *  height
    print("Area of the trapezoid = ", A)
else:
    A = (base1 + (base2-base1)/2) *  height
    print("Area of the trapezoid = ", A)

sidesnum = int(input("Enter num of sides:"))
sidelen = float(input("Enter side lengh:"))
# apothem = (sidelen) / (2 * math.tan(180/sidesnum))
area =(sidesnum * sidelen ** 2) / (4 * math.tan(math.pi / sidesnum))
print("Area of polygon = ", int(area))

pbase = float(input("Enter base of parallelogram:"))
pheight = float(input("Enter height of parallelogram:"))
print("Area of parallelogram = ", pbase * pheight)