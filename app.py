from flask import Flask, render_template, request, redirect, url_for

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
    global todoList
    description = request.form['description']
    if description:
        new_id = max([item['id'] for item in todoList]) + 1 if todoList else 1
        todoList.append({'id': new_id, 'description': description, 'status': 'Doing'})
    return redirect(url_for('index'))


@app.route('/update/<int:item_id>', methods=['POST'])
def update(item_id):
    global todoList
    for item in todoList:
        if item['id'] == item_id:
            item['status'] = 'Done' if item['status'] == 'Doing' else 'Doing'
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete(item_id):
    global todoList
    todoList = [item for item in todoList if item['id'] != item_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)