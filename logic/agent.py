"""
	- Agent module as part of the Commissioning system's logic

	- This module gathers attributes of an agent that will be used to create a new agent 
	  into the Agents' Database.

"""

__author__ = "Chris Wachira"
__maintainer__ = "chriskane816@gmail.com"
__version__ = "0.1"
__status__ = "Prototype"

import sys
sys.path.append("/home/chriswachira/Desktop/commissioner/")
from logic.date import Date, DateFormatter
from logic.database import Database
from logic.globalizer import Globalizer

class Agent():
	def __init__(self):
		self.db = Database("agents") 	# initialize database connection

	def attribs(self, **kwargs):
		gl = Globalizer("agent", "agents", "AGENTS")
	
		self.id = gl.get_globalID()
		self.firstname = kwargs.get('firstname')
		self.lastname = kwargs.get('lastname')
		self.DOA = kwargs.get('DOA')
		self.intro = kwargs.get('intro')
		self.cell = kwargs.get('cell')
		self.NID = kwargs.get('NID')
		self.gender = kwargs.get('gender')
		self.memo = kwargs.get('memo')

	def insert_attribs(self):
		self.db.sql_do("""INSERT INTO AGENTS VALUES
		(?,?,?,?,?,?,?,?,?)""", self.id, self.firstname, self.lastname, self.DOA, self.intro, self.cell, self.NID, self.gender, self.memo)
		self.db.close()


def get_curr_date():
        date = Date()
        
        dd = date.get_day()
        mm = date.get_month()
        yyyy = date.get_year()
        
        df = DateFormatter(dd, mm, yyyy)
        curr_date = df.add_format("-")
        return curr_date

def main():
        print("----CREATE NEW AGENT HERE!----")
        
        agent = Agent()

        fname = input("Enter first name: ")
        lname = input("Enter last name: ") 
        inp_doa = get_curr_date()
        inp_intro = input("Enter intro: ")
        inp_cell = input("Enter phone number: ")
        n_id = input("Enter National ID: ")
        inp_gender = input("Enter gender (M/F): ")

        agent.attribs(firstname=fname, lastname=lname, DOA=inp_doa, intro=inp_intro, cell=inp_cell, NID=n_id, gender=inp_gender)
        agent.insert_attribs()
        print("AGENT ID - " + agent.id)
        print("First name: " + agent.firstname.title())
        print("Last name: " + agent.lastname.title())
        print("Date of Admission: " + agent.DOA)
        print("Agent Level: " + agent.intro)
        print("Agent Cell: " + agent.cell)
        print("National ID: " + agent.NID)
        print("Agent\'s gender: " + agent.gender)

if __name__ == "__main__":
        main()
