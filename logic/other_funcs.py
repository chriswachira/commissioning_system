"""
	-	This module houses various functions or classes that assist in the refactoring of the 
		system's code
	- 	It helps in reducing code redudancy all across

"""

__author__ = "Chris Wachira"
__version__ = "0.1"
__maintainer__ = "chriskane816@gmail.com"
__status__ = "Prototype"

def get_prefix(sys_obj):
	#
	#	Returns a two character prefix depending on the system object(sys_obj) supplied as argument
	#
	prefix = None	# beginning characters for system objects
	
	if sys_obj == 'agent':
		prefix = "AG"
	elif sys_obj == 'customer':
		prefix = "CS"

	return prefix


def add_id_format(num):
	#
	#	Concatenates a provided number with zero(s) to match required global ID format
	#
	num = str(num)
	digits = None

	if len(num) == 1:
		digits = "00" + num
	elif len(num) == 2:
		digits = "0" + num
	elif len(num) == 3:
		digits == num

	return digits	#	The last 3 digits required to make a standard global ID e.g. AG-001

def join_prefix(prefix, obj_id):
	#
	#	Joins a system object's integer ID to the corresponding object's prefix
	#

	global_id = None
	digits = add_id_format(obj_id)	#	Returns standard Global ID format
	
	global_id = prefix + "-" + digits
	return global_id

