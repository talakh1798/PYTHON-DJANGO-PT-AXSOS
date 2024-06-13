from flask import Flask, render_template

app=Flask(__name__)
@app.route('/play')
def play_ground():
    return render_template("playground1.html" , title="palyground1" )

@app.route('/play/<num>')
def play_ground2(num):
    return render_template("playground2.html" ,count=int(num) )

@app.route('/play/<num>/<color>')
def play_ground3(num , color ):
    return render_template("playground3.html", count=int(num), color_box=(color))

if __name__=="__main__":
    app.run(debug=True)