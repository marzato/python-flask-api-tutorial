from flask import Flask,jsonify,request,json

app = Flask(__name__)

todos=[{ "label": "My first task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos) 


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object=json.loads(request_body)
    if isinstance(decoded_object,list):
        for task in decoded_object:
            todos.append(task)
    elif isinstance(decoded_object,dict):
        todos.append(decoded_object)
    else:
        return "input mal", 400
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
