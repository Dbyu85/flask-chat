import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomnumber123"
messages = []

def add_messages(username, message):
	""" Add messages to the 'messages' list """
	#in line 11 is a method to for getting time from python.
	now = datetime.now().strftime("%H:%M:%S")
	messages.append("({}) {}: {}".format(now, username, message))
	
	
def get_all_messages():
	""" get all of the messages and separate them witha 'br' """
	return "<br>".join(messages)

@app.route('/', methods =["GET", "POST"])
def index():
	"""Main page with instructions """
	if request.method == "POST":
		session["username"] = request.form["username"]
		
	if "username" in session:
		return redirect(session["username"])
	
	return render_template("index.html")


@app.route('/<username>')
def user(username):
	""" Display chat message """
	return "<h1>Welcome, {0}</h1> {1}".format(username, get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
	""" Creating a new message and redirect back to the chat page """
	add_messages(username, message)
	return redirect("/" + username)



app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)