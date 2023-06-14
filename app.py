from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@db/appdb'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete(task_id):
    task = Task.query.get(task_id)
    task.completed = True
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
