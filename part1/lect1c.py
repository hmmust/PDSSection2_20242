students = {} #dict()

students[1001]= ["Lana",20,25]
students[1002]= ["AbedAlraouf",20,24]
students[1003]= ("Raghad",21,23.5)
print(students)
print(students[1002])

for s  in students:
    print(s,students[s])
    
for (k,v) in students.items():
    print(k,v)
    
x,y = (10,20)
