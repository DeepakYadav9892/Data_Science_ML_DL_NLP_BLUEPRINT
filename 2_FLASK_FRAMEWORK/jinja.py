from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Flask course</h1>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello {name}!"
    return render_template("form.html")

# Simple result page
@app.route("/success/<int:score>")
def success(score):
    res = "PASS" if score >= 50 else "FAIL"
    return render_template("result.html", result=res, score=score)

# Dictionary-based result (Jinja loop demo)
@app.route("/successres/<int:score>")
def success_res(score):
    res = "PASS" if score >= 50 else "FAIL"
    exp = {"score": score, "result": res}
    return render_template("result1.html", results=exp)

if __name__ == "__main__":
    app.run(debug=True)
