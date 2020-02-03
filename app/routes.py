from flask import render_template, flash, redirect, request, url_for
from werkzeug import secure_filename
from app import app

play = 1

#main page plus random key handles transfers
@app.route("/index")
@app.route('/')
def index():
    global play
    return render_template("video.html", play=str(play))

@app.route("/increment/<amount>")
def increment(amount):
    global play
    play += int(amount)
    if play == 0:
        play = 1
    return redirect(url_for("index"))
