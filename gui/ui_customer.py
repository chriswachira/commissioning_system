"""
    - Customer module as part of the Commissioning system's GUI
    
    - This module creates a graphical user interface that the user will interact with
    
    - Users can view Customer details, create new, save and delete.

"""

__author__  = "Chris Wachira"
__version__ = "0.1"
__maintainer__ = "chriskane816@gmail.com"
__status__ = "Prototype"

import sys
sys.path.append("/home/chriswachira/Desktop/commissioner")
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from logic.database import Database
from logic.globalizer import Globalizer
from logic.indexer import Indexer
from logic.agent import Agent
from logic.other_funcs import get_prefix, join_prefix

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(40, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        
        self.lblCustomerID = QtWidgets.QLabel(self.centralwidget)
        self.lblCustomerID.setGeometry(QtCore.QRect(40, 100, 101, 18))
        self.lblCustomerID.setObjectName("lblCustomerID")
        
        self.lblDisplayID = QtWidgets.QLabel(self.centralwidget)
        self.lblDisplayID.setGeometry(QtCore.QRect(170, 100, 121, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblDisplayID.setFont(font)
        self.lblDisplayID.setObjectName("lblDisplayID")
        
        self.lblCustomerName = QtWidgets.QLabel(self.centralwidget)
        self.lblCustomerName.setGeometry(QtCore.QRect(40, 150, 59, 18))
        self.lblCustomerName.setObjectName("lblCustomerName")
        
        self.lblCell = QtWidgets.QLabel(self.centralwidget)
        self.lblCell.setGeometry(QtCore.QRect(40, 220, 111, 18))
        self.lblCell.setObjectName("lblCell")
        
        self.lblAddress = QtWidgets.QLabel(self.centralwidget)
        self.lblAddress.setGeometry(QtCore.QRect(510, 100, 59, 18))
        self.lblAddress.setObjectName("lblAddress")
        
        self.lblIntro = QtWidgets.QLabel(self.centralwidget)
        self.lblIntro.setGeometry(QtCore.QRect(40, 290, 111, 18))
        self.lblIntro.setObjectName("lblIntro")
        
        self.lblEmail = QtWidgets.QLabel(self.centralwidget)
        self.lblEmail.setGeometry(QtCore.QRect(510, 290, 59, 18))
        self.lblEmail.setObjectName("lblEmail")
        
        self.lblMemo = QtWidgets.QLabel(self.centralwidget)
        self.lblMemo.setGeometry(QtCore.QRect(40, 350, 59, 18))
        self.lblMemo.setObjectName("lblMemo")
        
        self.tedtMemo = QtWidgets.QTextEdit(self.centralwidget)
        self.tedtMemo.setGeometry(QtCore.QRect(170, 350, 371, 111))
        self.tedtMemo.setObjectName("tedtMemo")
        
        self.btnNew = QtWidgets.QPushButton(self.centralwidget)
        self.btnNew.setGeometry(QtCore.QRect(570, 350, 221, 34))
        self.btnNew.setObjectName("btnNew")
        
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(570, 390, 111, 34))
        self.btnSave.setObjectName("btnSave")
        self.btnSave.clicked.connect(self.btnSaveClicked)

        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(690, 390, 101, 34))
        self.btnDelete.setObjectName("btnDelete")
        self.btnDelete.clicked.connect(self.btnDeleteClicked)

        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(570, 430, 221, 34))
        self.btnExit.setObjectName("btnExit")
        self.btnExit.clicked.connect(self.btnExitClicked)

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(600, 20, 191, 32))
        self.dateEdit.setObjectName("dateEdit")
        
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setGeometry(QtCore.QRect(700, 60, 88, 34))
        self.btnNext.setObjectName("btnNext")
        self.btnNext.clicked.connect(self.btnNextClicked)

        self.btnPrevious = QtWidgets.QPushButton(self.centralwidget)
        self.btnPrevious.setGeometry(QtCore.QRect(600, 60, 88, 34))
        self.btnPrevious.setObjectName("btnPrevious")
        self.btnPrevious.clicked.connect(self.btnPreviousClicked)

        self.ledtCustomerName = QtWidgets.QLineEdit(self.centralwidget)
        self.ledtCustomerName.setGeometry(QtCore.QRect(170, 145, 241, 32))
        self.ledtCustomerName.setObjectName("ledtCustomerName")

        self.ledtCell = QtWidgets.QLineEdit(self.centralwidget)
        self.ledtCell.setGeometry(QtCore.QRect(170, 215, 241, 32))
        self.ledtCell.setObjectName("ledtCell")
        
        self.ledtIntro = QtWidgets.QLineEdit(self.centralwidget)
        self.ledtIntro.setGeometry(QtCore.QRect(170, 285, 91, 31))
        self.ledtIntro.setObjectName("ledtIntro")
        
        self.tedtAddress = QtWidgets.QTextEdit(self.centralwidget)
        self.tedtAddress.setGeometry(QtCore.QRect(510, 140, 281, 131))
        self.tedtAddress.setObjectName("tedtAddress")
        
        self.ledtEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.ledtEmail.setGeometry(QtCore.QRect(570, 285, 221, 32))
        self.ledtEmail.setObjectName("ledtEmail")

        self.lblAgentIntroName = QtWidgets.QLabel(self.centralwidget)
        self.lblAgentIntroName.setGeometry(QtCore.QRect(280, 285, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblAgentIntroName.setFont(font)
        self.lblAgentIntroName.setObjectName("lblAgentIntroName")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 30))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Customers"))
        self.lblTitle.setText(_translate("MainWindow", "Customers"))
        self.lblCustomerID.setText(_translate("MainWindow", "Customer ID"))
        self.lblDisplayID.setText(_translate("MainWindow", "TextLabel"))
        self.lblCustomerName.setText(_translate("MainWindow", "Name"))
        self.lblCell.setText(_translate("MainWindow", "Phone Number"))
        self.lblAddress.setText(_translate("MainWindow", "Address"))
        self.lblIntro.setText(_translate("MainWindow", "Introduced by:"))
        self.lblEmail.setText(_translate("MainWindow", "Email"))
        self.lblMemo.setText(_translate("MainWindow", "Memo"))
        self.btnNew.setText(_translate("MainWindow", "New"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnExit.setText(_translate("MainWindow", "EXIT"))
        self.btnNext.setText(_translate("MainWindow", "Next"))
        self.btnPrevious.setText(_translate("MainWindow", "Previous"))
        self.lblAgentIntroName.setText(_translate("MainWindow", "TextLabel"))

    def get_attribs(self, customer):
        """Gets records from the Customers' database and displays them on the Custmomers' Form"""
        """It uses a customer variable that will be used to select a record from the database"""
        
        customer_id = None
        prefix = get_prefix('customer')
        customer_id = join_prefix(prefix, customer)

        db = Database("customers")
        row = db.sql_do("SELECT * FROM CUSTOMERS WHERE ID = ?", customer_id)
        for attribs in row:
            pass

        cust_name = attribs[1]
        cust_cell = attribs[2]
        cust_address = attribs[3]
        cust_email = attribs[4]
        cust_intro = attribs[5]
        cust_memo = attribs[6]

        self.lblDisplayID.setText(customer_id)
        self.ledtCustomerName.setText(cust_name)
        self.ledtCell.setText(cust_cell)
        self.ledtEmail.setText(cust_email)

        if cust_intro == "-":
            self.ledtIntro.setText("---")
            self.lblAgentIntroName.setText("--COMPANY--")
        else:
            _conn = Database("agents")
            row = _conn.sql_do("SELECT FIRSTNAME, LASTNAME FROM AGENTS WHERE ID=?", cust_intro)
            for r in row: pass
            first_name = r[0].upper()
            last_name = r[1].upper()
            self.ledtIntro.setText(cust_intro)
            self.lblAgentIntroName.setText(first_name + " " + last_name)

    def btnNextClicked(self):
        #
        #       Shows the next record up in the database
        #
        try:
            currently_viewed = int(self.lblDisplayID.text()[-3:]) # gets the ID that is being currently viewed on the GUI
            self.get_attribs(currently_viewed + 1)
        except UnboundLocalError:
            print("Reached the end.")

    def btnPreviousClicked(self):
        #
        #       Shows the next record down in the database
        #
        try:
            currently_viewed = int(self.lblDisplayID.text()[-3:])
            self.get_attribs(currently_viewed - 1)
        except UnboundLocalError:
            print("Reached the end.")

    def btnNewClicked(self):
        #
        #       Clears all textboxes to allow entry of a new record
        #
        self.ledtCustomerName.clear()
        self.ledtIntro.clear()
        self.ledtCell.clear()
        self.ledtEmail.clear()
        #self.tedtMemo.clear()

        gl = Globalizer("customer", "customers", "CUSTOMERS")   # Initialize Globalizer Class from logic package        
        self.lblDisplayID.setText(gl.get_globalID())      #     Get a new global ID to display on GUI

if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(window)
        window.show()
        window.move(QtWidgets.QApplication.desktop().screen().rect().center() - window.rect().center())
        
        index = Indexer("customers", "CUSTOMERS")
        ui.get_attribs(index.get_last())

        sys.exit(app.exec_())
