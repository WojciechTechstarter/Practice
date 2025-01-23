from flask import Flask, request, jsonify

app = Flask(__name__)

# In-Memory "Datenbank"
products = []


# POST - Ein neues Produkt hinzufügen
@app.route("/products", methods=["POST"])
def create_product():
    new_product = request.get_json()

    # Checking if the input data include necessarry fields
    if not new_product or "name" not in new_product or "price" not in new_product:
        return jsonify({"error": "Invalid input"}), 400

    try:
        price = float(new_product["price"])

    except ValueError:
        return jsonify({"error": "Price must be a valid number"}), 400

    if price < 0:
        return jsonify({"error": "Price cannot be a negative number"}), 400

    # Here is key (id)   and here is it's value 1, 2, 3 ....
    new_product["id"] = max([p["id"] for p in products], default=0) + 1
    products.append(new_product)
    return jsonify(new_product), 201


# GET - Alle Produkte abrufen
@app.route("/products", methods=["GET"])
def get_products():

    name_filter = request.args.get("name")
    if name_filter:
        filtered_products = [
            p for p in products if name_filter.lower() in p["name"].lower()
        ]
        return jsonify(filtered_products), 200
    return jsonify(products), 200


# # GET - Alle Produkte abrufen
# @app.route("/products/<id>", methods=["GET"])
# def get_products_id(id):
#     product_id = int(id)
#     return jsonify({"The product with id = {product_id} is {products[id]}"})


if __name__ == "__main__":
    app.run(debug=True)
