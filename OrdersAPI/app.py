from flask import Flask, jsonify, request
app = Flask(__name__)

orders = [
    {"id": 1, "customer_id": 1, "product_id": 2, "quantity": 1},
    {"id": 2, "customer_id": 2, "product_id": 1, "quantity": 2}
]

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = next((o for o in orders if o['id'] == id), None)
    return jsonify(order or {})

@app.route('/orders', methods=['POST'])
def add_order():
    new_order = request.json
    orders.append(new_order)
    return jsonify(new_order), 201

if __name__ == '__main__':
    app.run(port=5001)