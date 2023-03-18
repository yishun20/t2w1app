from flask import Flask, render_template, request
#flask creates an app, render allw to, request will allw the form to be process (all 3 is required for anapp !!)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  name, = None
  gender = None
  colour= None
  hobbies = None
  feedback = None
  if request.form == 'POST':
    name = request.form['name']
    gender = request.form['gender']
    colour = request.form['colour']
    hobbies = request.form.getlist('hobbies')
    feedback = request.form['feedback']
#will basically take the value of the text box n area and assign to each variavle and end up in html
    
    return render_template('index.html', name=name, gender=gender, colour=colour, hobbies=hobbies, feedback=feedback)
#index: ownself name (will connect to html)

