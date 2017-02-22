"""
	- Database module as part of the Commissioning system's logic.
	
	- This module is supposed to provide Database functionality to the
	  Commissioning system, specifically, the SQLite3 database functionality.

"""

__author__ = "Chris Wachira"
__version__ = "0.1"
__maintainer__ = "chriskane816@gmail.com"
__status__ = "Prototype"

import sys
sys.path.append("/home/chriswachira/Desktop/commissioner")
import sqlite3
from logic.system import System

class Database():
	def __init__(self, filename):
		Sys = System()
		if Sys.current_os == 'nt':
			fn = Sys.home_dir + "\\" + filename + ".db"
		else:
			fn = Sys.home_dir + "/" + filename + ".db"

		self._db = sqlite3.connect(fn)
		self.c = self._db.cursor()
		print("Successfully connected to database - {0}".format(fn))

	def sql_do(self, sql, *params):
		cursor = self.c.execute(sql, params)
		return cursor
		self._db.commit()

	def close(self):
		self._db.commit()
		self._db.close()
		
