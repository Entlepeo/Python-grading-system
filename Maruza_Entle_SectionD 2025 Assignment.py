print("--GRADING SYSTEM--")

subjects = ["Math", "English", "Science", "Physics"]

#student-dictionary
students = {}

#add new student function
def add_student():
    name = input("Enter student name: ").capitalize()
    if name in students:
        print(f"{name} already exists. Choose another option.")
        return

    grades = {}
    for subject in subjects:
        while True:
            try:
                grade = float(input(f"Enter {name}'s grade for {subject}: "))
                if 0 <= grade <= 100:
                    grades[subject] = grade
                    break
                else:
                    print("Grade must be between 0 and 100.Try again")
            except ValueError:
                print("Grade must be between 0 and 100.")

    students[name] = grades
    print(f"Student {name} has been added.")

#remove a student function
def remove_student():
    name = input("Enter student name: ").capitalize()
    if name in students:
        del students[name]
        print(f" Student {name} has been removed.")
    else:
        print("Student not found.")

#function for updating students
def update_student():
    name = input("Enter student name: ").capitalize()
    if name not in students:
        print("Student not found.")
        return

    print(f"Current grades for {name}: {students[name]}")
    for subject in subjects:
        while True:
            try:
                update = float(input(f"Enter updated grade for {subject}: "))
                if 0 <= update <= 100:
                    students[name][subject] = update
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid Input.Grade must be between 0 and 100.")
    print(f"Student {name} grades have been updated.")


#function for student search and displaying information
def student_search():
    name = input("Enter student name: ").capitalize()
    if name not in students:
        print("Student not found.")
        return

    grades = students[name]
    total = sum(grades.values())
    average = total / len(grades)
    print(f"\n{name}'s Grades:")
    for subject, mark in grades.items():
        print(f"\n{subject}: {mark}")
    print(f"Average: {average:.2f}")

#function for displaying all students
def display_all():
    if not students:
        print("No student information found.")
        return

    print("\n---ALL STUDENTS---")
    for name, grades in students.items():
        total = sum(grades.values())
        average = total / len(subjects)
        print(f"{name}: {grades}, Average = {average:.2f}")

#function for viewing student grades
def view_student_grades():
    if not students:
        print("No student data to analyze.")
        return

    print("\n--- SUBJECT ANALYSIS ---")
    for i, subject in enumerate(subjects):
        try:
            subject_grades = [grades[subject] for grades in students.values()]
            print(f"{subject}: Highest = {max(subject_grades)}, Lowest = {min(subject_grades)}, "
                  f"Average = {sum(subject_grades)/len(subject_grades):.2f}")
        except KeyError:
            print(f"{subject}: Missing data for some students.")



#function for main menu
def main_menu():

    while True:
        print("\n--- SCHOOL MENU ---")
        print("1. Add a new student")
        print("2. Remove a student")
        print("3. Update student grades")
        print("4. Search for a student")
        print("5. Display all students")
        print("6. View student grades")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            update_student()
        elif choice == "4":
            student_search()
        elif choice == "5":
            display_all()
        elif choice == "6":
            view_student_grades()
        elif choice == "7":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

#function run program
def run_program():
    print("Welcome to Grading System!")
    main_menu()

#start-program
run_program()
