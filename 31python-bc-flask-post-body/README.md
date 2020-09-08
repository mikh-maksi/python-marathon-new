from flask import Flask, request


app = Flask("answer")


@app.route("/ab/record/<record_id>/field", methods=["POST"])
def new_field(record_id):
&nbsp;&nbsp;&nbsp;&nbsp;field_name = **request.json["name"]**
&nbsp;&nbsp;&nbsp;&nbsp;return f"Name {field_name}, record: {record_id}"
