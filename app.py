from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

todoList = [ 
    {'id' : 1, 'description' : 'SS1 Assignment 1', 'status' : 'Done'}, 
    {'id' : 2, 'description' : 'SS1 Assignment 2', 'status' : 'Doing'}, 
    {'id' : 3, 'description' : 'SS1 Final', 'status' : 'Doing'} 
] 

@app.route('/')
def index():
    return render_template('index.html', todoList=todoList)

if __name__ == '__main__':
    app.run(debug=True)