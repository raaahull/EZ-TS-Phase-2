student_grade=[]
student_grade.append((1,"Rahul"))
student_grade.append((4,"nani"))
student_grade.sort(reverse=True)
print("yes")
print(student_grade)
student_grade.append((3, "vishwak"))
student_grade.sort(reverse=True)
student_grade.append((2, "shiva"))
student_grade.sort(reverse=True)
print("priority wise sorted")
print(student_grade)
print("original queue")
while student_grade:
    print(student_grade.pop())
    