'''
Author 		: Pratamamia Agung P
Description	: Module for running backend server
'''

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
app = Flask(__name__)

#database connection configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:12345@localhost/quotania'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#model for quote
class Quote(db.Model):
    __tablename__ = "quotes"
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(200))
    author = db.Column(db.String(35))
    nbLike = db.Column(db.Integer, default = 0)
    date = db.Column(db.DateTime, default= datetime.today())
    
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author

#execute when running for the first time
db.create_all()

#routing for main page
@app.route('/')
@app.route('/index.html')
def main_page():
	return render_template('index.html')

#routing for submit quote
@app.route('/submit_quote', methods = ['GET', 'POST'])
def submit_quote():
	try:
		my_quote = Quote(request.args.get('quote', '', type = str), 
			request.args.get('author', '', type = str))
		db.session.add(my_quote)
		db.session.commit()
		return jsonify(status = True)
	except:
		return jsonify(status = False)


#ruoting for getting quote
@app.route('/get_initial_quote', methods= ['GET', 'POST'])
def get_initial_quote():
	quotes = Quote.query.order_by(Quote.nbLike.desc()).all()
	if(len(quotes) > 0):
		best_quote = quotes[0]
		if(len(quotes) > 1):
			next = True
		else:
			next = False
		return jsonify(quote = best_quote.quote, author = best_quote.author,
			nbLike = best_quote.nbLike, id = best_quote.id, before = False, next = next)
	else:
		return jsonify({})

#routing for get next quote
@app.route('/get_next_quote', methods = ['POST'])
def get_next_quote():
	quotes = Quote.query.order_by(Quote.nbLike.desc()).all()
	idx = 0
	curr_id = request.args.get('id', '', type = int)
	for quote in quotes:
		if (quote.id == curr_id):
			break
		else:
			idx += 1
	if (idx+1 < len(quotes)):
		next_quote = quotes[idx+1]
		if (idx + 2 < len(quotes)):
			next = True
		else:
			next = False

		return jsonify(quote = next_quote.quote, author = next_quote.author,
			nbLike = next_quote.nbLike, id = next_quote.id, next = next, before = True)
	else:
		return jsonify({})

#roting for get preceding qoute
@app.route('/get_before_quote', methods = ['POST'])
def get_before_quote():
	quotes = Quote.query.order_by(Quote.nbLike.desc()).all()
	idx = 0
	curr_id = request.args.get('id', '', type = int)
	for quote in quotes:
		if (quote.id == curr_id):
			break
		else:
			idx += 1
	if (idx-1 >= 0):
		before_quote = quotes[idx-1]
		if (idx - 2 >=0):
			before = True
		else:
			before = False
		return jsonify(quote = before_quote.quote, author = before_quote.author,
			nbLike = before_quote.nbLike, id = before_quote.id, next = True, before = before)
	else:
		return jsonify({})

#routing for like a quote
@app.route('/like_quote', methods = ['POST'])
def like_quote():
	try:
		liked = Quote.query.filter_by(id = request.args.get('id', '', type=int)).first()
		liked.nbLike += 1
		db.session.add(liked)
		db.session.commit()
		return jsonify(status = True)
	except:
		return jsonify(status = False)

@app.route('/refresh_navigator', methods = ['POST'])
def refresh_navigator():
	quotes = Quote.query.order_by(Quote.nbLike.desc()).all()
	idx = 0
	curr_id = request.args.get('id', '', type = int)
	for quote in quotes:
		if (quote.id == curr_id):
			break
		else:
			idx += 1
	if (idx-1 >= 0):
		before = True
	else:
		before = False
	if (idx + 1 < len(quotes)):
		next = True
	else:
		next = False
	return jsonify(nbLike = quotes[idx].nbLike, next = next, before = before)

#command to run backend application
if __name__=="__main__":
    app.jinja_env.cache = {}
    app.run(host='0.0.0.0', port=2000)