class Student:
    def _init_(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def _repr_(self):
        return f"Student(name={self.name}, age={self.age}, student_id={self.student_id})"

def create_students():
    students_dict = {}
    num_students = int(input("How many students do you want to create? "))
    
    for i in range(num_students):
        print(f"Enter details for student {i + 1}:")
        name = input("Name: ")
        age = int(input("Age: "))
        student_id = input("Student ID: ")
        
        student = Student(name, age, student_id)
        students_dict[student_id] = student
    
    return students_dict

def main():
    students = create_students()
    for student_id, student in students.items():
        print(f"Student ID: {student_id}, {student}")

if _name_ == "_main_":
    main()
