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

@app.route('/add', methods=['POST'])
def add():
    description = request.form['description']
    todoList.append({'id' : len(todoList) + 1, 'description' : description, 'status' : 'Done'})
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    for todo in todoList:
        if todo['id'] == id:
            todoList.remove(todo)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)