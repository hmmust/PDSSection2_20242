import random
#convert input list to dictionary as output
students = [ ["Layan Alaa","DSAI",12,13],
            ["Lana Bibars","CS",13,15],
            ["Raghad Saed","SE",16,14],
            ["Rashid Qaisi","DSAI",13,17] ]
students2 = dict(map(lambda s:(s[0],[s[1],s[2]+s[3]]),students))
student3 = { s[0]:[s[1],s[2]+s[3]] for s in students}
print(students2)
print(students2['Rashid Qaisi'])
#list1 = [(111,['Mohammad',21]),(222,['Zaid',22])]
#dict1 = dict(list1)
#print(dict1)