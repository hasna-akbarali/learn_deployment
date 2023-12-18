from flask import Flask,render_template

#initialize the app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact-us')
def contact():
    return render_template('contact-us.html')

@app.route('/courses')
def courses():
    return render_template('course.html')

@app.route('/feedback')
def feedback():
    return "Provide us with your valuable feedback"

#run the app
app.run()

'''
http://127.0.0.1:5000/

http - hyptertext transfer protocol
121.0.0.1 - IP Address
5000 - port
/ - route
'''