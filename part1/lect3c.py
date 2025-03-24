import random
print(random.randint(1000,9999))
students = [ ["Layan","DSAI",2004],
            ["Lana","CS",2004],
            ["Raghad","SE",2005],
            ["Rashid","DSAI",2003] ]
students2  = [ [ f"{s[0].lower()}@uop.edu.jo",
                f"{s[0][0]}{random.randint(1000,9999)}"]
              for s in students ]
print(students2)