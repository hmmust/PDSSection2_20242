import random
import sys
#print(sys.argv)
student= sys.argv[1]
username = f"{student.lower().replace(" ",".") }@uop.edu.jo"
password= f"{student.lower()[0]}{random.randint(100,999)}"
print(username,password)