import json  
class AddressBook:  
&nbsp;&nbsp;&nbsp;&nbsp;def \_\_init\_\_(self):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.records = {}  
&nbsp;&nbsp;&nbsp;&nbsp;def dumps(self):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return json.dumps(**self.records**)  
&nbsp;&nbsp;&nbsp;&nbsp;def loads(self, json_bytes):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.records = json.loads(json_bytes)  