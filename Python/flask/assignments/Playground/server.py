from flask import Flask, render_template 
app = Flask(__name__)                     
    
@app.route('/')                           
def hello_world():
    return render_template('index.html') 

@app.route('/play')                           
def play():
    return render_template('level1.html')  

@app.route('/play/<int:num>')
def repeat(num):
    return render_template('level3.html', num=num)

@app.route('/play/<int:num>/<string:color>')
def change(num, color):
    return render_template('level3.html', num=num, color=color)
    
if __name__=="__main__":
    app.run(debug=True)                   

