from flask import Blueprint, render_template,request,flash, jsonify,redirect,url_for
from flask_login import  login_required, current_user
from . import db
from .models import Task 
import json

views=Blueprint('views',__name__)


@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        task = request.form.get('task')

        new_task = Task(data=task, user_id=current_user.id)
       
      
        db.session.add(new_task)
        db.session.commit()
        print('task added!')
    return render_template("home.html",user=current_user)





@views.route('/delete-task', methods=['POST'])
def delete_task():
    
    task = json.loads(request.data)
    taskId = task['taskId']
    task= Task.query.get(taskId)
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()

    return jsonify({})


@views.route('/update-task', methods=['POST'])
def update_task():
    task = json.loads(request.data)
    taskId = task['taskId']
    task= Task.query.get(taskId)
    if task.user_id == current_user.id:
        task.complete=True
        db.session.commit()

    return jsonify({})







@views.route("/", methods=['GET','POST'])
def update():
    
    task = Task.query.get(task.complete)
    task.complete = not task.complete
  
    db.session.commit()
    return redirect(url_for("home.html", user=current_user))

