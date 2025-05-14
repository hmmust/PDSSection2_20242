import json
ali= {'name':'Ali',"Age":20,'Major':'DSAI',
      'Married':False,'NoOfChildren':None}
Students= [ {'name':'Ali',"Age":20,'Major':'DSAI',
            'Married':False,'NoOfChildren':None},
           {'name':'Abedraheem',"Age":21,'Major':'DSAI',
            'Married':True,'NoOfChildren':0}
          ]
file1 = open("./part5/students.json",mode='w')
json.dump(Students,file1)
file1.close()
with open("./part5/students.json",mode='w') as file1:
      json.dump(Students,file1)