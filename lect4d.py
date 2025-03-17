students = [ ["Layan Alaa","DSAI",12,13],
            ["Lana Bibars","CS",13,15],
            ["Raghad Saed","SE",16,14],
            ["Rashid Qaisi","DSAI",13,17] ]

students_s1 = list(sorted(students, key=lambda s: s[0].split()[1]))
students_s2 = list(sorted(students, key=lambda s: s[2]+s[3]))
students_s2 = list(reversed(sorted(students, key=lambda s: s[2]+s[3])))

print(students_s1)
print(students_s2)


