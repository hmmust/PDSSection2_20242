students = [] #list()

students.append(["Lana",20,25])
students.append(["AbedAlraouf",20,24])
students.append(("Raghad",21,23.5))
print(students)

for i in range(0,len(students)):
    print(students[i][0])

for s  in students:
    print(s[0])