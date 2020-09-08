from flask import Flask, jsonify


REGISTERED_FIELDS = ["Name", "Surname", "Email", "Phone", "Rate"]


app = Flask("answer")


@app.route("/fields")
def fields():
&nbsp;&nbsp;&nbsp;&nbsp;response = jsonify(**REGISTERED_FIELDS**)
&nbsp;&nbsp;&nbsp;&nbsp;return response
