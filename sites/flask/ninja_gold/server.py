from flask import Flask, render_template, session, request, redirect
import random, os
app = Flask(__name__)
app.secret_key =os.urandom(48)
print app.secret_key
@app.route('/')
def index():
    print "index()"
    if 'score' in session:
        print "playing"
        score = session['score']
        lines = session['lines']
    else:
        print "starting"
        session['score'] = 0
        session['lines'] = []
        score = 0
        lines = []

    return render_template("index.html" , score = score , transactions = lines)
@app.route('/earn', methods=['POST'])
def earn():
    print "earn()"
    if 'score' in session:
        score = int(session['score'])
    else:
        print "CRAP! no score ?!"
        return redirect('/')

    lines = session['lines']
    line = {}

    activity = request.form['hidden']
# set rewards for farming
    if activity == 'farm':
        reward = random.randrange(10,20)
        message = "Earned {r} gold coins for farming.\n".format(r=reward)
# set rewards for spelunking
    if activity == 'cave':
        reward = random.randrange(5,10)
        message = "Earned {r} gold coins while spelunking in a pirate cave.\n".format(r=reward)
# set rewards for raiding a castle
    if activity == 'raid':
        reward = random.randrange(2,5)
        message = "Stole {r} gold coins while raiding a castle.\n".format(r=reward)

    score = score + reward
    # build the line {} for insertion into the lines []
    line['activity'] = message
    line['reward'] = reward
    line['balance'] = score
    # insert the most recent activity at the top of the ledger
    lines.insert(0,line)

    session['score'] = score
    session['lines'] = lines

    return redirect('/')

@app.route('/gamble')
def gambling():
    print "gambling()"
    if 'score' in session:
        score = int(session['score'])
    else:
        print "CRAP! no score ?!"
        return redirect('/')

    lines = session['lines']

    reward = random.randrange(0,50)
    message = "Won {r} gold coins gambling at a casino.".format(r=reward)
    if random.randrange(0,2) >=1:
        message = "Lost {r} gold coins gambling at a casino.".format(r=reward)
        reward= -reward

    score = score + reward

    line = {}
    line['activity'] = message
    line['reward'] = reward
    line['balance'] = score
    lines.insert(0,line)

    session['score'] = score
    session['lines'] = lines

    return redirect('/')
app.run(debug=True)
