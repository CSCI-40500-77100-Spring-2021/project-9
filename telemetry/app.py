from flask import Flask

app = Flask(__name__)

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
