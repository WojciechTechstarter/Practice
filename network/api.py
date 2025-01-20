from flask import Flask, request

app = Flask(__name__)


# Begrüßungsroute
@app.route("/")
def home():
    return "Willkommen bei meiner Flask-App!"


# Info-Route
@app.route("/info")
def info():
    return "Dies ist eine einfache API mit Flask."


# Team-Route
@app.route("/team")
def team():
    return "Unser Team besteht aus IT-Experten und Entwicklern."


# Hilfe-Route
@app.route("/hilfe")
def hilfe():
    return "Hier findest du Unterstützung zu unserer API."


# Kontakt-Route
@app.route("/kontakt")
def kontakt():
    return "Schreibe uns eine E-Mail an kontakt@example.com."


# 1. About-Route
@app.route("/about")
def about():
    return "Mein Name ist Wojciech Olakowski, und ich interessiere mich für Webentwicklung."


# 2. projekt-Route
@app.route("/projekt")
def projekt():
    return "Mein aktuelles Projekt ist eine Flask-API für Anfänger."


# 3. news-Route
@app.route("/news")
def news():
    return "Heute lernen wir, wie man APIs mit Flask erstellt!"


# 4. feedback-Route
@app.route("/feedback")
def feeedback():
    return "Wir freuen uns über dein Feedback unter feedback@example.com."


# 5. support-Route
@app.route("/support")
def support():
    return "Besuche unsere Support-Seite unter support.example.com."


# language-Route
@app.route("/support")
def language():
    return "To change the language please visit the website example.com and click on the flag icon in the top right corner."


# Extra tast


# @app.route("/greet")
# def greet():
#     greeting = request.args.get("greet")
#     return "Hallo, willkomen auf meiner Flask-API!".format(greeting)


if __name__ == "__main__":
    app.run(port=6060)
