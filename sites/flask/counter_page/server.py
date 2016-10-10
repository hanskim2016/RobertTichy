from flask import Flask, redirect, render_template, request, session
import os
app = Flask(__name__)
app.secret_key =os.urandom(48)
print app.secret_key
@app.route('/')
def index():
    print "index()"
    if 'counter' in session:
        session['counter'] = int(session['counter']) + 1
    else:
        session['counter'] = 0
    return render_template("index.html")
@app.route('/skip')
def skip():
    print "skip()"
    session['counter'] = int(session['counter']) + 1
    return redirect('/')
@app.route('/reset')
def reset():
    print "reset()"
    session['counter'] = '-1'
    return redirect('/')
app.run(debug=True)
