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
@app.route('/get_quote_after', methods = ['GET', 'POST'])
def get_quote_after():
	quotes = Quote.query.order_by(Quote.nbLike.desc()).all()
	print(list(quotes))
	return jsonify(status = True)

if __name__=="__main__":
    app.jinja_env.cache = {}
    app.run(host='0.0.0.0', port=2000)