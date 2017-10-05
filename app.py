from flask import Flask, request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from flaskrun import flaskrun

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)

    def __init__(self, content):
        self.content = content
        self.done = False

    def __repr__(self):
        return '<Content %s>' % self.content

class OfferHelp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    what = db.Column(db.Text)
    when = db.Column(db.Text)

    def __init__(self, what, when):
        self.what = what
        self.when = when

    def __repr__(self):
        return '<Offer: %s | %s>' % self.what, self.when

db.drop_all()
db.create_all()


@app.route('/')
def tasks_list():
    tasks = Task.query.all()
    return render_template('list.html', tasks=tasks)


@app.route('/task', methods=['POST'])
def add_task():
    content = request.form['content']
    if not content:
        return 'Error'

    task = Task(content)
    db.session.add(task)
    db.session.commit()
    return redirect('/')


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return redirect('/')

    db.session.delete(task)
    db.session.commit()
    return redirect('/')


@app.route('/done/<int:task_id>')
def resolve_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return redirect('/')
    if task.done:
        task.done = False
    else:
        task.done = True

    db.session.commit()
    return redirect('/')

@app.route('/offerhelp')
def offer_help():
    return render_template('offerHelp.html')

@app.route('/addhelp', methods=['POST'])
def addHelp():
   what = request.form['what']
   if not what:
       return "Error: We don't know what you wan't to do. Please share this with us!"
   when = request.form['when']
   if not when:
       return "We appreciate that you wan't to offer your time always. Still please submit a time where you wan't to help others with your valuable time!"

   offerhelp = OfferHelp(what, when)
   db.session.add(offerhelp)
   db.session.commit()

   return redirect('/')
    

if __name__ == '__main__':
    flaskrun(app)
