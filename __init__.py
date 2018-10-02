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
        #intent_name = req.get('queryResult').get('intent').get('displayName')
        source = req.get('originalDetectIntentRequest').get('source')
        #time = req.get('queryResult').get('parameters').get('time')
        time = req.get('queryResult').get('outputContexts')[0].get('parameters').get('time.original')
        print(req)
        
        response = {
            "fulfillmentText": "You choose " + time + ". No problem！",
        }
        if source == 'line' or source=='facebook':
            return make_response(jsonify(response))
        else:
            return make_response(jsonify({
                "fulfillmentText": "Sorry: this channel will not process the current intent",
            }))

if __name__ == "__main__":
    app.run(debug=True)
