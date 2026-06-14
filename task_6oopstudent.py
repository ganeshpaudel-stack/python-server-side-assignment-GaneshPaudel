''' Develop a simple OOP based python class Student with attributes like name, roll number, and marks . Implement  methods to input
 and display details.'''

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print("Student Details:")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

name = input("Enter student's name: ")
roll_number = input("Enter student's roll number: ")
marks = float(input("Enter student's marks: "))

s1= Student(name, roll_number, marks)
s1.display_details()