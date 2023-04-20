student_scores = input("Input a list of student scores: ").split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])

x=0
for i in student_scores:
    if i > x:
        x = i

print(f"The highest score in the class is: {x}")
