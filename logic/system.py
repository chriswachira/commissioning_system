"""
	- system module as part of the Commissioning system's logic.

	- This module is supposed to provide OS-based functionality to
	  the Commissioning system

"""
__author__ = "Chris Wachira"
__version__ = "0.1"
__maintainer__ = "chriskane816@gmail.com"
__status__ = "Prototype"

import os

class System():
	def __init__(self):
		self.current_os = os.name	# get current OS' type/name
		current_user = os.getlogin()	# get current logged-in user's name
		self.home_dir = ""		# initialize home directory variable

		if self.current_os == 'nt':
			self.home_dir = "C:\\Users\\{0}\\Documents\\BitBox".format(current_user)
		elif self.current_os == 'posix':
			self.home_dir = "/home/{0}/Documents/BitBox".format(current_user)

		if not os.path.exists(self.home_dir):
			os.mkdir(self.home_dir)
			print("Folder successfully created at {0}".format(self.home_dir))

	def make_dir(self, dir_name):
		import os

		try:
			if self.current_os == 'nt':
				os.mkdir(self.home_dir + "\{0}".format(dir_name))
			else:
				os.mkdir(self.home_dir + "/{0}".format(dir_name))

		except FileExistsError:
			print("Folder already exists!")
				 
