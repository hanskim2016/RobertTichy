from flask import Flask, render_template, session, request, redirect
import random, os
app = Flask(__name__)
app.secret_key =os.urandom(48)
@app.route('/')
def index():
    pyNumber = random.randrange(0, 101)

    pyFlag = 'start'
    pyGameOn = True
    counter = 0

    session['pyNum'] = pyNumber
    session['pyGameOn'] = pyGameOn
    session['pyFlag'] = pyFlag

    return render_template("index.html" , gameOn = pyGameOn , flag = pyFlag)

@app.route('/guess', methods=['POST'])
def processGuess():
    if 'pyFlag' in session:
        pyFlag = session['pyFlag']
        pyNumber = session['pyNum']
        pyGameOn = session['pyGameOn']
    else:
        print "CRAP! no pyFlag ?!"
        return redirect('/')

    pyGuess = int(request.form['guess'])
    pyGameOn = True


    # processing logic here and only passing low/high into the page
    # so users cannot get any access to the number
    if (pyGuess < int(pyNumber)):
        pyFlag = "low"
    elif (pyGuess > int(pyNumber)):
        pyFlag = "high"
    elif (pyGuess == int(pyNumber)):
        pyFlag = "win"
        pyGameOn = False

    session['pyFlag'] = pyFlag
    session['pyGameOn'] = pyGameOn

    return render_template("index.html" , gameOn = pyGameOn , flag = pyFlag)

@app.route('/quit', methods=['POST'])
def pleadToContinue():

    if 'pyFlag' in session:
        pyFlag = session['pyFlag']
        pyNumber = session['pyNum']
        pyGameOn = session['pyGameOn']
    else:
        print "@2 CRAP! no pyFlag ?!"
        return redirect('/')

    pyFlag="quitting"
    pyGameOn=False

    session['pyFlag'] = pyFlag
    session['pyGameOn'] = pyGameOn

    return render_template("index.html" , gameOn = pyGameOn , flag = pyFlag)

@app.route('/done')
def done():
    session.pop('pyNum')
    session.pop('pyFlag')
    session.pop('pyGameOn')

    return render_template("done.html")
app.run(debug=True)
