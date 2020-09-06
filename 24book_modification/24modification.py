import json
class IncorrectInput(Exception):
    pass
class AddressBook:
    def __init__(self):
        self.records = {}
        self.last_record_id = 0
    def dumps(self):
        return json.dumps(self.records)
    def loads(self, json_bytes):
        self.records = json.loads(json_bytes)
        self.last_record_id = max(self.records.keys()) + 1
    def add(self, record):
        self.records[self.last_record_id] = record  
        self.last_record_id += 1
    def delete(self, record_id: int):
        try:
            key = int(record_id)
            self.records.pop(key)  
        except TypeError:
            raise IncorrectInput(f"Record ID {record_id} is not int")
        except KeyError:
            raise IncorrectInput(f"Record {record_id} not found")
    def update_record(self, record_id, field_idx, value):
        record = self.records[record_id]
        record.update(field_idx, value)