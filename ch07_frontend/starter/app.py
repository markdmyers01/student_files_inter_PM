"""

    app.py    -   This is the Flask server to run.  You
                  will need to run this server and then go to your
                  browser and browse to localhost:8051


    To get it working properly, however, requires 4 steps to be
    accomplished first:


    1. import the SchoolManager class and call its find() method.
       Can you do this on your own?  If not, refer to the back of the
       student manual


    Perform steps 2 through 4 as described below.

"""

from flask import Flask, render_template, jsonify, Response
from ch07_frontend.starter.schools import SchoolManager

app = Flask(__name__)
database = 'course_data.db'

@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/school/<school_name>', methods=['GET'])
def get_schools(school_name):
    results = None
    try:
        results = [str(school) for school in SchoolManager(database).find(school_name)]
    except Exception as err:
        results = err.args

    resp = jsonify(schools=results, school_name=school_name)
    return Response(resp.data, status=200, mimetype='application/json')


@app.route('/schools/')
def get_all_schools():
    results = None
    try:
        results = {f'{s.fullname} ({s.city})': (s.city, s.state, s.country) for s in SchoolManager(database).get_all_schools()}
    except Exception as err:
        results = err.args

    resp = jsonify(total_schools=len(results), schools=results)
    return Response(resp.data, status=200, mimetype='application/json')


app.run(host='localhost', port=8051)
