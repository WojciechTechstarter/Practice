from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Welcome Mamazon"


@app.route("/item/<product_id>", methods=["GET"])
def get_item(product_id):
    color = request.args.get("color")  # /item/2?color=black
    size = request.args.get("size")  # /item/2?size=M
    # /item/2?color=black&size=M
    return f"Welcome Mamazon's item {product_id} with the color {color} an with the size {size}"


@app.route("/brand", methods=["GET"])
def get_h_and_m_default_brand_page():
    # Should return a welcome to brand page text
    return "Welcome to H&M store!!!!!!"


@app.route("/brand/<brand_id>", methods=["GET"])
def get_brand_by_id(brand_id):
    # Should return  welcome to specific brand page text
    # E.g. Welcome to Hilfigher (dynamisch)
    # Should be able to filter by brand type and should display the filter on the screen
    # E.g. Welcome to Hilfigher and the type is t-shirts
    brand_type = request.args.get("type")
    # Should be able to filter by condition of the article and should display the condition on the screen
    # --> Goals E.g. Welcome to Hilfigher and the type is t-shirts and the condition is used
    condition_type = request.args.get("condition")

    return f"Welcome to {brand_id}, where you can browse through many different kinds of {condition_type} {brand_type}!"


@app.route("/user/<user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user_name = request.args.get("name")
    user_age = request.args.get("age")
    user_gender = request.args.get("gender")
    user_height = request.args.get("height")
    return f"{user_name} is {user_age} years old {user_gender} with the height of {user_height}."


if __name__ == "__main__":
    app.run(debug=True, port=6060)
