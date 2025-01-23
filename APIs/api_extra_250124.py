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


# @app.route("/user/<int:user_id>", methods=["GET"])
# def get_user_id(user_id):
#     final_user = None

#     for u in users:
#         if u["id"] == user_id:
#             final_user = u

#     if final_user == None:
#         return "There is no such user"

#     return f"The user is {final_user}"


# Rückgabe: Nutzerdetails wie {"id": 1, "name": "Alice", "email":
# "alice@example.com"}


# Route 3: /search?name=<name>
# Beispiel: http://localhost:6060/search?name=Charlie
# Rückgabe: "Found user: Charlie" oder "No user found with name: Charlie"


@app.route("/search", methods=["GET"])
def get_user_by_name():
    final_user = None
    name = request.args.get("name")

    for u in users:
        u["name"] = name
        final_login = u

    if final_login == None:
        return "The username doesn`t exist"

    return f"User {final_user} has successfully logged in!"


# Rückgabe: "User Bob successfully logged in!" (oder Fehler, falls ID nicht
# existiert)


if __name__ == "__main__":
    app.run(debug=True, port=6060)
