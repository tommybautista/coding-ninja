from flask import Flask, render_template 
app = Flask(__name__)                     
    
@app.route('/')                           
def index():
    return render_template('index.html') 

@app.route('/names')                           
def names():

    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'},
        {'first_name' : 'Har', 'last_name' : 'Old'},
        {'first_name' : 'Tom', 'last_name' : 'My'},
        {'first_name' : 'Jenni', 'last_name' : 'Fer'},
        {'first_name' : 'Jack', 'last_name' : 'Son'},
        {'first_name' : 'John', 'last_name' : 'Son'},
        {'first_name' : 'Jor', 'last_name' : 'Dan'},
        {'first_name' : 'James', 'last_name' : 'Son'},
        {'first_name' : 'Apo', 'last_name' : 'Lo'},
        {'first_name' : 'Kangar', 'last_name' : 'Roo'},
        {'first_name' : 'Tomin', 'last_name' : 'Jerri'},
        {'first_name' : 'Li', 'last_name' : 'Yon'},
        {'first_name' : 'Li', 'last_name' : 'Ger'}
    ]

    return render_template("index.html", user = users)


if __name__=="__main__":
    app.run(debug=True)  