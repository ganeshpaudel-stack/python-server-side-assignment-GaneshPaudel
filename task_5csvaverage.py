# 5. Write Python code to read from a CSV file of student marks and calculate average marks.

import csv
with open("05_marks.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    
    total_st = 0
    total_marks  = 0

    for row in reader:
        total_st += 1
        total_marks += int(row[1])

    average_marks = total_marks/total_st
    print("No of students = ", total_st)
    print("Total marks = ", total_marks)
    print("Average marks  = " ,average_marks)
