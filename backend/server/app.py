from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import kwic

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/input", methods=['GET','POST'])
@cross_origin()
def process_input():
    result = request.get_json()
    obj = kwic.KWIC()
    obj.input(result)
    obj.circular_shift()
    obj.make_alpha()
    out = obj.output()
    return {
        "data": out,
    }

if __name__ == "__main__":
    app.run()