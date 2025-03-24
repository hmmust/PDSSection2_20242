import random
#convert input dict to dictionary as output
students = { "Layan":["DSAI",12,13],
            "Lana":["CS",13,15],
            "Raghad":["SE",16,14],
            "Rashid":["DSAI",13,17] }
students2 = dict(map(lambda s: (s[0],[s[1][0],s[1][1]+s[1][2]]),students.items()))
print(students2)
students3 = dict(map(lambda s: 
    (s[0],[f"{s[0].lower()}@uop.edu.jo",random.randint(100,999)]),students.items()))
print(students3)

#list1 = [(111,['Mohammad',21]),(222,['Zaid',22])]
#dict1 = dict(list1)
#print(dict1)