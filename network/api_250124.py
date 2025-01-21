# 1. Erstelle eine Flask-App mit mindestens drei GET-Endpunkten.
# 2. Die GET-Anfragen sollen unterschiedliche Funktionen ausführen:

from flask import Flask, request

app = Flask(__name__)

# ○ Route 1: /brand/<id>?type=<type>&condition=<condition>
# ■ Beispiel: http://localhost:6060/brand/10?type=clothes&condition=new


@app.route("/brand/<id>", methods=["GET"])
def get_brand_id(id):

    # Validation if 'id' is a number - this was with chatgpt Hilfe
    if not id.isdigit():
        return "ID must be a number"

    brand_type = request.args.get("type")
    brand_condition = request.args.get("condition")
    return f"Brand-ID: {id}, Type: {brand_type}, Condition: {brand_condition}"

    # ■ Ausgabe: "Brand-ID: 10, Type: clothes, Condition: new"


# ○ Route 2: /product/<product_id>
# ■ Beispiel: http://localhost:6060/product/123


@app.route("/product/<product_id>", methods=["GET"])
def get_product_id(product_id):
    return f"Product-ID: {product_id}"


# ■ Ausgabe: "Product-ID: 123"


# ○ Route 3: /search
# ■ Beispiel: http://localhost:6060/search?query=shoes


@app.route("/search", methods=["GET"])
def get_search():
    search_id = request.args.get("query")
    return f"Searching for: {search_id}"

    #  URL input --->   http://localhost:6060/search?search=shoes


# ■ Ausgabe: "Searching for: shoes"


# 3. Bonus: Implementiere eine Validierung der Parameter (z. B. id muss eine Zahl sein).
# 4. Teste die Routen mit Postman oder deinem Browser.

if __name__ == "__main__":
    app.run(debug=True, port=6060)
