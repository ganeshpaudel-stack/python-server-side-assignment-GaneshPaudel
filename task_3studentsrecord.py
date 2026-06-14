''' Implements a program to store student records(name, roll, marks, contract number) using a dictionry.
a) Provide menu to add search and display students.'''

students = {}
while True:
    print("----Student Records Management----")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display Students")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student's name: ")
        roll = input("Enter student's roll number: ")
        marks = input("Enter student's marks: ")
        contact = input("Enter student's contact number: ")
        students[roll] = {'name': name, 'marks': marks, 'contact': contact}
        print("Student added successfully!\n")

    elif choice == '2':
        roll = input("Enter roll number to search: ")
        if roll in students:
            print("Student found:")
            print(f"Name: {students[roll]['name']}")
            print(f"Marks: {students[roll]['marks']}")
            print(f"Contact: {students[roll]['contact']}\n")
        else:
            print("Student not found!\n")

    elif choice == '3':
        if students:
            print("List of Students:")
            for roll, info in students.items():
                print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}, Contact: {info['contact']}")
            print()
        else:
            print("No students to display!\n")

    elif choice == '4':
        print("Exiting the program. ")
        break
    else:
        print("Invalid choice! Please try again.\n")
        