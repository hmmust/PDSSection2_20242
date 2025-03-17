import random
students = [ ["Layan Alaa","DSAI",12,13],
            ["Lana Bibars","CS",13,15],
            ["Raghad Saed","SE",16,14],
            ["Rashid Qaisi","DSAI",13,17] ]

student2 = [ [s[0],s[1],s[2]+s[3]] for s in students]
students3 = list(map(lambda s:[s[0],s[1],s[2]+s[3]],students))

gep = lambda s: [f"{s[0].lower() }@uop.edu.jo",
                 f"{s[0][0].lower()}{random.randint(100,999)}" ]
students4 = list(map(gep,students))
print(student2)
print(students3)
print(students4)
