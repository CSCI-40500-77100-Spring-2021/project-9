from datetime import datetime
import json
import os

from flask import abort, Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
db = SQLAlchemy(app)

class Usage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(255), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    duration_ms = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __str__(self):
        return f"Usage#{self.id}: {self.method} {self.size} {self.duration_ms} {self.created_at}"

    class UsageEncoder(json.JSONEncoder):
        def default(self, obj):
            fields = {}
            for field in ['id', 'method', 'size', 'duration_ms', 'created_at']:
                attr = obj.__getattribute__(field)
                try:
                    json.dumps(attr)
                    fields[field] = attr
                except TypeError:
                    fields[field] = str(attr)
            return fields


# The endpoint to record metrics.
# Method: POST
# Arguments in body:
#   * voting method
#   * dataset size
#   * duration of the calculation?
# For now, just have the server print out this data and respond with HTTP code
# 200 OK. Later, we'll hook this up to a database.
@app.route("/record", methods=['POST'])
def record():
    try:
        usage = Usage(method=request.form['method'],
                      size=request.form['size'],
                      duration_ms=request.form['duration_ms'])
    except KeyError:
        abort(400)

    db.session.add(usage)
    db.session.commit()
    return "OK"

@app.route("/drop", methods=['GET'])
def drop():
    num = Usage.query.delete()
    db.session.commit()
    return str(num)

@app.route("/data", methods=['GET'])
def data():
    usages = Usage.query.all()
    return json.dumps(usages, cls=Usage.UsageEncoder)

@app.route("/data/human", methods=['GET'])
def data_human():
    usages = Usage.query.all()
    return "\n".join([str(x) for x in usages])
