print("helloworld")

print("aayush")

#user input= The info which user provide. input is always in string form so to do arethamatic or anything typecast it.

name=input("what is your friends name? : ")
age=input("what is your friends age? : ")

print(f"Hello {name}")

if int(age)<18:
    print("you are okay")
else:
    print("you are too old")

age=int(age)
age=age+1
print(f"Happy birthday {name}! You are now {age}.")

#EXERCISE 1 : area of quadrilateral calculator

length=int(input("What is the qudrilaterals length? :"))
breadth=int(input("What is the quadrilaterals breadth? :"))

area=length*breadth
print(f"Your quadrilateral area is : {area}")

#EXEECISE 2 : Shopping cart calculator

item=input("What would you like to buy? :")
price=float(input("What is the price of the item? :"))
quantity=int(input("How many would you like to buy? :"))

total=price*quantity
print(f"Your total comes to : {total}")
