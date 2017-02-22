"""
	- Customer module as part of the Commissioning System's logic

	- This module gathers attributes of customers that will be used to enter a new 
	  customer into the customer's database.

"""

__author__ = "Chris Wachira"
__maintainer__ = "chriskane816@gmail.com"
__version__ = "0.1"
__status__ = "Prototype"

from globalizer import Globalizer
from database import Database

class Customer():
	def __init__(self):
		self.db = Database("customers")		# initialize customer's database connection

	def attribs(self, **kwargs):
		gl = Globalizer("customer", "customers", "CUSTOMERS")
		self.id = gl.get_globalID()
		self.name = kwargs.get('name')
		self.address = kwargs.get('address')
		self.cell = kwargs.get('cell')
		self.email = kwargs.get('email')
		self.intro = kwargs.get('intro')
		self.memo = kwargs.get('memo')

	def insert_attribs(self):
		self.db.sql_do("""INSERT INTO CUSTOMERS VALUES
		(?,?,?,?,?,?,?)""", self.id, self.name, self.address, self.cell, self.email, self.intro, self.memo)
		self.db.close()
