print("helloworld")

print("aayush")

#Arethamatic and maths

friends=10

#friends -= 1
#friends += 1

#friends *=3
#friends **=2

#friends /=3
friends %=4

print(friends)

x=1.8
y=-4
z=6.28

value=round(x)
value=abs(y)
value=pow(y,3)

print(value)

import math

print(math.pi)
print(math.e)

#result=math.sqrt(z)
result=math.ceil(3.7)
#result=math.floor(3.7)
print(result)

#EXERCIES 3 Circumference of circle

Radius=float(input("What is the Radius of the circle? :"))

w = 2 * math.pi * Radius

print(f"The circumference of the circle is: {round(w, 2)}")

#EXERCISE 4  Area of circle

radius=float(input("What is the Radius of the circle? :"))

radius **=2
area = math.pi * radius  #pow(radius,2)

print(f"Area of circle is : {round(area , 2)}")

a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))

c=math.sqrt( pow(a,2) + pow(b,2))

print(f"THe value of c is : {round(c,2)}")
