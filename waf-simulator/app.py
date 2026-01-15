from flask import Flask, render_template, request
from waf_engine import inspect_request
from logger import log_attack

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        user_input = request.form["input"]
        result = inspect_request(user_input)

        if result != "Safe Request":
            log_attack(user_input, result)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
