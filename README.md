-GRADEBOOK GRADING SYSTEM-

PROJECT OVERVIEW

To develop a comprehensive, user-friendly Python based grading system that  digitizes the current grading system.The system manages student records, allows handling of multiple subjects, and support operations like adding, updating, searching, sorting, and reporting student grades. Each section introduces new programming ways from basic input and output concepts to a more object-oriented and exception handling design.

SECTION DESCRIPTIONS

SECTION A

-Section A creates a simple proram using scalar objects and loops, it focusus on using basic    input and output concepts loops and also introduces validity.

Section A prompts the user to input the number of students as well as their names and collects each students single subject grade and validates grades by checking grades only between and inclusive of 0 and 100.

It also prints basic results(class average and class total).




SECTION B 

-Section B introduces Lists and tuples in the program.

Expanded each student to multiple subjects those subjects being Math,Science,Physics and English

Uses Tuples to store student records and lists to store their grades.

Calculates the average of each student as well as the overall class totals and averages.

It also allows identification of each subjects highest and lowest grades.

It outputs a summary of all students and their performances.



SECTION C

-Section C introduces Dictionaries.

The tuples we had placed are replaced with dictionaries for better data management.

It stores the students grades per subject in dictionaries.

This section introduces the use of menus and adds the ability to add, update, search, view and remove functionalities. 

It also implements subject-specific analysis for each student as well as their calculated grades.




SECTION D

-Section D uses functions.

Section D modularized code into functions to allow reusability and code organization.

It also brought on simple error handling for example KeyErrors and ValueErrors and a more menu functionality



SECTION E

-Section E introduces a more Object-oriented Programm.

Implements a STUDENT CLASS which stores the students names and grades in dictionaries and the key focuses in the student class are to calculate the students averages and display of all grades.

Also implements a GRADEBOOK CLASS which manages multiple student objects and the overall class calculations, it manages the school menu interface and provides the student-subject analysis and also searches,updates,removes students.



SECTION F

-Section F- Exception Handling and Enhancements

Section F is the final enhancement of the grading system and cintergrates the previous sections into 1.

It adds the use of custom exceptions for example InvalidGradeError and StudentNotFoundError for clean, more user-friendly error messages. Implemented Bubble Sort algorithm to rank the students in descending order by their average grades and names.
Adds comprehensive testing and documentations findings as comments in the code.



Section Integration Summary.
Each section builds on the previous one:

- Section A lays the foundation with basic input/output concepts meaning its independent.
- 
- Section B introduces multi-subject support and compound data structures.
- 
- Section C enhances data structure flexibility.
- 
- Section D improves code organization.
- 
- Section E formalizes the program with OOP.
- 
- Section F ensures usability, and completeness.



INPUT AND OUPUT EXPECTATION EXAMPLE:
--GRADING SYSTEM--
Welcome to Grading System!

--- SCHOOL MENU ---
1. Add a new student
2. Remove a student
3. Update student grades
4. Search for a student
5. Display all students
6. View student grades
7. Exit
Enter your choice: 1
Enter student name: ENTLE
Enter Entle's grade for Math: 34
Enter Entle's grade for English: 67
Enter Entle's grade for Science: 88
Enter Entle's grade for Physics: 99
Student Entle has been added.

--- SCHOOL MENU ---
1. Add a new student
2. Remove a student
3. Update student grades
4. Search for a student
5. Display all students
6. View student grades
7. Exit
Enter your choice: 1
Enter student name: TY
Enter Ty's grade for Math: 780
Grade must be between 0 and 100.Try again
Enter Ty's grade for Math: 34
Enter Ty's grade for English: 67
Enter Ty's grade for Science: 89
Enter Ty's grade for Physics: 90
Student Ty has been added.

--- SCHOOL MENU ---
1. Add a new student
2. Remove a student
3. Update student grades
4. Search for a student
5. Display all students
6. View student grades
7. Exit
Enter your choice: 1
Enter student name: TEPS
Enter Teps's grade for Math: 67
Enter Teps's grade for English: 89
Enter Teps's grade for Science: 90
Enter Teps's grade for Physics: 56
Student Teps has been added.

--- SCHOOL MENU ---
1. Add a new student
2. Remove a student
3. Update student grades
4. Search for a student
5. Display all students
6. View student grades
7. Exit
Enter your choice: 2
Enter student name: TEPS
 Student Teps has been removed.

--- SCHOOL MENU ---
1. Add a new student
2. Remove a student
3. Update student grades
4. Search for a student
5. Display all students
6. View student grades
7. Exit
Enter your choice: 3
Enter student name: ENTLE
Current grades for Entle: {'Math': 34.0, 'English': 67.0, 'Science': 88.0, 'Physics': 99.0}
Enter updated grade for Math: 67
Enter updated grade for English: 98
Enter updated grade for Science: 78
Enter updated grade for Physics: 56
Student Entle grades have been updated.

--- SCHOOL MENU ---
1. Add a new student
2. Remove a student
3. Update student grades
4. Search for a student
5. Display all students
6. View student grades
7. Exit
Enter your choice: 4
Enter student name: TEP
Student not found.

--- SCHOOL MENU ---
1. Add a new student
2. Remove a student
3. Update student grades
4. Search for a student
5. Display all students
6. View student grades
7. Exit
Enter your choice: 4
Enter student name: ENTLE

Entle's Grades:

Math: 67.0

English: 98.0

Science: 78.0

Physics: 56.0
Average: 74.75

--- SCHOOL MENU ---
1. Add a new student
2. Remove a student
3. Update student grades
4. Search for a student
5. Display all students
6. View student grades
7. Exit
Enter your choice: 5

---ALL STUDENTS---
Entle: {'Math': 67.0, 'English': 98.0, 'Science': 78.0, 'Physics': 56.0}, Average = 74.75
Ty: {'Math': 34.0, 'English': 67.0, 'Science': 89.0, 'Physics': 90.0}, Average = 70.00

--- SCHOOL MENU ---
1. Add a new student
2. Remove a student
3. Update student grades
4. Search for a student
5. Display all students
6. View student grades
7. Exit
Enter your choice: 6

--- SUBJECT ANALYSIS ---
Math: Highest = 67.0, Lowest = 34.0, Average = 50.50
English: Highest = 98.0, Lowest = 67.0, Average = 82.50
Science: Highest = 89.0, Lowest = 78.0, Average = 83.50
Physics: Highest = 90.0, Lowest = 56.0, Average = 73.00

--- SCHOOL MENU ---
1. Add a new student
2. Remove a student
3. Update student grades
4. Search for a student
5. Display all students
6. View student grades
7. Exit
Enter your choice: 7
 Exiting program. Goodbye!


-THE EXAMPLES ABOVE SHOW THE PROGRAM OUPUTS AND INPUTS AND HOW IT WORKS, IT DEMONSTRATES HOW EXCEPTIONS AND VALIDATIONS WORK AND SHOWS VALIDITY ERRORS, CALCULATIONS AND ALSO THE SUBJECT ANALYSIS INCLUDING THE USE OF THE SCHOOL MENU INTERFACE.



Grading System Assumptions and Limitations

-Assumptions:

They are four fixed subjects: MATH,PHYSICS,ENGLISH,SCIENCE

Grade must fall between 0 and 100.

Unique Student names

User interaction with menu interface and user knowledge.



-Limitations:

Data isnt saved, student records are temporarily in the memory

Subjects are fixed and cannot be modified during runtime

No multi user access

Basic-Error Handling


  


