from flask import Flask, render_template, request, redirect, session
from cs50 import SQL
import random
import datetime

app = Flask(__name__)
app.secret_key = "290708"

#connect SQL
db = SQL("sqlite:///slanglinker.db")

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/slang")
def slang_list():
    q = request.args.get("q")
    if q:
        slangs = db.execute("SELECT * FROM slang WHERE phrase LIKE ?", f"%{q}%")
    else:
        slangs = db.execute("SELECT * FROM slang")
    return render_template("slang.html", slangs=slangs, query=q)

@app.route('/slang/<int:id>')
def slang_details(id):
    slang = db.execute("SELECT * FROM slang WHERE id = :id", id=id)

    #execution
    if slang:
        return render_template("explain.html", slang = slang[0])
    else:
        return "Slang not found", 404

@app.route("/explain")
def explain():
    word = request.args.get("word")
    if not word:
        return redirect("/")  # return to home

    word = word.strip().lower()

    result = db.execute("SELECT * FROM slang WHERE LOWER(TRIM(phrase)) LIKE ?", f"%{word}%")

    if result:
        return render_template("explain.html", slang=result[0])
    else:
        return render_template("explain.html", slang=None, word=word)

@app.route("/word")
def word():
    slangs = db.execute("SELECT * FROM slang")
    if not slangs:
        return render_template("word.html", slang=None)

    today = datetime.date.today().toordinal()
    index = today % len(slangs)

    if 0 <= index < len(slangs):
        slang = slangs[index]
    else:
        slang = random.choice(slangs)

    return render_template("word.html", slang=slang)

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        phrase = request.form.get("phrase")
        meaning = request.form.get("meaning")
        example = request.form.get("example")
        context = request.form.get("context")

        if not phrase or not meaning:
            return render_template("submit.html", error="Please fill out all required fields.")

        db.execute("INSERT INTO submissions (phrase, meaning, example, context) VALUES (?, ?, ?, ?)",
                   phrase.strip(), meaning.strip(),
                   example.strip() if example else None,
                   context.strip() if context else None)  #inserting data from submissions

        return render_template("submit.html", success="Thanks! Your slang has been submitted for review. You will see it in a matter of time on our page 😎")
    return render_template("submit.html")



#admin side
@app.route("/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        code = request.form.get("code")
        if code == "290708":
            session["admin"] = True
            return redirect("/review")
        else:
            return render_template("admin.html", error="Incorrect admin code.")
    return render_template("admin.html")
@app.route("/review", methods=["GET", "POST"])
def review():
    if not session.get("admin"):
        return redirect("/admin")

    if request.method == "POST":
        slang_id = request.form.get("id")
        action = request.form.get("action")

        if action == "admit":
            submission = db.execute("SELECT * FROM submissions WHERE id = ?", slang_id)
            if submission:
                slang = submission[0]
                db.execute("INSERT INTO slang (phrase, meaning, example, context) VALUES (?, ?, ?, ?)",
                           slang["phrase"], slang["meaning"], slang["example"], slang["context"])
                db.execute("DELETE FROM submissions WHERE id = ?", slang_id)
        elif action == "reject":
            db.execute("DELETE FROM submissions WHERE id = ?", slang_id)

        return redirect("/review")

    submissions = db.execute("SELECT * FROM submissions")
    return render_template("review.html", submissions=submissions)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

#error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404





