print("helloworld")

print("aayush")

a=10
b=12

print(a**b)

print(a*b)
print("aayush")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subjects = {}

    def add_subject(self, subject, marks):
        self.subjects[subject] = marks

    def show_report(self):
        print(f"\n--- Report for {self.name} (Age {self.age}) ---")
        for subject, marks in self.subjects.items():
            print(f"{subject}: {marks}")
        avg = sum(self.subjects.values()) / len(self.subjects)
        print(f"Average: {avg:.2f}")


# Using the class
name = input("Enter your name: ")
age = int(input("Enter your age: "))

student = Student(name, age)

num = int(input("How many subjects? "))
for i in range(num):
    subject = input("Subject name: ")
    marks = int(input("Marks: "))
    student.add_subject(subject, marks)

student.show_report()