from flask import Flask , render_template

app=Flask(__name__)
@app.route('/')
def board(row=8,col=8):
    boxes=int(row)
    boxes=int(col)
    return render_template('checkboard.html', boxes=boxes) 

@app.route('/4')
def board1(row=8,col=4):
    boxes=int(row)
    boxes=int(col)
    return render_template('checkboard.html', boxes=boxes) 

@app.route('/<row>/<col>')
def board2(row,col):
    boxes=int(row)
    boxes=int(col)
    return render_template('checkboard.html', boxes=boxes) 





if __name__=="__main__":
    app.run(debug=True)