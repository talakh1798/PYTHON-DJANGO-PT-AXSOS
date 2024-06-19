from flask import Flask, session, redirect, url_for, render_template, request
import random

app = Flask(__name__)
app.secret_key = 'secret key'  

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['message'] = ''
    return render_template('index.html', message=session['message'])

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    number = session['number']

    if guess < number:
        session['message'] = 'Too low!'
    elif guess > number:
        session['message'] = 'Too high!'
    else:
        session['message'] = 'Correct! The number was {}. Play again?'.format(number)
        session.pop('number') 

    return redirect(url_for('index'))

@app.route('/restart')
def restart():
    session.pop('number', None)
    session['message'] = ''
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
