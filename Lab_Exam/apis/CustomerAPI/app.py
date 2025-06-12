from flask import Flask, jsonify, request
app = Flask(__name__)

customers = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = next((c for c in customers if c['id'] == id), None)
    return jsonify(customer or {})

@app.route('/customers', methods=['POST'])
def add_customer():
    new_customer = request.json
    customers.append(new_customer)
    return jsonify(new_customer), 201

if __name__ == '__main__':
    app.run(port=5000)
