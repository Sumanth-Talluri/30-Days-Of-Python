age = 14
height = 185.5
comp = 1 + 2j

base = float(input("Enter base: "))
ht = float(input("Enter height: "))
area = 0.5*base*ht
print(f"The area of the triangle is {area}")

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a+b+c
print(f"The perimeter of the triangle is {perimeter}")

length = float(input("Enter lenght: "))
width = float(input("Enter width: "))
print(f"Area: {length*width}")
print(f"Perimeter: {2*(length+width)}")

r = float(input("Enter radius: "))
print(f"Area of circle: {3.14*r*r}")
print(f"Circumference of circle: {2*3.14*r}")

x_intercept = -(-2)/2
y_intercept = -2
slope = 2
print(f"x_intercept: {x_intercept}")
print(f"y_intercept: {y_intercept}")
print(f"slope: {slope}")

m = (10-2)/(6-2)
print(f"Slope between point (2, 2) and point (6,10) is: {m}")

if slope > m:
    print("Slope of Task 8 is greater")
else:
    print("Slope of Task 9 is greater")

for x in [-4, -3, -2, -1, 0, 1, 2, 3, 4]:
    y = x**2 + 6*x + 9
    if y == 0:
        print(f"y is zero when x is : {x}")
        break

print(not (len("python") or len("jargon")))

if "on" in "python" and "on" in "jargon":
    print("present in both")

if "jargon" in "I hope this course is not full of jargon":
    print("jargon is present in the sentence")

if not ("on" in "dragon" or "on" in "python"):
    print("There is no 'on' in both dragon and python")

length = len("python")
fltval = float(length)
strval = str(fltval)

n = int(input("Enter a number"))
if n % 2 == 0:
    print("n is even")
else:
    print("n is odd")

if 7//3 == int(2.7):
    print("The floor division of 7 by 3 is equal to the int converted value of 2.7")

if type('10') == type(10):
    print("Equal types")
else:
    print("Not equal types")

if int(9.8) == 10:
    print("equal")
else:
    print("not equal")

hrs = int(input("Enter hours: "))
rate = int(input("Enter rate per hour: "))
print(f"Your weekly earning is {hrs*rate}")

yrs = int(input("Enter number of years you have lived: "))
print(f"You have lived for {yrs*31536000} seconds")

print("Pattern \n")
for i in range(1, 6):
    for j in range(1, 6):
        if i == 1:
            print("1 ", end=' ')
        else:
            if j == 1:
                print(f"{i} ", end=' ')
            elif j == 2:
                print("1 ", end=' ')
            else:
                print(f"{i**(j-2)} ", end=' ')
    print("\n", end='')
