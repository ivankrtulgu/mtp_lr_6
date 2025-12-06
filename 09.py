from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    users = ["Иван", "Мария", "Пётр"]
    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)