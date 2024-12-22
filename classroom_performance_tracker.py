class Student:
    def __init__(self, name, marks_list):
        self.name = name
        self.avg_marks = self.avg(marks_list)

    def avg(self, marks_list):
        return sum(marks_list) / len(marks_list)
    
    def get_avg(self):
        return self.avg_marks
    
def get_top_performer(students):
    return max(students.items(), key=lambda s: s[1].get_avg())[0]

students = {}
no_of_students = int(input("Enter the number of students: "))
for  i in range(no_of_students):
    name = input("\nEnter the name of student {}: ".format(i+1))
    marks = list(map(int, input("Enter the marks of {} separated by space: ".format(name)).split()))
    students[name] = Student(name, marks)

print("\nAverage Marks: ",dict({name: obj.get_avg() for name,obj in students.items()}))
top_performer = get_top_performer(students)
print("Top Performer:",top_performer)