from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    languages = [
    "Python","Javascript","HTML","CSS","C++","RPG","BASIC","VB","Swift","C#",
    "other"
    ]
    locations = [
    "San Jose","Seattle","Chicago","New York City","Dallas","online"
    ]
    return render_template("index.html", languages=languages,
    locations = locations
    )
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/post', methods=['POST'])
def result():
    print "Got Post Info"
    # we'll talk about the following two lines after we learn a little more
    # about forms
    name = request.form['name']
    comments = request.form['comments']
    comments = comments[0:120]
    lang_choice = request.form['language']
    location = request.form['location']

    # redirects back to the '/' route
    return render_template("result.html", name = name, comments = comments, language = lang_choice, studio = location)
app.run(debug=True) # run our server
