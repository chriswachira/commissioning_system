"""

        - Indexer module as part of the Commissioner System's logic.

        - This module is supposed to facilitate the indexing of newly added
          objects across the system, i.e. Agents and Customers.

        - It checks the last ID in an Agent's or Customer's database and 
          provides a new ID from the last ID by adding one to it.

        - Requires parameters of the database filename and the table name

"""

__author__ = "Chris Wachira"
__version__ = "0.1"
__maintainer__ = "chriskane816@gmail.com"
__status__ = "Prototype"

import sys
sys.path.append("/home/chriswachira/Desktop/commissioner")

from logic.database import Database

class Indexer():
        def __init__(self, filename, tablename):
                db = Database(filename) # initialize database connection
                self.last_id = None     # initialize last_id variable

                id_list = []
                ids = db.sql_do("SELECT ID FROM {0}".format(tablename)) # get all IDs from table
                for row in ids:
                        id_list.append(row)

                if len(id_list) != 0:
                        self.last_id = int(id_list[-1][0][-3:])     # get last digit of lastly inserted ID
                else:
                        self.last_id = 0
                        print("No record yet at the {0} table".format(tablename.upper()))

        def get_last(self):
                return self.last_id
        
        def get_new(self):
                new_id = int(self.last_id) + 1
                return new_id
