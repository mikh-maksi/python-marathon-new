import json  
b = '{"Name":"Serhii","City":"Kyiv","Skill":"Python","Phone":"+380631234567","Rate":2700,"Email":"serhshems@gmail.com"}'  
c = **json.loads(b)**  
print(c['City'])  
  
record = {}  
record['Name'] = "Serhii"  
record['City'] = "Kyiv"  
record['Skill'] = "**Python**"  
d = json.dumps(record)  
print(d)
