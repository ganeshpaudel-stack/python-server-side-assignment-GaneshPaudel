# Create a program that takes a list of students and store them in file. Then read the file and display the content.

n = int(input("How many students do you want to enter? "))

with open("students.txt", "a") as file:
    for i in range(n):
        name = input("Enter the name of the student: ")
        file.write(name + "\n")

print("\nThe list of students is:")

with open("students.txt", "r") as file:
    print(file.read())