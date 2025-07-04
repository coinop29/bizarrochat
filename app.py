import os
from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

languages = ['es', 'fr', 'de', 'zh-cn', 'ru', 'ar', 'en']

def bizzaro_translate(text):
    for lang in languages:
        text = translator.translate(text, dest=lang).text
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    translated = ""
    if request.method == "POST":
        message = request.form["message"]
        translated = bizzaro_translate(message)
    return render_template("index.html", translated=translated)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
