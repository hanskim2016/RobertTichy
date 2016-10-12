from flask import Flask, render_template, redirect
app = Flask(__name__)
@app.route('/')
def start():
    return render_template('index.html')    # Render the template and return it!
@app.route('/ninjas')
def ninjas():
    return render_template('images.html',image='TMNTs.gif')
@app.route('/ninjas/<arg>')
def ninjas_wargs(arg):
    print arg

    arg = arg.lower()
    print arg
    print (arg=='blue')

    image='April.jpg'

    if arg=='blue':
        image='Leonardo.jpg'
    if arg=='red':
        image='Raphael.png'
    if arg=='orange':
        image='Michelangelo.jpg'
    if arg=='purple':
        image='Donatello.jpeg'

    return render_template('images.html',image=image)
app.run(debug=True)      # Run the app in debug mode.
