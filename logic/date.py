"""
	- Date module as part of the Commissioning system.

	- This module will provide basic date and time functionality to the Commissioning system.

"""

__author__ = "Chris Wachira"
__version__ = "0.1"
__maintainer__ = "chriskane816@gmail.com"
__status__ = "Prototype"

import datetime

class Date():
	def __init__(self):
		self.now = datetime.datetime.now()

	def get_day(self):
		day = self.now.day
		return day

	def get_month(self):
		month = self.now.month
		return month

	def get_year(self):	
		year = self.now.year
		return year

class DateFormatter():
	def __init__(self, *args):
		self.args = args

	def add_format(self, separator):
		sep = separator		# a single character either a hyphen(-) or forward slash(/)

		current_date = str(self.args[0]) + sep + str(self.args[1]) + sep + str(self.args[2])
		return current_date	# the current system date
