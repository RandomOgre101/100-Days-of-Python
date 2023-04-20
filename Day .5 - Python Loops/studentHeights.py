student_heights = input("Input a list of student heights: ").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])

totalHeight = 0
for i in student_heights:
    totalHeight += i

totalStudents = 0
for j in student_heights:
    totalStudents += 1

avg = totalHeight/totalStudents

print(round(avg))
