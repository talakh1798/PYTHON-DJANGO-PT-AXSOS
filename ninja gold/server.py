from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
    return render_template("index.html", gold=session['gold'], activities=session['activities'])

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    if building == 'farm':
        gold_earned = random.randint(10, 20)
    elif building == 'cave':
        gold_earned = random.randint(5, 10)
    elif building == 'house':
        gold_earned = random.randint(2, 5)
    elif building == 'casino':
        gold_earned = random.randint(-50, 50)
    
    session['gold'] += gold_earned
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if gold_earned >= 0:
        activity = f"Earned {gold_earned} golds from the {building}! ({timestamp})"
    else:
        activity = f"Entered a casino and lost {abs(gold_earned)} golds... Ouch. ({timestamp})"
    
    session['activities'].append(activity)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)