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


class HelpOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    what = db.Column(db.Text)
    when = db.Column(db.Text)

    def __init__(self, what, when):
        self.what = what
        self.when = when

    def __repr__(self):
        return '<Offer: %s | %s>' % self.what, self.when


db.create_all()


@app.route('/')
def map():
    return render_template('base.html')


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
    event = HelpRequest(datetime.strptime(start_time, fmt),
                        datetime.strptime(end_time, fmt))
    db.session.add(event)
    db.session.commit()
    return redirect('/helpRequestList')


@app.route('/HelpOfferList')
def offer_help():
    offers = HelpOffer.query.all()
    return render_template('helpOfferList.html', offers=offers)


@app.route('/HelpOffer', methods=['POST'])
def addHelp():
    what = request.form['what']
    if not what:
        return "Error: We don't know what you wan't to do. Please share this with us!"
    when = request.form['when']
    if not when:
        return "We appreciate that you wan't to offer your time always. Still please submit a time where you wan't to help others with your valuable time!"

    offerhelp = HelpOffer(what, when)
    db.session.add(offerhelp)
    db.session.commit()

    return redirect('/HelpOfferList')


if __name__ == '__main__':
    flaskrun(app)
