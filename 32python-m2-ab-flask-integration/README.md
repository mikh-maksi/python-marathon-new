from flask import Flask, request, jsonify  


class AddressBook:  
&nbsp;&nbsp;&nbsp;&nbsp;def \_\_init\_\_(self):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.records = {}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.last_record_id = 0  
  
&nbsp;&nbsp;&nbsp;&nbsp;def add(self, record):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.records[self.last_record_id] = record  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.last_record_id += 1  
  
&nbsp;&nbsp;&nbsp;&nbsp;def str_search(self, search_str: str):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result = {}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for record_id, record in self.records.items():  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if search_str in record:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result[record_id] = record  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return result  
  
&nbsp;&nbsp;&nbsp;&nbsp;def multiple_search(self, **search_items):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result = {}  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for record_id, record in self.records.items():  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if record.multiple_search(**search_items):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result[record_id] = record  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return result  
  

AB = AddressBook()  
app = Flask("answer")  

  
@app.errorhandler(Exception)  
def handle_exception(e):  
&nbsp;&nbsp;&nbsp;&nbsp;return jsonify(message=str(e))  


@app.route("/ab/search")  
def search():  
&nbsp;&nbsp;&nbsp;&nbsp;search_query = request.args.to_dict()  
&nbsp;&nbsp;&nbsp;&nbsp;search_result = {}  
&nbsp;&nbsp;&nbsp;&nbsp;if "all" in search_query:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pass  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;search_result = AB.str_search(search_query['all'])  
&nbsp;&nbsp;&nbsp;&nbsp;else:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pass  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# PUT YOUR CODE HERE  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;search_result = AB.multiple_search **(\*\*search_query)**          
&nbsp;&nbsp;&nbsp;&nbsp;search_result_dict = {}  
&nbsp;&nbsp;&nbsp;&nbsp;for key, rec in search_result.items():  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;search_result_dict[str(key)] = rec.to_dict()  
&nbsp;&nbsp;&nbsp;&nbsp;response = jsonify(**search_result_dict)  
&nbsp;&nbsp;&nbsp;&nbsp;return response  