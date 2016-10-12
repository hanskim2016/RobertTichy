from flask import Flask, render_template, request, redirect, flash, session
import os, random
app = Flask(__name__)
app.secret_key=os.urandom(128)
# our index route will handle rendering our form
@app.route('/')
def index():

    if 'errors' not in session:
        session['errors'] = False

    languages = [
    "Python","Javascript","HTML","CSS","C++","RPG","BASIC","VB","Swift","C#",
    "other"
    ]
    locations = [
    "San Jose","Seattle","Chicago","New York City","Dallas","online"
    ]
    return render_template("index.html",
                            errors = session['errors'],
                            languages = languages,
                            locations = locations
    )

@app.route('/post', methods=['POST'])
def validate():
    print "Got Post Info"

    name = request.form['name']
    comments = request.form['comments']
    lang_choice = request.form['language']
    location = request.form['location']

    session['errors'] = False

    session['comments'] = comments
    session['name'] = name
    session['language'] = lang_choice
    session['location'] = location

    if len(name) < 1:
        #error name too short
        flash("Name cannot be empty.")
        session['errors'] = True
    if len(comments) < 1:
        #comments too short
        flash("Comments are required.  Thank you.")
        session['errors'] = True
    if len(comments) > 120:
        #comments too long
        flash("Comments need to be kept under 120 characters.  Yours are {l}.".format(l=len(comments)))
        session['errors'] = True

    #If no errors in form then proceed to write the data to the session or DB.
    #Otherwise let everything fall down to the return redirect
    if session['errors'] == False:
        print "No Errors, write to session"
        return render_template('result.html')

    # redirects back to the '/' route
    return redirect('/')
app.run(debug=True) # run our server
