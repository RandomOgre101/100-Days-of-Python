import random

# numbers = [1,2,3]
# new_list = [n+1 for n in numbers]
# print(f"{new_list}")

# name = "Rishi"
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [n*2 for n in range(1,5)]
# print(new_list)

#           Conditional List Comprehension
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_list = [name.upper() for name in names if len(name) > 5]
# print(new_list)

#           Dictionary Comprehension
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)

# passed_students = {student:score for (student,score) in student_scores.items() if score >= 70}
# print(passed_students)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "scores": [56, 76, 98]
}

# for (k,v) in student_dict.items():
#     print(k)

# print(student_dict)

import pandas as pd

df = pd.DataFrame(student_dict)
# print(df)

#       Inbuilt Loop
for (index, row) in df.iterrows():
    print(row)

for (index, row) in df.iterrows():
    if row.student == "Angela":
        print(row.scores)
