from flask import Flask, request
from users_list import users

app = Flask(__name__)


# getting user by id
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    final_user = None

    for u in users:
        if u["id"] == user_id:
            final_user = u
            break

    if final_user == None:
        return "User could not be found "

    return f"The User is {final_user}"


# Route 3: /search?name=<name>
# Beispiel: http://localhost:6060/search?name=Charlie
# Rückgabe: "Found user: Charlie" oder "No user found with name: Charlie"
@app.route("/search", methods=["GET"])
def get_user_by_name():
    final_user = None
    name = request.args.get("name")
    for u in users:
        if u["firstName"] == name:
            final_user = u

    if final_user == None:
        return "User could not be found "

    return f"The User is {final_user}"


# 1. Postman installieren
# 2. url eingeben, POST Befehl aushwählen --> siehe Screenshot
# 3. Ausführen und veschiedene Parameter im  body angeben
# 4. Zusatz: Versuchen den richtigen Benutzer zu bekommen
# 5. Zusatz Zusatz: Versucht eine weitere post anfrage mit signup zu erstellen,
# welche Route einen neuen Nutzer in die Liste einfügt
@app.route("/users/login", methods=["POST"])
def login():
    credentials = request.get_json()
    username = credentials["username"]
    password = credentials["password"]
    email = credentials["email"]
    # Now you can access the user based on email and password and return if valid credentials
    return f"Hallo {credentials} {username} {password} {email}"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
