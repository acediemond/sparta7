from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('Homework1.html')



@app.route('/music')
def music():
   return 'music!'



app.run('0.0.0.0',port=5000,debug=True)
