from flask import Flask, request, render_template
from api import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)