from cmath import phase
from flask import Flask, render_template 

app = Flask(__name__)    

@app.route('/checker')    
def checkerNoCoord():
    return render_template("check.html", xCoord=1, yCoord=1)

@app.route('/checker/<int:xCoord>')    
def checkerXCoord(xCoord):
    return render_template("check.html", xCoord=xCoord, yCoord=1)

@app.route('/checker/<int:xCoord>/<int:yCoord>')
def checkerXYCoord(xCoord, yCoord):
    return render_template("check.html", xCoord=xCoord, yCoord=yCoord)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
