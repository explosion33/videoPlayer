from flask import render_template, flash, redirect, request, url_for
from werkzeug import secure_filename
from app import app
import os

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

    vids = os.listdir(os.getcwd() + "/app/static/videos")


    play += int(amount)
    if play == 0:
        play = 1

    nums = []
    for vid in vids:
        vid = vid[::-1]
        vid = vid[4::]
        num = ""
        for i in vid:
            if i != "_":
                num += i
            else:
                break
        num = num[::-1]
        nums.append(int(num))

    if play not in nums:
        play -= int(amount)
    
    return redirect(url_for("index"))
