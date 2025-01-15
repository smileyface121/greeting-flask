
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key= "lundpeychaar"

@app.route("/")
def index():
    flash("whats your name?")
    return render_template('index.html')

@app.route("/greet", methods=["POST", "GET"])
def gree():
    request.form['name_input']
    flash("Hi   " +str(request.form['name_input']) +", Great to see you!")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

    