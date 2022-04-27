from flask import Flask, render_template 
app = Flask(__name__)                     
    
@app.route('/')                           
def index():
    return render_template('index.html', rows=8, cols=8) 

@app.route('/<int:x>')                           
def rows(x):
    return render_template('index.html', rows=x, cols=8) 

@app.route('/<int:x>/<int:y>')                           
def cols(x,y):
    return render_template('index.html', rows=x, cols=y) 

@app.route('/<int:x>/<int:y>/<string:color1>')                           
def color1(x,y,color1):
    return render_template('index.html', rows=x, cols=y, color1=color1) 

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')                           
def color2(x,y,color1,color2):
    return render_template('index.html', rows=x, cols=y, color1=color1, color2=color2) 

if __name__=="__main__":
    app.run(debug=True)  