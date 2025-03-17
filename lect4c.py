students = [ ["Layan Alaa","DSAI",12,13],
            ["Lana Bibars","CS",13,15],
            ["Raghad Saed","SE",16,14],
            ["Rashid Qaisi","DSAI",13,17] ]

filter1 = lambda s: s[2]+s[3] >25
students_f1 = list(filter(filter1,students))
students_f2 = list(filter(lambda s: s[1] == 'DSAI',students))
#students_f1 = [* filter(filter1,students)]
print(students_f1)
print(students_f2)

