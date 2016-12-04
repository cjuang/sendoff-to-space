from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
import lxml
from lxml import html
import requests

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///messages.db")

# delete messages older than 30 days on the server
# if db.execute("SELECT * FROM messages") != None & db.execute("DELETE FROM messages WHERE msg_date < GetDate() - 30") != None:
#     db.execute("DELETE FROM messages WHERE Date < GetDate(Date) - 30")

@app.route("/")
def index():
    # scrape HTML from SpaceflightNow website
    page = requests.get('http://spaceflightnow.com/launch-schedule/')
    tree = html.fromstring(page.content)
    
    # find the time and location of launch
    scrape_timeloc = tree.xpath('//div[@class="missiondata"]/text()')
    # find date of launch
    scrape_date = tree.xpath('//span[@class="launchdate"]/text()')
    # find name of mission
    scrape_name = tree.xpath('//span[@class="mission"]/text()')
    
    # pick earliest launch, date, time, and location
    launch_date = scrape_date[0]
    launch_time = scrape_timeloc[0]
    launch_loc = scrape_timeloc[1]
    launch_name = satname(scrape_name[0])
    
    # load all current messages
    messages_history = db.execute("SELECT msg_from, msg_to, msg_msg, msg_date FROM messages ORDER BY id DESC")
    
    # return launch info, messages
    return render_template("main.html", lname = launch_name, ldate = launch_date, 
           lloc = launch_loc, ltime = launch_time, messages = messages_history)
    
@app.route("/write", methods=["GET", "POST"])
def write():
    """Write a nice message to the departing spacecraft"""
    if request.method == "GET":
        return render_template("write.html")
        
    if request.method == "POST":
        
        # make variable for stock name
        sender = request.form.get("inputfrom")
        mission = request.form.get("inputto")
        message = request.form.get("inputmsg")
        
        # check to make sure there is something in at least one of the forms
        # if sender is None & mission is None & message is None:
        #    flash('Error: Form was blank, returning to message page')
        #    return redirect(url_for("write.html"))
        
        # append new user to user list
        db.execute("INSERT INTO messages (msg_from, msg_to, msg_msg) VALUES (:sender, :to, :msg)", 
                    sender=sender, to=mission, msg=message)
        
        # success
        flash('Successfully received your message!')
        return redirect(url_for('index'))

# @app.route("/articles")
# def articles(launch_name):
#     """Look up articles for a launch."""
#     # take the launch_name as input, convert to bytes
#     satinput = str.encode(launch_name)
    
#     # initialize array to store articles
#     lookupresult = []
    
#     # call lookup function to find relevant news articles
#     lookupresult = lookup(satinput)
    
#     # return the newsfeed
#     return jsonify(lookupresult)