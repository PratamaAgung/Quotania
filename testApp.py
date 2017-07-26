'''
Author 		: Pratamamia Agung P
Date 		: 26 July 2017
Description	: Module for testing Quotania backend app
'''

from mainApp import app, Quote
import unittest
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from datetime import datetime
import json


#This is a class test for testing template (html and jinja)
class TestApp(unittest.TestCase):
	#setUp test
	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True

	#closing test
	def tearDown(self):
		pass

	#testing index.html
	def test_index(self):
		result = self.app.get('/')
		self.assertEqual(result.status_code, 200)

	def test_index_data(self):
		result = self.app.get('/')
		assert b'Quotania' in result.data


#This is a class test for testing database and its access method
class TestQuoteDB(unittest.TestCase):
	db = 0

	#setUp environment for all DB test
	@classmethod
	def setUpClass(cls):
		app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:12345@localhost/testdb'
		app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
		global db 
		db = SQLAlchemy(app)

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

		db.create_all()
		db.session.add(Quote("This is my quote", "Me"))
		db.session.add(Quote("A bright beautiful day", "Anonymous"))
		db.session.commit()

	#closing after all test complete
	@classmethod
	def tearDownClass(cls):
		pass

	#setUp each test
	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True

	#closing each test
	def tearDown(self):
		pass

	#test for submitting quotes
	def test_submit_quote(self):
		self.app.post('/submit_quote?author=Me&quote=This+is+my+quote')
		self.app.post('/submit_quote?author=Anonymous&quote=A+bright+beautiful+day')
		results = Quote.query.order_by(Quote.date).all()
		self.assertEqual(results[1].author, 'Anonymous')
		self.assertEqual(results[1].quote, 'A bright beautiful day')

	#test for get next quote
	def test_get_next_quote(self):
		first_quote = Quote.query.order_by(Quote.nbLike.desc()).first()
		result = self.app.post('get_next_quote?id=' + str(first_quote.id))
		assert b'"author": "Anonymous"' in result.data
		assert b'"quote": "A bright beautiful day"' in result.data

	#test for get before quote
	def test_get_before_quote(self):
		second_quote = Quote.query.order_by(Quote.nbLike.desc()).all()[1]
		result = self.app.post('get_before_quote?id=' + str(second_quote.id))
		assert b'"author": "Me"' in result.data
		assert b'"quote": "This is my quote"' in result.data

	#test for like quote
	def test_like_quote(self):
		like_quote = Quote.query.order_by(Quote.nbLike.desc()).first()
		nbLike = like_quote.nbLike
		liked_id = like_quote.id
		self.app.post('/like_quote?id=' + str(like_quote.id))
		modified = Quote.query.filter_by(id = liked_id).first()
		self.assertEqual(modified.nbLike, nbLike+1)


#command to execute all test
if __name__ == '__main__':
	unittest.main()