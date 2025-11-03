print("--GRADING SYSTEM--")

subjects = ["Math", "English", "Science","Physics"]

#dictionary
students ={}

while True:
    print("n/SCHOOL MENU")
    print("1. Add a new student")
    print("2. Remove a student")
    print("3. Update students grades")
    print("4. View student grades")
    print("5. Student Search")
    print("6. Display all students")
    print("7. Exit")

    choice = input("Enter your choice: ")

#ADDING A STUDENT
    if choice == "1":
        name=input("Enter student name: ").capitalize()
        if name in students:
            print(f"{name} already exists. Choose another option.")
        else:
            grades={}
            for subject in subjects:
                while True:
                    try:
                        grade=float(input(f"Enter {name}'s grade for {subject}: "))
                        if 0<= grade <= 100:
                            grades[subject]= grade
                            break
                        else:
                            print("Grade must be between 0 and 100. Try again.")
                    except ValueError:
                        print("Grade must be between 0 and 100.")

            #dictionary
            students[name] = grades
            print(f"Student {name} has been added.")

#REMOVING YOUR STUDENTS
    elif choice == "2":
        name=input("Enter student name: ").capitalize()
        if name in students:
            del students[name]
            print(f"Student {name} has been removed.")
        else:
            print(f"Student {name} not found")


#UPDATING STUDENT GRADES
    elif choice == "3":

        name = input("Enter student name: ").capitalize()
        if name in students:
            print(f"Current grades for {name}: {students[name]}")
            for subject in subjects:
                while True:
                    try:
                        update = float(input(f"Enter updated grade for {subject}: "))
                        if 0<= update <= 100:
                            students[name][subject] = update
                            break
                        else:
                            print("Grade must be between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            print(f"{name}'s grades have been updated.")
        else:
            print(f"Student {name} not found.")

#VIEW GRADES BY SUBJECT
    elif choice == "4":
        subject=input("Enter subject name: ").capitalize()
        if subject in subjects:
            print(f"\n{subject} Grades:")
            for name, grades in students.items():
                print(f"\n{name}: {grades[subject]}")
        else:
            print("Subject grades not found.")

#STUDENT SEARCH
    elif choice == "5":
        name=input("Enter student name: ").capitalize()
        if name in students:
            grades=students[name]
            total=sum(grades.values())
            average=total/len(grades)
            print(f"\n{name} Grades:")
            for subject, mark in grades.items():
                print(f"\n{subject}: {mark}")
            print(f"average: {average:.2f}")
        else:
            print("Student not found")

#DISPLAY STUDENT INFORMATION
    elif choice == "6":
            if not students:
                print("No student information found")
            else:
                print("\n---ALL-STUDENTS---")
                for name, grades in students.items():
                    average=sum(grades.values())/len(grades)
                    print(f"\n{name}:{grades}, Average = {average:.2f}")

#EXIT PROGRAM
    elif choice == "7":
            print("You selected Exit.Bye")
            break

    else:
        print("Invalid choice. Try again.")