import json

ali= {'name':'Ali',"Age":20,'Major':'DSAI',
      'Married':False,'NoOfChildren':None}
Students= [ {'name':'Ali',"Age":20,'Major':'DSAI',
            'Married':False,'NoOfChildren':None},
           {'name':'Abedraheem',"Age":21,'Major':'DSAI',
            'Married':True,'NoOfChildren':0}
          ]
print(type(json.dumps(ali))) # string
print(json.dumps(Students)) # string
json_string = '{"name":"Ali", "age":25,"married":true}'
print(type(json.loads(json_string)))