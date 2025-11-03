#SECTION A
print("--GRADING SYSTEM--")

#STUDENT ENTRY
num_of_students = int(input("Enter the number of students: "))

#to calculate the total grades
total=0

for i in range(num_of_students):
    print("\nstudents #", i+1, ": ")
    name = input(f"Enter student's name {i+1}: ")

     #GRADE VALIDATION
    while True:
        try:
            grade = int(input("Enter grade between 1-100: "))
            if grade > 0 and grade <= 100:
                print("Acceptable grade.")
                break
            else:
                print("Grade must be between 1 and 100.")
        except ValueError:
            print("Grade must be a number between 1 and 100.")


    print(f"{name}'s grade is {grade}")

#calculations
    total = total + grade

average = total / num_of_students

#CLASS SUMMARY
print("\n-Class Summary-")
print(f"Total grade: {total} ")
print(f"Average grade: {average:.2f} ")
