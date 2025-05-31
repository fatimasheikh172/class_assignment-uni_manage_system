class Person():
    def __init__(self , name , age ):

        self.name = name
        self.age = age

    def get_name(self):
        print(self.name , self.age)

class Student(Person):
    def __init__(self , name , age , roll_number):
      super().__init__(name , age)
      self.rollnumber = roll_number
      self.cources = []

    def add_regestration(self , cource):
      self.cources.append(cource)
      cource.add_student(self)

class Instructor(Person):
  def __init__(self , name , age , salary):
    super().__init__(name , age)
    self.salary = salary
    self.cources = []

  def assigncourse(self , cource):
    self.cources.append(cource)
    cource.add_instructor(self)

class Cource:
  def __init__(self , name):
    self.name = name
    self.students = []
    self.instructor = []

  def add_student(self , student):
    self.students.append(student)

  def add_instructor(self , instructor):
    self.instructor.append(instructor)

class Department:
  def __init__(self , name):
    self.name = name
    self.cources = []

  def add_cource(self , cource):
    self.cources.append(cource)

# create department
cs_department = Department("Computer Science")
 
 # create course
course1 = Cource("Python")
course2 = Cource("Java")
course3 = Cource("Machine learning")

# create add course
cs_department.add_cource(course1)
cs_department.add_cource(course2)
cs_department.add_cource(course3)

# create instructor
instructor = Instructor("Dr. Sarah Johnson" , 30 , 75000)
instructor.assigncourse(course1)
instructor.assigncourse(course2)
instructor.assigncourse(course3)

# craete student
student = Student("Ali" , 20 , 123)
student.add_regestration(course1)



print("\n📚 Department Information")
print("=" * 40)
print(f"🏛️  Department Name: {cs_department.name}")
print(f"📚 Total Courses  : {len(cs_department.cources)}")
print("=" * 40)

print("\n👨‍🏫 Instructor Information")
print("=" * 40)
print(f"👤 Name           : {instructor.name}")
print(f"🎂 Age            : {instructor.age}")
print(f"💰 Salary         : ${instructor.salary:,.2f}")
print(f"📚 Teaching Courses:")
for course in instructor.cources:
    print(f"   • {course.name}")
print("=" * 40)

print("\n📘 Course Information")
print("=" * 40)
for course in cs_department.cources:
    print(f"\n📚 Course: {course.name}")
    if course.instructor:
        print(f"👨‍🏫 Instructor: {course.instructor[0].name}")
    else:
        print("👨‍🏫 Instructor: Not Assigned")
    print(f"👥 Enrolled Students: {len(course.students)}")
    print("-" * 30)

print("\n🧑‍🎓 Student Information")
print("=" * 40)
print(f"👤 Student Name    : {student.name}")
print(f"🎂 Student Age     : {student.age}")
print(f"🎓 Roll Number     : {student.rollnumber}")
print(f"📚 Enrolled Course : {[c.name for c in student.cources][0]}")
print("=" * 40) 

