from flask import Flask, redirect, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    conn = get_db()
    reviews = conn.execute("SELECT * FROM reviews").fetchall()
    conn.close()
    return render_template("page01.html", reviews=reviews)


@app.route("/add_review", methods=["POST"])
def add_review():
    data = request.form

    name = data["name"]
    place = data["place"]
    review = data["review"]

    conn = get_db()
    conn.execute(
        "INSERT INTO reviews (name, place, review) VALUES (?, ?, ?)",
        (name, place, review),
    )
    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/get_reviews")
def get_reviews():
    conn = get_db()
    reviews = conn.execute("SELECT * FROM reviews").fetchall()
    conn.close()

    return jsonify([dict(row) for row in reviews])

@app.route("/tabarka")
def tabarka():
    return render_template("tabarka.html")

@app.route("/aindraham")
def aindraham():
    return render_template("ain-drahem.html")
@app.route("/ainsoltane")
def ainsoltane():
    return render_template("ain-soltan.html")
@app.route("/bni-mtir")
def bni_mtir():
    return render_template("bni-mtir.html")
@app.route("/bulla-regia")
def bulla_regia():
    return render_template("bulla-regia.html")

if __name__ == "__main__":
    app.run(debug=True)