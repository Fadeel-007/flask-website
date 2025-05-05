from app import app
from flask import render_template,flash,redirect,url_for
from app.forms import LoginForm

@app.route('/login', methods= ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))





@app.route('/')
@app.route('/index')
def index():
    user = {"username" :  "kira" }
    return render_template('index.html',title="home", user=user )
    
