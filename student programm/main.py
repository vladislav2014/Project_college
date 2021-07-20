from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidgetItem

import form
from form import *
import sys
import connect_testBD
from connect_testBD import *
import operation_TestforStudent
from operation_TestforStudent import *
import pymysql
from dialogs import *


class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = form.Ui_Form()
        self.ui.setupUi(self)
        self.value = 0
        self.save_nums = []
        self.true_answer = []
        self.name_question = []
        self.user_ans = []
        self.itog = []
        self.ui.authorization.clicked.connect(self.auth)
        self.ui.next_page.clicked.connect(self.set_name_subject)
        self.ui.back.clicked.connect(self.back_page)
        self.ui.start_test.clicked.connect(self.start_test)
        self.ui.next_question.clicked.connect(self.next_question)
        self.ui.prev_question.clicked.connect(self.prev_question)
        self.ui.end_test.clicked.connect(self.itog_test)
        self.ui.next_tpage.clicked.connect(self.opensetsubject)
        self.ui.back_page.clicked.connect(self.backpage)
        self.ui.check_password.clicked.connect(self.password)
        self.ui.check_raiting.clicked.connect(self.view_result)
        self.ui.backtomenu.clicked.connect(self.backtoMenu)
        self.ui.backfromView.clicked.connect(self.backFromview)
        self.ui.answer1.clicked.connect(lambda: self.get_user_ans(self.ui.answer1.text(), 1))
        self.ui.answer2.clicked.connect(lambda: self.get_user_ans(self.ui.answer2.text(), 2))
        self.ui.answer3.clicked.connect(lambda: self.get_user_ans(self.ui.answer3.text(), 3))
        self.ui.answer4.clicked.connect(lambda: self.get_user_ans(self.ui.answer4.text(), 4))

    def auth(self):
        self.login_student = self.ui.login_student.text()
        self.password_student = self.ui.password_student.text()
        check_login(self)
        take_infoStudent(self)
        if self.id_group_check != ():
            self.check_student()
        else:
            showDialog(self)

    def check_student(self):
        authOk(self)
        self.ui.stackedWidget.setCurrentIndex(1)

    def opensetsubject(self):
        self.set_subject()
        self.ui.stackedWidget.setCurrentIndex(3)

    def set_subject(self):
        mylist = change_subject(self)
        for i in range(len(mylist)):
            self.ui.set_subject.addItem(mylist[i])

    def set_name_subject(self):
        self.name_subject = self.ui.set_subject.currentText()
        set_nameTest(self)
        if self.n_test != ():
            self.name_test()
        else:
            showDialog2(self)

    def name_test(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        mylist = set_nameTest(self)
        for i in range(len(mylist)):
            self.ui.set_nameTest.addItem(mylist[i])

    def back_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.enter_password.clear()
        self.ui.set_nameTest.clear()

    def backtoMenu(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.set_subject.clear()

    def backpage(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.enter_password.clear()

    def backFromview(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.tableWidget.setRowCount(0)

    def start_test(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.nameTest = self.ui.set_nameTest.currentText()
        for btn in [self.ui.answer1, self.ui.answer2, self.ui.answer3, self.ui.answer4]:
            btn.setAutoExclusive(False)
            btn.setChecked(False)
            btn.repaint()
        set_password(self)

    def password(self):
        self.ent_password = self.ui.enter_password.text()
        if self.ent_password == self.setpassword:
            self.ui.stackedWidget.setCurrentIndex(6)
            self.take_question()
            self.get_cor_answ()
            for btn in [self.ui.answer1, self.ui.answer2, self.ui.answer3, self.ui.answer4]:
                btn.setAutoExclusive(True)
                btn.setChecked(False)
                btn.repaint()
        else:
            badpassword(self)

    def take_question(self):
        try:
            connection = pymysql.connect(
                host=host_2,
                port=3306,
                user=user_2,
                database=db_name_2,
                password=password_2,
                cursorclass=pymysql.cursors.DictCursor
            )

            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT id_теста FROM `название тестов` WHERE `название_теста` = (%s) ",
                                   self.nameTest)
                    self.idtest = cursor.fetchone()["id_теста"]
                    connection.commit()

                with connection.cursor() as cursor:
                    cursor.execute("SELECT `вопрос` FROM `вопросы` WHERE `id_теста` = (%s)",
                                   self.idtest)
                    self.n_test = cursor.fetchall()
                    for i in self.n_test:
                        self.name_question.append(str(i['вопрос']))
                    connection.commit()
            finally:
                connection.close()
        except Exception as ex:
            print(ex)
        self.take_answer(self.name_question)

    def take_answer(self, question):
        self.ui.question.setText(str(question[self.value]))
        self.value += 1
        try:
            connection = pymysql.connect(
                host=host_2,
                port=3306,
                user=user_2,
                database=db_name_2,
                password=password_2,
                cursorclass=pymysql.cursors.DictCursor
            )
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT id_теста FROM `название тестов` WHERE `название_теста` = (%s) ",
                                   self.nameTest)
                    self.set_idtest = cursor.fetchone()["id_теста"]

                with connection.cursor() as cursor:
                    cursor.execute("SELECT id_предмета FROM `название тестов` WHERE `название_теста` = (%s) ",
                                   self.nameTest)
                    self.idsubject = cursor.fetchone()["id_предмета"]
                    connection.commit()
                with connection.cursor() as cursor:
                    cursor.execute("SELECT `ответ_на_вопрос` FROM `ответы на вопросы` WHERE `id_теста` = (%s)  "
                                   "AND id_вопроса = (%s)",
                                   (self.set_idtest, self.value))
                    self.set_answer = cursor.fetchall()
                    m = 1
                    for i in self.set_answer:
                        var = eval(f'self.ui.answer{m}')
                        var.setText(i['ответ_на_вопрос'])
                        m += 1
                    connection.commit()
            finally:
                connection.close()
        except Exception as ex:
            print(ex)
        self.value -= 1

    def next_question(self):
        size = len(self.name_question)
        size -= 1
        if self.value < size:
            self.value += 1
            self.take_answer(self.name_question)
            for btn in [self.ui.answer1, self.ui.answer2, self.ui.answer3, self.ui.answer4]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
                btn.repaint()
            if self.save_nums[self.value] == '':
                for btn in [self.ui.answer1, self.ui.answer2, self.ui.answer3, self.ui.answer4]:
                    btn.setAutoExclusive(False)
                    btn.setChecked(False)
                    btn.repaint()
            else:
                if self.save_nums[self.value] == 1:
                    self.ui.answer1.setAutoExclusive(True)
                    self.ui.answer1.setChecked(True)
                    self.ui.answer1.repaint()
                if self.save_nums[self.value] == 2:
                    self.ui.answer2.setAutoExclusive(True)
                    self.ui.answer2.setChecked(True)
                    self.ui.answer2.repaint()
                if self.save_nums[self.value] == 3:
                    self.ui.answer3.setAutoExclusive(True)
                    self.ui.answer3.setChecked(True)
                    self.ui.answer3.repaint()
                if self.save_nums[self.value] == 4:
                    self.ui.answer4.setAutoExclusive(True)
                    self.ui.answer4.setChecked(True)
                    self.ui.answer4.repaint()
            self.ui.answer1.setAutoExclusive(True)
            self.ui.answer2.setAutoExclusive(True)
            self.ui.answer3.setAutoExclusive(True)
            self.ui.answer4.setAutoExclusive(True)
        else:
            self.ui.answer1.setAutoExclusive(True)
            self.ui.answer2.setAutoExclusive(True)
            self.ui.answer3.setAutoExclusive(True)
            self.ui.answer4.setAutoExclusive(True)
            return 0

    def prev_question(self):
        if self.value != 0:
            self.value -= 1
            self.take_answer(self.name_question)
            for btn in [self.ui.answer1, self.ui.answer2, self.ui.answer3, self.ui.answer4]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
                btn.repaint()
            if self.save_nums[self.value] == '':
                for btn in [self.ui.answer1, self.ui.answer2, self.ui.answer3, self.ui.answer4]:
                    btn.setAutoExclusive(False)
                    btn.setChecked(False)
                    btn.repaint()
            else:
                if self.save_nums[self.value] == 1:
                    self.ui.answer1.setAutoExclusive(True)
                    self.ui.answer1.setChecked(True)
                    self.ui.answer1.repaint()
                if self.save_nums[self.value] == 2:
                    self.ui.answer2.setAutoExclusive(True)
                    self.ui.answer2.setChecked(True)
                    self.ui.answer2.repaint()
                if self.save_nums[self.value] == 3:
                    self.ui.answer3.setAutoExclusive(True)
                    self.ui.answer3.setChecked(True)
                    self.ui.answer3.repaint()
                if self.save_nums[self.value] == 4:
                    self.ui.answer4.setAutoExclusive(True)
                    self.ui.answer4.setChecked(True)
                    self.ui.answer4.repaint()
            self.ui.answer1.setAutoExclusive(True)
            self.ui.answer2.setAutoExclusive(True)
            self.ui.answer3.setAutoExclusive(True)
            self.ui.answer4.setAutoExclusive(True)
        else:
            return 0

    def get_cor_answ(self):
        try:
            connection = pymysql.connect(
                host=host_2,
                port=3306,
                user=user_2,
                database=db_name_2,
                password=password_2,
                cursorclass=pymysql.cursors.DictCursor
            )
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT id_теста FROM `название тестов` WHERE `название_теста` = (%s) ",
                                   self.nameTest)
                    self.set_idtest = cursor.fetchone()["id_теста"]
                    connection.commit()
                with connection.cursor() as cursor:
                    cursor.execute("SELECT id_предмета FROM `название тестов` WHERE `название_теста` = (%s) ",
                                   self.nameTest)
                    self.idsubject = cursor.fetchone()["id_предмета"]
                    connection.commit()

                with connection.cursor() as cursor:
                    cursor.execute("SELECT `ответ_на_вопрос` FROM `ответы на вопросы` WHERE `id_теста` = (%s) AND "
                                   "  `верность_ответа` = 'Да' ",
                                   self.set_idtest)
                    self.tanswer = cursor.fetchall()
                    for i in self.tanswer:
                        self.user_ans.append('')
                        self.save_nums.append('')
                        self.true_answer.append(i['ответ_на_вопрос'])
                    connection.commit()
            finally:
                connection.close()
        except Exception as ex:
            print(ex)

    def get_user_ans(self, ans, nums):
        self.user_ans[self.value] = ans
        self.save_nums[self.value] = nums

    def itog_test(self):
        size = len(self.user_ans)
        result = 0
        self.raiting = 2
        for i in range(size):
            if self.user_ans[i - 1] == self.true_answer[i - 1]:
                result += 1
        self.itog_result = result * 100 / len(self.n_test)
        if self.itog_result < 50:
            self.raiting = 2
        elif 50 < self.itog_result < 75:
            self.raiting = 3
        elif 76 < self.itog_result < 85:
            self.raiting = 4
        elif 86 < self.itog_result <= 100:
            self.raiting = 5
        insert_result(self)
        resultDialog(self)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.clearall()

    def view_result(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        check_result(self)
        row = len(self.raiting)
        self.ui.tableWidget.setRowCount(row)
        for i in range(row):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(self.tns))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(self.tsns))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(str(self.resultnamesubject[i])))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(self.resultnametest[i])))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(self.raiting[i])))

    def clearall(self):
        self.ui.set_nameTest.clear()
        self.ui.set_subject.clear()
        self.ui.enter_password.clear()
        self.value = 0
        self.save_nums = []
        self.true_answer = []
        self.name_question = []
        self.user_ans = []
        self.itog = []
        for btn in [self.ui.answer1, self.ui.answer2, self.ui.answer3, self.ui.answer4]:
            btn.setAutoExclusive(False)
            btn.setChecked(False)
            btn.repaint()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    mywin.setWindowIcon(QIcon("test.png"))
    style = """
        QWidget {
            background: rgb(20, 137, 166);
        }
        
        QLabel#label_4,  QLabel#label, QLabel#label_2,QLabel#label_3{
            font-size: 32px;
            padding: 15px;
            font-weight: bold;
            border-radius: 15px;
        }
        
        QPushButton#next_tpage, QPushButton#check_raiting{
            padding: 10px;
        }
        
        QPushButton, QLineEdit, QLabel{
            background-color: white;
            padding: 3px;
            margin: 0 3 0 3;
            font-size: 17px;
            border-radius: 5px;
        }
        QRadioButton {
            font-size: 18px;
            background-color: white;
            padding-left: 15px;
            padding-top: 7px;
            padding-bottom: 7px;
            border-radius: 5px;
        }
        
        QLineEdit#question {
            font-size: 21px;
            
        }
        
        QTableWidget:item {
            background:  rgb(225, 228, 232);
            border:0px;
            
        }
        
        QComboBox {
            font-family: Times New Roman;
            font-size: 20px;
            background: rgba(255, 255, 255, 0.8);
        }
        
        
QComboBox QAbstractItemView {
            border: 1px solid grey;
            background: white;
            selection-background-color: light blue;
        }
        
        QComboBox:active {
            background:none;
        }
    
    """
    app.setStyleSheet(style)
    app.exec_()
