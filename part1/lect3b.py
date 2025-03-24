students = [ ["Layan","DSAI",2004],
            ["Lana","CS",2004],
            ["Raghad","SE",2005],
            ["Rashid","DSAI",2003] ]
students2  = [ [s[0].lower(),s[1], 2025-s[2] ]
              for s in students ]
print(students2)
student3 =  [s  for s in students2 if s[2]>20 ]
print(student3)
student4 =  [s  for s in students2 if s[1] =='DSAI' ]
print(student4)
student5 =  [s  for s in students2 
             if s[1] in ("CS","SE") and 
             s[0][0] in ("r",'s','t')]
print(student5)