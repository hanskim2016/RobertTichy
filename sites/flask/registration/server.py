from flask import Flask, render_template, request, redirect, session
import os, re
app = Flask(__name__)
app.secret_key=os.urandom(128)
# our index route will handle rendering our form
@app.route('/')
def index():

    if 'errors' not in session:
        session['errors'] = []

    return render_template("user_reg.html",errors = session['errors'])
@app.route('/signup', methods=['POST'])
def signup():
    print "Got Post Info"

    pwd_1 = request.form['pwd_1']
    pwd_2 = request.form['pwd_2']
    first = request.form['first_name']
    last = request.form['last_name']
    user_id = request.form['email_id']
    #
    print first, last, user_id,len(pwd_1),len(pwd_2)
    #
    session['errors'] = []
    #
    session['pwd_1'] = pwd_1
    session['pwd_2'] = pwd_2
    session['first_name'] = first
    session['last_name'] = last
    session['user_id'] = user_id

    if pwd_1 != pwd_2:
        session['errors'].append('Passwords do not match, please reenter both.')
        session['pwd_1'] = ''
        session['pwd_2'] = ''
    if not re.search(r'[0-9]',pwd_1):
        session['errors'].append('Password should contain at least one number.')
    if not re.search(r'[A-Z]',pwd_1):
        session['errors'].append('Password should contain at least one uppercase.')
    if not re.search(r'[a-z]',pwd_1):
        session['errors'].append('Password should contain at least one lowercase.')
    if not re.search(r'[~!@#$%^&*_+]',pwd_1):
        session['errors'].append('Password should have at least one of these: ~!@#$%^&*_+')
    if len(first)<1:
        session['errors'].append('Please enter a first name.')
    if len(last)<1:
        session['errors'].append('Please enter a last name.')
    if len(user_id)<1:
        session['errors'].append('Please enter an email address.')
    if not re.search(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$',user_id):
        session['errors'].append('Enter a valid email address.')

    print "session['errors'] = ",session['errors']
    if not session['errors']:
        print "No Errors- render success"
        return render_template('success.html')

    # redirects back to the '/' route
    return redirect('/')
app.run(debug=True) # run our server
