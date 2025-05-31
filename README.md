"# class_assignment-uni_manage_system" 

# 🎓 University Management System (OOP in Python)

This is a simple object-oriented Python program simulating a **University Department System**, including functionality for **Departments**, **Courses**, **Students**, and **Instructors**.

---

## 📂 Project Structure

The system is composed of the following classes:

- `Person`: Base class with `name` and `age`.
- `Student`: Inherits from `Person`. Has a `roll_number` and registered `courses`.
- `Instructor`: Inherits from `Person`. Has a `salary` and teaches multiple `courses`.
- `Cource`: Represents a course, with registered `students` and assigned `instructors`.
- `Department`: A university department containing multiple `courses`.

---

## 🛠 Features

- Create departments and add courses to them.
- Register students in specific courses.
- Assign instructors to courses.
- Display department, course, instructor, and student details in a formatted output.

---

==========================

📘 Concepts Used in Python Code

==========================

1. ✅ **Classes and Objects**
   - Class definitions: `Person`, `Student`, `Instructor`, `Cource`, `Department`
   - Object creation (e.g., `student = Student(...)`)

2. ✅ **Inheritance**
   - `Student` and `Instructor` inherit from `Person`
   - `super().__init__()` is used to call the parent constructor

3. ✅ **Constructors (`__init__` method)**
   - Used to initialize object properties when a class instance is created

4. ✅ **Instance Variables**
   - e.g., `self.name`, `self.age`, `self.rollnumber`, etc.

5. ✅ **Method Overriding**
   - Not directly overridden here, but methods like `__init__` are customized in child classes

6. ✅ **Encapsulation**
   - Properties are accessed and modified only through methods (e.g., `add_student()`)

7. ✅ **List Data Structure**
   - Used to store multiple students/instructors/courses in one place
   - Examples: `self.students = []`, `self.cources = []`

8. ✅ **Function/Method Definitions**
   - Custom methods like `add_student()`, `assigncourse()`, `add_cource()` etc.

9. ✅ **Composition (HAS-A Relationship)**
   - A `Department` has `Courses`
   - A `Course` has `Students` and `Instructors`

10. ✅ **Formatted Strings (f-strings)**
    - Used for neat and readable output:  
      `print(f"Name: {instructor.name}")`

11. ✅ **Looping (for loop)**
    - Iterating over lists:  
      `for course in instructor.cources:`

12. ✅ **Conditional Statements**
    - `if course.instructor:` used to check if an instructor is assigned


13. ✅ **Type Hinting (Optional Concept)**
    - Not used here, but can be added for clarity (e.g., `def __init__(self, name: str)`)

==========================

🧠 Concepts help you write reusable, structured, and readable code in OOP style!

==========================
