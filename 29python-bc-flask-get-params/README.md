from flask import Flask, request, jsonify

app = Flask("answer")

@app.route("/ab/search")
def search():
&nbsp;&nbsp;&nbsp;&nbsp;search_query = request.args.to_dict()
&nbsp;&nbsp;&nbsp;&nbsp;response = jsonify(keys=list(search_query.keys()), values=list(search_query.values()))
&nbsp;&nbsp;&nbsp;&nbsp;return response