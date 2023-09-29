from flask import Flask, request, render_template
from collections import Counter

app = Flask(__name__,template_folder="templates")

@app.route('/')
def quiz():
    return render_template('form.html')

@app.route('/form', methods=['POST'])
def form():
    answers = []
    answers.append(request.form['q1'])
    answers.append(request.form['q2'])
    answers.append(request.form['q3'])
    answers.append(request.form['q4'])
    answers.append(request.form['q5'])
    a=0
    b=0
    for i in answers:
        if i=="a":
            a=a+1
        else:
            b=b+1    

    if(a>b):
        return render_template('medical.html', answers=answers)
    else:
        return render_template('non_medical.html', answers=answers)










@app.route('/non_med', methods=['POST'])
def non_med():
    answers = []
    answers.append(request.form['q1'])
    answers.append(request.form['q2'])
    answers.append(request.form['q3'])
    answers.append(request.form['q4'])
    answers.append(request.form['q5'])
    a=0
    b=0
    for i in answers:
        if i=="a":
            a=a+1
        else:
            b=b+1    

    if(a>b):
        print("engineering")
        return render_template('1.html', answers=answers)
    else:
        return render_template('1.html', answers=answers) 
        print("non engineering")      

@app.route('/med', methods=['POST'])
def med():
    answers = []
    answers.append(request.form['q1'])
    answers.append(request.form['q2'])
    answers.append(request.form['q3'])
    answers.append(request.form['q4'])
    answers.append(request.form['q5'])
    a=0
    b=0
    for i in answers:
        if i=="a":
            a=a+1
        else:
            b=b+1    

    if(a>b):
        print("MBBS")
        return render_template('1.html', answers=answers)
    else:
        return render_template('1.html', answers=answers) 
        print("non MBBS")      

if __name__ == '__main__':
    app.run(debug=True)