from flask import Flask, request, render_template, redirect, url_for
from database import user_table

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")

    found_User = user_table.find_one({
        "username": username,
        "password": password
    })

    if found_User:
        return redirect(url_for('home'))
    else:
        return render_template("login.html")
    
  return render_template("login.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        username = request.form.get("username")
        role = request.form.get("role")
        password = request.form.get("password")

        user_table.insert_one({
           "username": username,
           "role": role,
           "password": password
        })
        return redirect(url_for('login'))

    return render_template("register.html")

@app.route("/home")
def home():
  return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)

    

