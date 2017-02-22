"""
        -       Agent module as part of the Commissioner system's GUI 
        -       This module create a graphical user interface for a user to interact
        -       It will allow users to view Agent's details, create new, save and delete.

"""

__author__ = "Chris Wachira"
__maintainer__ = "chriskane816@gmail.com"
__version__ = "0.1"
__status__ = "Prototype"

import sys
sys.path.append("/home/chriswachira/Desktop/commissioner")
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from logic.database import Database
from logic.globalizer import Globalizer
from logic.indexer import Indexer
from logic.agent import Agent, get_curr_date
from logic.other_funcs import get_prefix, join_prefix

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 550)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(20, 20, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        
        self.lblAgentID = QtWidgets.QLabel(self.centralwidget)
        self.lblAgentID.setGeometry(QtCore.QRect(20, 120, 81, 18))
        self.lblAgentID.setObjectName("lblAgentID")
        
        self.lblDisplayID = QtWidgets.QLabel(self.centralwidget)
        self.lblDisplayID.setGeometry(QtCore.QRect(130, 120, 101, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lblDisplayID.setFont(font)
        self.lblDisplayID.setObjectName("lblDisplayID")
        
        self.lblFirstName = QtWidgets.QLabel(self.centralwidget)
        self.lblFirstName.setGeometry(QtCore.QRect(20, 190, 81, 18))
        self.lblFirstName.setObjectName("lblFirstName")
        
        self.lblLastName = QtWidgets.QLabel(self.centralwidget)
        self.lblLastName.setGeometry(QtCore.QRect(20, 250, 71, 18))
        self.lblLastName.setObjectName("lblLastName")
        
        self.lblIntro = QtWidgets.QLabel(self.centralwidget)
        self.lblIntro.setGeometry(QtCore.QRect(20, 310, 59, 18))
        self.lblIntro.setObjectName("lblIntro")
        
        self.lblCell = QtWidgets.QLabel(self.centralwidget)
        self.lblCell.setGeometry(QtCore.QRect(480, 120, 101, 18))
        self.lblCell.setObjectName("lblCell")
        
        self.lblDOA = QtWidgets.QLabel(self.centralwidget)
        self.lblDOA.setGeometry(QtCore.QRect(480, 180, 59, 18))
        self.lblDOA.setObjectName("lblDOA")
        
        self.lblNID = QtWidgets.QLabel(self.centralwidget)
        self.lblNID.setGeometry(QtCore.QRect(480, 240, 101, 18))
        self.lblNID.setObjectName("lblNID")
        
        self.lblGender = QtWidgets.QLabel(self.centralwidget)
        self.lblGender.setGeometry(QtCore.QRect(480, 300, 59, 18))
        self.lblGender.setObjectName("lblGender")
        
        self.lblMemo = QtWidgets.QLabel(self.centralwidget)
        self.lblMemo.setGeometry(QtCore.QRect(20, 360, 59, 18))
        self.lblMemo.setObjectName("lblMemo")

       
        
        self.btnNew = QtWidgets.QPushButton(self.centralwidget)
        self.btnNew.setGeometry(QtCore.QRect(620, 360, 181, 31))
        self.btnNew.setObjectName("btnNew")
        self.btnNew.clicked.connect(self.btnNewClicked)
        
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(620, 400, 88, 34))
        self.btnSave.setObjectName("btnSave")
        self.btnSave.clicked.connect(self.btnSaveClicked)
        
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(710, 400, 91, 34))
        self.btnDelete.setObjectName("btnDelete")
        self.btnDelete.clicked.connect(self.btnDeleteClicked)
        
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(620, 440, 181, 34))
        self.btnExit.setObjectName("btnExit")
        self.btnExit.clicked.connect(self.btnExitClicked)
        
        self.btnPrevious = QtWidgets.QPushButton(self.centralwidget)
        self.btnPrevious.setGeometry(QtCore.QRect(620, 20, 81, 34))
        self.btnPrevious.setObjectName("btnPrevious")
        self.btnPrevious.clicked.connect(self.btnPreviousClicked)
        
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setGeometry(QtCore.QRect(717, 20, 81, 34))
        self.btnNext.setObjectName("btnNext")
        self.btnNext.clicked.connect(self.btnNextClicked)
        
        self.ledtFirstName = QtWidgets.QLineEdit(self.centralwidget)
        self.ledtFirstName.setGeometry(QtCore.QRect(120, 180, 221, 32))
        self.ledtFirstName.setObjectName("ledtFirstName")
        
        self.ledtLastName = QtWidgets.QLineEdit(self.centralwidget)
        self.ledtLastName.setGeometry(QtCore.QRect(120, 240, 221, 32))
        self.ledtLastName.setObjectName("ledtLastName")
        
        self.ledtIntro = QtWidgets.QLineEdit(self.centralwidget)
        self.ledtIntro.setGeometry(QtCore.QRect(120, 300, 91, 32))
        self.ledtIntro.setObjectName("ledtIntro")
        
        self.ledtCell = QtWidgets.QLineEdit(self.centralwidget)
        self.ledtCell.setGeometry(QtCore.QRect(620, 120, 181, 32))
        self.ledtCell.setObjectName("ledtCell")

        self.btnDatePicker = QtWidgets.QPushButton(self.centralwidget)
        self.btnDatePicker.setGeometry(QtCore.QRect(620, 170, 181, 34))
        self.btnDatePicker.setObjectName("btnDatePicker")
        self.btnDatePicker.clicked.connect(self.showDatePicker)
        
        #self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        #self.calendarWidget.setGeometry(QtCore.QRect(530,200, 272, 240))
        #self.calendarWidget.setObjectName("calendarWidget")

        self.ledtNID = QtWidgets.QLineEdit(self.centralwidget)
        self.ledtNID.setGeometry(QtCore.QRect(620, 230, 181, 32))
        self.ledtNID.setObjectName("ledtNID")
        
        self.radioMale = QtWidgets.QRadioButton(self.centralwidget)
        self.radioMale.setGeometry(QtCore.QRect(620, 300, 71, 22))
        self.radioMale.setObjectName("radioMale")
        
        self.radioFemale = QtWidgets.QRadioButton(self.centralwidget)
        self.radioFemale.setGeometry(QtCore.QRect(730, 300, 105, 22))
        self.radioFemale.setObjectName("radioFemale")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 360, 341, 111))
        self.textEdit.setObjectName("textEdit")
        
        self.ledtSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.ledtSearch.setGeometry(QtCore.QRect(620, 70, 181, 32))
        self.ledtSearch.setObjectName("ledtSearch")

        self.lblAgentIntroName = QtWidgets.QLabel(self.centralwidget)
        self.lblAgentIntroName.setGeometry(QtCore.QRect(220, 300, 241, 31))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitle.setText(_translate("MainWindow", "Agent Sheet"))
        self.lblAgentID.setText(_translate("MainWindow", "Agent ID"))
        self.lblDisplayID.setText(_translate("MainWindow", "TextLabel"))
        self.lblFirstName.setText(_translate("MainWindow", "First Name"))
        self.lblLastName.setText(_translate("MainWindow", "Last Name"))
        self.lblIntro.setText(_translate("MainWindow", "Intro"))
        self.lblCell.setText(_translate("MainWindow", "Phone Number"))
        self.lblDOA.setText(_translate("MainWindow", "D.O.A."))
        self.lblNID.setText(_translate("MainWindow", "National ID"))
        self.lblGender.setText(_translate("MainWindow", "Gender"))
        self.lblMemo.setText(_translate("MainWindow", "Memo"))
        self.btnNew.setText(_translate("MainWindow", "New"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnExit.setText(_translate("MainWindow", "EXIT"))
        self.btnPrevious.setText(_translate("MainWindow", "Previous"))
        self.btnNext.setText(_translate("MainWindow", "Next"))
        self.btnDatePicker.setText(_translate("MainWindow", "Select Date"))
        self.radioMale.setText(_translate("MainWindow", "&Male"))
        self.radioFemale.setText(_translate("MainWindow", "Fema&le"))
        self.lblAgentIntroName.setText(_translate("MainWindow", "TextLabel"))

    def showDatePicker(self):

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(530,200, 272, 240))
        self.calendarWidget.setObjectName("calendarWidget")

        Ui_MainWindow.setupUi(self.calendarWidget)
        self.calendarWidget.show()
        
#class DatePicker(self):
 #               def __init__(self):
  #                      _ui = Ui_MainWindow()
#
     #           def getSelectedDate(self):
  #                       return _ui.setupUi.calendarWidget.selectedDate()



    def get_attribs(self, agent):
        #
        #       Gets records from the Agents database and displays them on the Agents Form
        #       It uses a agent variable that will be used to select a record from the database
        #
        
        agent_id = None
        prefix = get_prefix('agent')    #       Get prefix from other_funcs
        agent_id = join_prefix(prefix, agent)   #       Get global ID from other_funcs

        db = Database("agents")
        row = db.sql_do("SELECT * FROM AGENTS WHERE ID = ?", agent_id)
        for attribs in row:
            pass
        
        agent_firstName = attribs[1].title()
        agent_lastName = attribs[2].title()
        doa = attribs[3].split("-")
        agent_doa = doa[0] + doa[1] + doa[2]
        agent_intro = attribs[4]
        agent_cell = attribs[5]
        agent_NID = attribs[6]
        agent_gender = attribs[7]
        agent_memo = attribs[8]
    
        self.lblDisplayID.setText(agent_id)
        self.ledtFirstName.setText(agent_firstName)
        self.ledtLastName.setText(agent_lastName)
        self.ledtCell.setText(agent_cell)
        self.ledtNID.setText(agent_NID)
        
        if agent_intro == "-":
            self.ledtIntro.setText("---")
            self.lblAgentIntroName.setText("--COMPANY--")
        else:
            _conn = Database("agents")
            row = _conn.sql_do("SELECT FIRSTNAME, LASTNAME FROM AGENTS WHERE ID=?", agent_intro)
            for r in row:   pass
            first_name = r[0].upper()
            last_name = r[1].upper()
            self.ledtIntro.setText(agent_intro)
            self.lblAgentIntroName.setText(first_name + " " + last_name)
        
        if agent_gender == 'm':
            self.radioMale.setChecked(True)
        else:
            self.radioFemale.setChecked(True)

    def btnNewClicked(self):
        #
        #       Clears all textboxes to allow entry of a new record
        #
        self.ledtFirstName.clear()
        self.ledtLastName.clear()
        self.ledtIntro.clear()
        self.ledtCell.clear()
        self.ledtNID.clear()
        self.lblAgentIntroName.clear()
        #self.tedtMemo.clear()

        gl = Globalizer("agent", "agents", "AGENTS")
        self.lblDisplayID.setText(gl.get_globalID())

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

    def btnSaveClicked(self):
        #
        #       Inserts new record attributes to database. Will only update if record already exists
        #

        agent_id = self.lblDisplayID.text()
        firstname = self.ledtFirstName.text()
        lastname = self.ledtLastName.text()
        intro = self.ledtIntro.text()[0:6]
        cell = self.ledtCell.text()
        NID = self.ledtNID.text()
        memo = self.tedtMemo.toPlainText()
        if self.radioMale.isChecked():
            gender = 'm'
        else: 
            gender = 'f'

        _db = Database("agents")
        id_list = []
        ids = _db.sql_do("SELECT ID FROM AGENTS")
        for i in ids:
            id_list.append(i)

        for item in id_list:
            if agent_id not in item[0]:
                self.create_new()
                break
            else:
                print("Agent already in database!")
                _db.sql_do("""UPDATE AGENTS SET FIRSTNAME=?,LASTNAME=?,INTRO=?,CELL=?,NID=?,GENDER=? WHERE ID=?""",firstname, lastname, intro, cell, NID, gender, agent_id)

                db.close()

    def btnDeleteClicked(self):
        #
        #       Deletes a record when Delete button is pressed
        #
        currently_viewed = self.lblDisplayID.text()
        _db = Database("agents")
        _db.sql_do("DELETE FROM AGENTS WHERE ID=?",currently_viewed)
        _db.close()

    def btnExitClicked(self):
        #
        #       Exits the interface when Exit button is pressed
        #
        sys.exit()

    def create_new(self):
        #
        #       Gets newly inserted Agent attributes and inserts them into the Agent's attributes. It works with
        #       the Agent module from the logic package
        #
        _agent = Agent()    # initialize instance of Agent class from logic package

        fname = self.ledtFirstName.text()
        lname = self.ledtLastName.text()
        inp_DOA = get_curr_date()
        inp_intro = self.ledtIntro.text()
        inp_cell = self.ledtCell.text()
        inp_NID = self.ledtNID.text()
        
        if self.radioMale.isChecked():
            inp_gender = 'm'
        else: 
            inp_gender = 'f'
        
        inp_Memo = self.tedtMemo.toPlainText()

        _agent.attribs(firstname=fname, lastname=lname, DOA=inp_DOA, intro=inp_intro, cell=inp_cell, NID=inp_NID, gender=inp_gender, memo=inp_Memo)
        _agent.insert_attribs()

        print("First Name: " + _agent.firstname)
        print("Last Name: " + _agent.lastname)
        print("Date of Admission: " + _agent.DOA)
        print("Agent Introduced by: " + _agent.intro)
        print("Agent's Cell No.: " + _agent.cell)
        print("Agent's NID: " + _agent.NID)
        print("Agent\'s gender: " + _agent.gender)             
    
                 

if __name__ == "__main__":
        app = QApplication(sys.argv)

        window = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(window)
        window.show()
        window.move(QtWidgets.QApplication.desktop().screen().rect().center() - window.rect().center())
        
        index = Indexer("agents", "AGENTS")
        ui.get_attribs(index.get_last())

        sys.exit(app.exec_())  

