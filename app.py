from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flaskrun import flaskrun

from flask_bootstrap import Bootstrap

from datetime import datetime


app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class HelpRequest(db.Model):
    tablename__ = 'helprequests'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.Date)
    end_time = db.Column(db.Date)

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


db.create_all()


@app.route('/helpRequestList')
def need_help_events_list():
    events = HelpRequest.query.all()
    return render_template('helpRequestList.html', events=events)


@app.route('/helpRequest', methods=['POST'])
def add_help_event():
    start_time = request.form['Start Time']
    end_time = request.form['End Time']
    if not start_time:
        return 'Error'

    if not end_time:
        return 'Error'

    fmt = "%Y-%m-%d"
    event = HelpRequest(datetime.strptime(start_time, fmt), datetime.strptime(end_time, fmt))
    db.session.add(event)
    db.session.commit()
    return redirect('/helpRequestList')


@app.route('/')
def map():
    return render_template('base.html')


if __name__ == '__main__':
    flaskrun(app)
