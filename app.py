from cs50 import SQL
from flask import Flask, render_template,request

app  = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",sports = SPORTS)

SPORTS = ["Basketball","Soccer","Ultimate"]


# "REGISTRANTS  = {}"  gemmer registrants i memory

#Når vi får en Post request bliver vi sendt til denne side. 
@app.route("/register", methods = ["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message = "missing name")
    
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message = "missing sport ")
    
    if sport not in SPORTS:
        return render_template("error.html", message = "Invalid sport")
    
    # REGISTRANTS[name] = sport
    db.execute("INSERT INTO registrants (name,sport) VALUES(?,?)",name,sport )
    return render_template("succes.html")

@app.route("/registrants")
def registrants():
    registrants = db.execute("SELECT name, sport, FROM registrants ")
    return render_template("registrants.html", registrants = registrants)


import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("froshims.db")

# Create a cursor
cur = conn.cursor()

# Create the table
cur.execute("""
CREATE TABLE registrants (
    id INTEGER,
    name TEXT NOT NULL,
    sport TEXT NOT NULL,
    PRIMARY KEY(id)
);
""")

# Commit changes and close connection
conn.commit()
conn.close()







if __name__ == "__main__":
    app.run(debug = True)