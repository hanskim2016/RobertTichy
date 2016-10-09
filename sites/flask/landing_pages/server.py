from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", phrase="Hello,", times=5)
@app.route('/ninjas/')
def ninjas():
    return render_template("ninjas.html", phrase="Ninjas", times=7)
@app.route('/dojos/new')
def dojo_form():
    return render_template("dojo_form.html")
app.run(debug=True)
