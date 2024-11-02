def calc_student_grades(student):
    name=student['name']
    grades=[student['math'],student['science'],student['english']]
    avg_grade=sum(grades)/len(grades)
    return name,avg_grade

def calc_class_avg(students):
    total_grade=0
    num_grade=0
    for student in students:
        for key,value in student.items():
            if key!='name':
                total_grade+=value
                num_grade+=1
    return total_grade/num_grade


students=[]
num_students=int(input("enter number of students "))
for i in range(num_students):
    name=input("student name ")
    math=float(input("math "))
    english=float(input("english "))
    science=float(input("science "))
    student={'name':name,'math':math,'english':english,'science':science}
    students.append(student)

print("grades of each student ")
for student in students:
    print(calc_student_grades(student))

print("class average ",calc_class_avg(students))
