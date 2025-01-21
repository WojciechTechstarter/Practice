from flask import Flask, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]

# 1. Erstelle eine Flask-App mit den folgenden Routen:
# ○ Route 1: /user/<id>
# Beispiel: http://localhost:6060/user/1


@app.route("/user/<id>", methods=["GET"])
def get_user_id(id):
    for user in users:
        if user["id"] == int(id):  # matching the id
            return user  # returning id from the list

    return "ID must be a number between 1 and 3"

    user_name = request.args.get("name")
    user_email = request.args.get("email")
    return f"Nutzerdetails wie"


# Rückgabe: Nutzerdetails wie {"id": 1, "name": "Alice", "email":
# "alice@example.com"}


if __name__ == "__main__":
    app.run(debug=True, port=6060)
