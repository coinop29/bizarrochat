import os
from flask import Flask, render_template, request, redirect, session
from googletrans import Translator

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "bizzaro_secret")

translator = Translator()
chat_history = []

languages = ['es', 'fr', 'de', 'zh-cn', 'ru', 'ar', 'en']

def bizzaro_translate(text):
    for lang in languages:
        text = translator.translate(text, dest=lang).text
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "username" not in session:
            session["username"] = request.form["username"]
        message = request.form["message"]
        translated = bizzaro_translate(message)
        chat_history.append((session["username"], translated))
        return redirect("/")
    return render_template("index.html", chat_history=chat_history, username=session.get("username"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
