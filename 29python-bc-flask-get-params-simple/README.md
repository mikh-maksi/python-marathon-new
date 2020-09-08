from flask import Flask, request, jsonify  

app = Flask("answer")  

@app.route("/ab/id")  
def get_id():  
&nbsp;&nbsp;&nbsp;&nbsp;response = **request.args["id"]**  
&nbsp;&nbsp;&nbsp;&nbsp;return response  

## Уточнить сам код 