from flask import Flask , render_template ,request
app=Flask(__name__)
@app.route('/')
def Dojo():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['languages']
    gender = request.form['gender']
    comment = request.form['comment']
    return render_template('result.html', name=name, location=location, language=language, gender=gender, comment=comment )


if __name__=="__main__":
    app.run(debug=True)
