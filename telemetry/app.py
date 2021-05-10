from flask import Flask, jsonify, request
from tests.test_fptp import TestFPTP
from votelib.irv import irv_test
app = Flask(__name__)
fptp = TestFPTP()
irv = irv_test()

# The endpoint to record metrics.
# Method: POST
# Arguments in body:
#   * voting method
#   * dataset size
#   * duration of the calculation?
# For now, just have the server print out this data and respond with HTTP code
# 200 OK. Later, we'll hook this up to a database.
@app.route("/record")
def record():
    return "Hello World"


@app.route('/get/voting/results', methods=['POST'])
def get_voting_results():
    values = request.get_json()
    required = ['voting_method']
    if not all(keys in values for keys in required):
        return 'Missing request info', 400
    voting = values['voting_method']
    if voting == "FPTP":
        result = fptp.test_fptp_tie()
    else:
        result = irv.irv()
    response = {'Winner': result}
    return jsonify(response), 201
