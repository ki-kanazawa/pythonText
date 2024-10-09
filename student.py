class student:
    def __init__(self,name , grades=None):
        self.name = name
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
    
class GradeBook:
    def __init__(self):
        self.students = {}
    
    def add_student(self, student):
        self.students[student.name] = student

    def remove_student(self , name):
        if name in student.name:
            del self.students[name]

    def get_student_average(self , name):
        student = self.students[name]
        if student:
            return student.get_average()
        else:
            print(f'学生情報{name}見つかりません')
            return None
    def get_class_average(self):
        total,count = 0,0
        for student in self.students.values():
            total += sum(student.grades)
            count += len(student.grades)
        return total / count if count > 0 else 0
    
alice = student("Alice",[90,80,70])
bob = student("Bob", [89,90,70])

gradebook = GradeBook()
gradebook.add_student(alice)
gradebook.add_student(bob)

print(f"Aliceの平均点数：{gradebook.get_student_average('Alice')}")
print(f"クラスの平均点数：{gradebook.get_class_average()}")