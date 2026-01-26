from flask import Flask,jsonify,request

app=Flask(__name__)
items=[
    {"id":1,"name":"Item 1","description":"This is item 1 "},
    {"id":2,"name":"Item 2","description":"This is item 2 "}
]
@app.route('/home')

def home():
    return "welcome to home of application "

##get: return all the items from the form 

@app.route('/items',methods=['GET'])

def get_items():
    return jsonify(items)

##get : retrive a specific item by ID 
@app.route('/items/<int:item_id>',methods=['GET'])

def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"itemm is not found "})
    return jsonify(item)

##POST:create a new task 
@app.route('/items'.methods['POST'])

def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"itemm is not found "})
    new_item={
        "id":items[-1]['id']+1 if items else 1
        "name":request.json['name'],
        "description":request.json["description"]
    }
items.append(new_item)
return jsonify(new_item)

## Put  update an existing item 
@app.route('/item/<int:item_id',methods=['PUT'])

def update_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"Item not found "})


if __name__=='__main__':
    app.run(debug=True)