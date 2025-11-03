#SECTION F
print("--GRADING SYSTEM--")

#Custom Exceptions
class InvalidGradeError(Exception):
    """Raised when the grade entered is invalid (not 0–100 or not numeric)."""
    pass


class StudentNotFoundError(Exception):
    """Raised when a student search fails."""
    pass

#Student Class
class Student:
    def __init__(self, name):
        self.name = name.capitalize()
        self.grades = {}

    def add_grade(self, subject, grade):
        """Add or update a grade"""
        try:
            grade = float(grade)
            if not 0 <= grade <= 100:
                raise InvalidGradeError(f"{subject} grade must be between 0 and 100.")
            self.grades[subject] = grade
        except ValueError:
            raise InvalidGradeError("Grade is not numeric.")

    def average(self):
        return sum(self.grades.values()) / len(self.grades) if self.grades else 0

    def display(self):
        print(f"\n{self.name}'s Grades:")
        for subject, mark in self.grades.items():
            print(f"  {subject}: {mark}")
        print(f"Average: {self.average():.2f}")

#Gradebook Class
class Gradebook:
    def __init__(self, subjects):
        self.subjects = subjects
        self.students = {}

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
                    student.add_grade(subject, grade)
                    break
                except InvalidGradeError as e:
                    print("Error:", e)
        self.students[name] = student
        print(f"Student {name} has been added.")

    def remove_student(self):
        name = input("Enter student name: ").capitalize()
        try:
            if name not in self.students:
                raise StudentNotFoundError(f"Student '{name}' not found.")
            del self.students[name]
            print(f"Student {name} removed.")
        except StudentNotFoundError as e:
            print("Error:", e)

    def update_student(self):
        name = input("Enter student name: ").capitalize()
        try:
            if name not in self.students:
                raise StudentNotFoundError(f"Student '{name}' not found.")
            student = self.students[name]
            for subject in self.subjects:
                while True:
                    try:
                        grade = input(f"Enter updated grade for {subject}: ")
                        student.add_grade(subject, grade)
                        break
                    except InvalidGradeError as e:
                        print("Error:", e)
            print(f"{name}'s grades have been updated.")
        except StudentNotFoundError as e:
            print("Error:", e)

    def search_student(self):
        name = input("Enter student name: ").capitalize()
        try:
            if name not in self.students:
                raise StudentNotFoundError(f"Student '{name}' not found.")
            self.students[name].display()
        except StudentNotFoundError as e:
            print("Error:", e)

#Bubble Sort Algorithm
    def bubble_sort_students(self):
        """Sort students by average (descending)."""
        student_list = list(self.students.values())
        n = len(student_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if student_list[j].average() < student_list[j + 1].average():
                    student_list[j], student_list[j + 1] = student_list[j + 1], student_list[j]
        return student_list

    def display_sorted(self):
        """Display students by the sorted average grade."""
        if not self.students:
            print("No students to sort.")
            return
        print("\n--- SORTED STUDENTS (By Average Grade) ---")
        for s in self.bubble_sort_students():
            s.display()

    def display_all(self):
        if not self.students:
            print("No student data available.")
            return
        print("\n--- ALL STUDENTS ---")
        for s in self.students.values():
            s.display()

    def view_subject_analysis(self):
        """Show highest, lowest, and average for each subject."""
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


#Main Program
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
        print("7. Display sorted students")
        print("8. Exit")

        choice = input("Enter your choice: ")

        try:
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
                gradebook.display_sorted()
            elif choice == "8":
                print("Exiting Program. Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main_menu()


#Testing Documentation
#test1: Added a valid student:Works
#test2: Entered a non-numeric grade:InvalidGradeError handled :Works
#test3: Entered grade >100 :InvalidGradeError handled:Works
#test4: Removed missing student :StudentNotFoundError handled:Works
#test5: Sorting by average :Displays students in descending order:Works
#test6: No students in system :Program displays "No student data available":Works
#test7: Searched for existing student:Displayed details correctly: Works

