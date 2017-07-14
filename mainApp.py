from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def main_page():
    return render_template('index.html')

@app.route('/submit_quote', methods = ['POST'])
def submit_quote():
	return jsonify(status = True);

if __name__=="__main__":
    app.jinja_env.cache = {}
    app.run(host='0.0.0.0', port=2000)