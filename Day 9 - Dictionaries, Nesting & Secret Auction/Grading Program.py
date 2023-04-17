student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

student_grades = {}

for score in student_scores:
    if student_scores[score] in range(91,101):
        student_grades[score] = "Outstanding"

    elif student_scores[score] in range(81,91):
        student_grades[score] = "Exceeds Expectations"

    elif student_scores[score] in range(71,81):
        student_grades[score] = "Acceptable"
    elif 71 > student_scores[score]:
        student_grades[score] = "Fail"


print(student_grades)

#Nesting
travel_log = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12}
}

#nesting dict in list
travel_log2 = [
    {
    "country": "France",
     "cities_visited":["Paris", "Lille", "Dijon"], 
     "total_visits": 12
    },
    {
    "country": "Germany",
    "cities_visited":["Berlin", "Munich", "Leipzig"],
    "total_visits": 5
    }
]

print(travel_log2)

    
