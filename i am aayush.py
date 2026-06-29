print("learning something new")
print("i am about to kill you")

your_name= "Aayush the great coder"
print(f"hello {your_name}")
food="apple"
print(f"you like {food}")
email="aayushchawan3@gmail.com"
print("my email is {email}")
#integers

age=12
a=19
print(f"you are {age} years old")
print(f"a+{age}")

#floats
a=0.79
b=34.56

print(a+b)
total=b+a*b
print(f"Total : {total}")

#boolean
is_older_than_18 = True
print(f"is_older_than_18: {is_older_than_18}")

if is_older_than_18:
    print("You are eligible to watch this")
else:
    print("You are not eligible to watch this")

a = True
if a:
    print("hi")
else:
    print("get out")

is_with_other_boy = True
if is_with_other_boy:
    print("SHE IS CHEATING ON YOU")
else:
    print("SHE IS NOT CHEATING ON YOU")

#type casting
my_name = "BOB THE BUILDER"
age = 25
weight = 1000.9
is_your_friend = True

print(type(weight))

weight = int(weight)
print(f"my weight is :{weight}")

age = str(age)
print(age)

name=input("What is your name? :")
print(f"You are the best {name}")

age = input("what is your age?")
age = int(age)
age += 1

#can i put such constraints that i can say you are old if above 45 and you are young iif answer is below 45
print(f"you are {age} years old")
name = input("Enter your name: ")
age = input("Enter your age: ")
weight = input("Enter your weight (in kg): ")

# Type casting
age = int(age)
weight = float(weight)

# Data card
print(f"\n--- APPLICANT DATA ---")
print(f"Name  : {name}")
print(f"Age   : {age}")
print(f"Weight: {int(weight)} kg")
print(f"Weight data type: {type(weight)}")

# Booleans
is_old_enough = age >= 18
is_weight_ok = weight <= 90.0

print(f"\nAge eligible    : {is_old_enough}")
print(f"Weight eligible : {is_weight_ok}")


    






