students = [ ["Layan","DSAI",12,13],
            ["Lana","CS",13,15],
            ["Raghad","SE",16,14],
            ["Rashid","DSAI",13,17] ]
students2  = { s[0].lower():s[2]+s[3] 
              for s in students
              if s[2]+s[3] > 25}
print(students2)
