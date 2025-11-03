print("--GRADING SYSTEM--")

subjects = ["Math", "English", "Science","Physics"]
num_of_students = int(input("Enter the number of students: "))
students = []

for i in range(num_of_students):
    print("\nstudents #", i+1, ": ")
    name = input(f"Enter student's name {i+1}: ")
    grades=[]

   #Grade Validation
    for subject in subjects:
        while True:
            try:
                grade = float(input(f"Enter {name}'s grade for {subject} (0-100): "))
                if grade > 0 and grade <= 100:
                    print("Acceptable grade.")
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100. Try again.")
            except ValueError:
                print("Grade must be between 0 and 100.")

    # Store student as a tuple (name, [grades])
    students.append((name, grades))

#Student Summary
print("\n -Student Summary-")
for student in students:
    name, grades = student
    total = sum(grades)
    avg = total / len(grades)
    print(f"{name} - Grades: {grades}, Total Mark: {total}, Average Mark: {avg:.2f}")

# determining the highest and lowest marks in each subject
print("\n-Subject Analysis-")
for i, subject in enumerate(subjects):
    subject_grades = [student[1][i] for student in students]
    print(f"{subject}: Highest Mark = {max(subject_grades)}, Lowest Mark = {min(subject_grades)},Average Mark = {sum(subject_grades)/len(subject_grades):.2f}")

# Overall class total and average across all subjects
print("\n-Class Summary-")
all_grades = [grade for student in students for grade in student[1]]
overall_total = sum(all_grades)
overall_avg = overall_total / len(all_grades)
print(f"\nOverall Class Total (all subjects): {overall_total}")
print(f"Overall Class Average (all subjects): {overall_avg:.2f}")