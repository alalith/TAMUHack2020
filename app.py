from flask import Flask, render_template, request, url_for, Markup
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html',)

if __name__ == '__main__':
    app.rum(debug=True)