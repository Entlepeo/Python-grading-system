#SECTION E
print("--GRADING SYSTEM--")


# Student Class
class Student:
    def __init__(self, name):
        self.name = name.capitalize()
        self.grades = {}  # {subject: mark}

    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:
            self.grades[subject] = grade
        else:
            raise ValueError("Grade must be between 0 and 100.")

    def update_grades(self, subjects):
        for subject in subjects:
            while True:
                try:
                    new_grade = float(input(f"Enter updated grade for {subject}: "))
                    if 0 <= new_grade <= 100:
                        self.grades[subject] = new_grade
                        break
                    else:
                        print("Grade must be between 0 and 100.Try Again.")
                except ValueError:
                    print("Grade must be between 0 and 100.")

    def average(self):
        return sum(self.grades.values()) / len(self.grades) if self.grades else 0

    def display(self):
        print(f"\n{self.name}'s Grades:")
        for subject, mark in self.grades.items():
            print(f"  {subject}: {mark}")
        print(f"Average: {self.average():.2f}")



# Gradebook Class
class Gradebook:
    def __init__(self, subjects):
        self.subjects = subjects
        self.students = {}  # {name: Student object}

    def add_student(self):
        name = input("Enter student name: ").capitalize()
        if name in self.students:
            print(f"{name} already exists.")
            return

        student = Student(name)
        for subject in self.subjects:
            while True:
                try:
                    grade = float(input(f"Enter {name}'s grade for {subject}: "))
                    if 0 <= grade <= 100:
                        student.add_grade(subject, grade)
                        break
                    else:
                        print("Grade must be between 0 and 100.Try Again.")
                except ValueError:
                    print("Grade must be between 0 and 100.")

        self.students[name] = student
        print(f"Student {name} has been added.")

    def remove_student(self):
        name = input("Enter student name: ").capitalize()
        if name in self.students:
            del self.students[name]
            print(f"Student {name} removed.")
        else:
            print("Student not found.")

    def update_student(self):
        name = input("Enter student name: ").capitalize()
        if name in self.students:
            self.students[name].update_grades(self.subjects)
            print(f"{name}'s grades have been updated.")
        else:
            print("Student not found.")

    def search_student(self):
        name = input("Enter student name: ").capitalize()
        student = self.students.get(name)
        if student:
            student.display()
        else:
            print("Student not found.")

    def display_all(self):
        if not self.students:
            print("Student not found.")
            return
        print("\n--- ALL STUDENTS ---")
        for student in self.students.values():
            student.display()

    def view_subject_analysis(self):
        if not self.students:
            print("No student data to analyze.")
            return
        print("\n--- SUBJECT ANALYSIS ---")
        for subject in self.subjects:
            try:
                marks = [stu.grades[subject] for stu in self.students.values()]
                print(f"{subject}: Highest = {max(marks)}, Lowest = {min(marks)}, "
                      f"Average = {sum(marks)/len(marks):.2f}")
            except KeyError:
                print(f"{subject}: Missing data for some students.")


# Main Program

def main_menu():
    subjects = ["Math", "English", "Science", "Physics"]
    gradebook = Gradebook(subjects)

    while True:
        print("\n--- SCHOOL MENU ---")
        print("1. Add new student")
        print("2. Remove student")
        print("3. Update student grades")
        print("4. Search for a student")
        print("5. Display all students")
        print("6. View subject analysis")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            gradebook.add_student()
        elif choice == "2":
            gradebook.remove_student()
        elif choice == "3":
            gradebook.update_student()
        elif choice == "4":
            gradebook.search_student()
        elif choice == "5":
            gradebook.display_all()
        elif choice == "6":
            gradebook.view_subject_analysis()
        elif choice == "7":
            print("Exiting Program.Bye")
            break
        else:
            print("Invalid option. Try again.")


# Run Program
if __name__ == "__main__":
    main_menu()



