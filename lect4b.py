import random
students = [ ["Layan","DSAI",12,13],
            ["Lana","CS",13,15],
            ["Raghad","SE",16,14],
            ["Rashid","DSAI",13,17] ]
def generate_email(s,y):
    return f"{ y(s[0]) }@uop.edu.jo"
generate_user = lambda s: f"{s.lower()}.{s.lower()}"
generate_user2 = lambda s: f"{s[0].lower()}{random.randint(100,999)}"
print(generate_email(students[0],generate_user))
print(generate_email(students[0],generate_user2))
