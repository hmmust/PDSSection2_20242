students = [ ["Layan","DSAI",12,13],
            ["Lana","CS",13,15],
            ["Raghad","SE",16,14],
            ["Rashid","DSAI",13,17] ]
calc_marks= lambda s:s[2]+s[3]
print(calc_marks(students[0]))
generate_email= lambda s:s[0].lower()+"@uop.edu.jo"
print(generate_email(students[0]))
isPassed = lambda s: s[2]+s[3] >=25
print(isPassed(students[0]))
