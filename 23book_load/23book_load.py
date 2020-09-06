import json
class AddressBook:
    def __init__(self):
        self.records = {}
    def dumps(self):
        return json.dumps(self.records)  
    def loads(self, json_bytes):
        self.records = json.loads(json_bytes)  