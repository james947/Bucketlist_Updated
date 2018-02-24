from flask import Flask,redirect,render_template,request, url_for, flash
from .users import User,Bucketlist
from datetime import datetime

app = Flask(__name__)

#an empty dict to store users
USERS=[]

#an empty dict to store posts
POSTS=[]

@app.route('/')
def root():
    return redirect(url_for('index')) 
#checks user login
@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        for user in USERS:
            if user.username == request.form['username'] and user.password == request.form['password']:
                return redirect(url_for('dashboard'))
            else:
                flash("invalid user credentials please try again")   
    return  render_template('index.html')

#adds user in the list
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['password']
        password = request.form['password']
        #store form data received
        new_user = User(username,email,password)
        #append the form data in the list
        USERS.append(new_user)
        #redirect back to the login page
        return redirect(url_for('index'))
    return render_template('signup.html')

#shows all the posts
@app.route('/dashboard')
def dashboard():
    post = POSTS
    return render_template('bucketlist.html', post=post)


#adds activities on post request
@app.route('/dashboard/addActivities', methods = ['GET','POST'])
def addActivities():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        new_post=Bucketlist(title,description,date_posted=datetime.now())
        POSTS.append(new_post)
        return redirect(url_for('dashboard'))
    return render_template('addActivities.html')

@app.route('/delete<int:id>')
def delete(id):
    for id in POSTS:
        POSTS.remove(id)
        return redirect(url_for('dashboard'))



