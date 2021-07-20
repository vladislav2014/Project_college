import random
import string

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon

import form
from errors import showDialog, showInfo, showInfouser, showSave, showDelete, showError
from form import *
import sys
from config import *
import pymysql
from operationMySQL import *
from random import randint


class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.generate.clicked.connect(self.generate)
        self.ui.save.clicked.connect(self.save_login_and_password)
        self.set_nameGroup()
        self.ui.remind_student.clicked.connect(self.open_remind)
        self.ui.close_remind.clicked.connect(self.close_remind)
        self.ui.remind.clicked.connect(self.remind_login_password)
        self.ui.openDelete.clicked.connect(self.openDelete)
        self.ui.deleteStudent.clicked.connect(self.delete_student)
        self.ui.go_back.clicked.connect(self.close_delete)

    def generate(self):
        self.set_name_group = self.ui.name_group.currentText()
        self.check_input_name_and_secondName()

    def check_input_name_and_secondName(self):
        self.name_edit = self.ui.name_edit.text()
        self.secondName = self.ui.secondName_edit.text()
        self.name_edit = self.name_edit.upper()
        self.secondName = self.secondName.upper()
        if self.name_edit == "" or self.secondName == "":
            showInfo(self)
        else:
            self.check_origin_name_and_secondName()

    def check_origin_name_and_secondName(self):
        self.origin_name = self.ui.name_edit.text()
        self.origin_secondName = self.ui.secondName_edit.text()
        self.origin_name = self.origin_name.upper()
        self.origin_secondName = self.origin_secondName.upper()
        check_origin_name_and_secondName(self)
        if self.origin_student != ():
            showDialog(self)
            self.ui.gen_login.clear()
            self.ui.gen_password.clear()
        else:
            self.generate_login_student()
            self.generate_password()

    def generate_login_student(self):
        self.login_student = []
        for i in range(4):
            random_number = randint(0, 9)
            self.login_student.append(random_number)
        self.login_student = (''.join(map(str, self.login_student)))
        generate_login(self)
        self.result_name_group = self.name_group[0]
        self.result_login = self.result_name_group + self.login_student
        check_origin_login(self)
        if self.origin_login != ():
            self.generate_login_student()
        else:
            self.ui.gen_login.setText(self.result_login)

    def generate_password(self):
        self.password_student = []
        letters = string.ascii_lowercase
        for i in range(5):
            random_password = randint(0, 9)
            self.password_student.append(random_password)
        self.password_student = (''.join(map(str, self.password_student)))
        self.password_student += (''.join(random.choice(letters) for i in range(1)))
        check_origin_password(self)
        if self.origin_password != ():
            self.generate_password()
        else:
            self.ui.gen_password.setText(self.password_student)

    def save_login_and_password(self):
        self.itog_login = self.ui.gen_login.text()
        self.itog_password = self.ui.gen_password.text()
        if self.itog_login == "":
            showError(self)
        else:
            insert_login_password(self)
            self.ui.gen_login.clear()
            self.ui.gen_password.clear()
            self.ui.name_edit.clear()
            self.ui.secondName_edit.clear()
            showSave(self)

    def set_nameGroup(self):
        mylist = change_group(self)
        for i in range(len(mylist)):
            self.ui.name_group.addItem(mylist[i])
            self.ui.group_remind.addItem(mylist[i])
            self.ui.group_delete.addItem(mylist[i])

    def open_remind(self):
        self.ui.stackedWidget.setCurrentIndex((self.ui.stackedWidget.currentIndex() + 1) % 2)
        self.ui.gen_login.clear()
        self.ui.gen_password.clear()
        self.ui.name_edit.clear()
        self.ui.secondName_edit.clear()

    def close_remind(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.old_login.clear()
        self.ui.old_password.clear()
        self.ui.name_remind.clear()
        self.ui.secondName_remind.clear()

    def remind_login_password(self):
        self.remind_name = self.ui.name_remind.text()
        self.remind_secondName = self.ui.secondName_remind.text()
        if self.remind_name != "" and self.remind_secondName != "":
            self.remind_nameGroup = self.ui.group_remind.currentText()
            remind_login_password_sql(self)
            self.check_input_remind()
        else:
            showInfo(self)
            self.ui.old_login.clear()
            self.ui.old_password.clear()

    def check_input_remind(self):
        if self.allInfo != ():
            self.ui.old_login.setText(self.rlogin)
            self.ui.old_password.setText(self.rpassword)
        else:
            self.ui.old_login.clear()
            self.ui.old_password.clear()
            showInfouser(self)

    def openDelete(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def delete_student(self):
        self.name_delete = self.ui.name_delete.text()
        self.name_delete = self.name_delete.upper()
        self.secondName_delete = self.ui.secondName_delete.text()
        self.secondName_delete = self.secondName_delete.upper()
        self.deleteGroup = self.ui.group_delete.currentText()
        if self.name_delete == "" or self.secondName_delete == "":
            showInfo(self)
        else: self.check_del_info()

    def check_del_info(self):
        check_deleteUser(self)
        if self.allInfo != ():
            deleteUser(self)
            showDelete(self)
            self.ui.name_delete.clear()
            self.ui.secondName_delete.clear()
        else:
            showInfouser(self)

    def close_delete(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.name_delete.clear()
        self.ui.secondName_delete.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    mywin.setWindowIcon(QIcon("login.png"))
    style = """
    QWidget{
        background: rgb(67, 100, 145);
    }
    
    QPushButton, QLineEdit, QLabel, QComboBox {
        background-color: white;
        padding: 3px;
        margin: 0 3 0 3;
        font-size: 17px;
        border-radius: 5px;
        font-family: Cambria;
    }
    
    QComboBox QAbstractItemView {
            border: 1px solid grey;
            background: white;
            selection-background-color: light blue;
        }
        
    """
    app.setStyleSheet(style)
    mywin.setMaximumSize(540, 390)
    app.exec_()
