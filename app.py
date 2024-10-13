
"""
Flask app to host API + simple interface for toggling api & lights running
"""

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

db = SQLAlchemy(app)

# T/F flag for whether to run API
class APIToggleFlag(db.Model):
	app_is_on = db.Column(db.Boolean, default=False, primary_key=True)

@app.route("/", methods=["GET"])
def home():
	"""
	Home page route
	"""
	return render_template("index.html")

@app.route("/off", methods=["GET"])
def turn_off():
	"""
	route to turn led system off and conserve api calls
	"""
	return render_template("leds_off.html")

@app.route('/on', methods=['GET'])
def turn_on():
	"""
	Route to turn led system on
	"""
	return render_template("leds_off.html")

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=5500)
