"""
	- Globalizer module as part of the Commissioning system's logic.

	- This module is supposed to provide a global identification to the objects
	  of this system(Agents or Customers).

	- It gets a new ID from the Indexer module and uses it to create a new global ID for
	  a new object being added into the system.
	
	- Agents' global ID begin with a 'AG-' prefix while Customers' global ID begins with 
	  a 'CS-' prefix. Example, first Agent in Database will get a global ID 'AG-001'.

"""

__author__ = "Chris Wachira"
__version__ = "0.1"
__maintainer__ = "chriskane816@gmail.com"
__status__ = "Prototype"

from logic.indexer import Indexer

class Globalizer():
	def __init__(self, sys_obj, filename, tablename):
		Index = Indexer(filename, tablename)	# intialize Indexer 
		new_index = Index.get_new()		# get new id from Indexer module
		prefix = ""

		if sys_obj == 'agent':
			prefix = "AG-"
		elif sys_obj == 'customer':
			prefix = "CS-"

		_id = str(new_index)
		if len(str(new_index)) == 1:
			new_id = "00" + _id
		elif len(str(new_index)) == 2:
			new_id = "0" + _id
		elif len(str(new_index)) == 3:
			new_id = _id

		self.global_id = prefix + new_id

	def get_globalID(self):
		return self.global_id

