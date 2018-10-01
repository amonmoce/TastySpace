from flask import Flask, Response
from flask import jsonify
from flask import make_response
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return Response("TastySpace is up and running!"), 200
    else:
        req = request.get_json(force=True)
        intent_name = req.get('queryResult').get('intent').get('displayName')
        fulfillmentText = req.get('queryResult').get('fulfillmentText')
        response = {
            "fulfillmentText": fulfillmentText + '(' + intent_name + ')',
        }


if __name__ == "__main__":
    app.run(debug=True)
