// apis/ProductAPI/app.py
from flask import Flask, jsonify, request
app = Flask(__name__)

products = [
    {"id": 1, "name": "Smartphone", "price": 699},
    {"id": 2, "name": "Laptop", "price": 1299}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((p for p in products if p['id'] == id), None)
    return jsonify(product or {})

@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(port=5002)