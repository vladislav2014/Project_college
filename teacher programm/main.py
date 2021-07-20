import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from form import *
from config import *
import operation_MYSQL
from operation_MYSQL import *
from tests_for_createTest import *
import pymysql


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.value = 0
        self.counter_value = self.value
        self.index = 0
        self.counter = 0
        self.count = 0
        self.answerNumber = []
        self.massQuestion = []
        self.massAnswer1 = []
        self.massAnswer2 = []
        self.massAnswer3 = []
        self.massAnswer4 = []
        self.massTrueAnswer1 = []
        self.massTrueAnswer2 = []
        self.massTrueAnswer3 = []
        self.massTrueAnswer4 = []
        self.ui.create_test_btn.clicked.connect(self.open_create_test)
        self.ui.edit_test_btn.clicked.connect(self.open_edit_test)
        self.ui.education_btn.clicked.connect(self.education)
        self.ui.next_education.clicked.connect(self.next_education)
        self.ui.prev_education.clicked.connect(self.prev_education)
        self.ui.main_menu.clicked.connect(self.main_menu)
        self.ui.next_page_create.clicked.connect(self.nextCreate)
        self.ui.prev_page_create.clicked.connect(self.prevCreate)
        self.ui.return_from_edit.clicked.connect(self.main_menu)
        self.ui.return_from_create.clicked.connect(self.main_menu)
        self.ui.next_create.clicked.connect(self.next_create_test)
        self.ui.end_create.clicked.connect(self.end)
        self.ui.goto_main.clicked.connect(self.main_menu)
        self.ui.go_to_setTest.clicked.connect(self.opensetTest)
        self.ui.begin_edit.clicked.connect(self.beginEdit)
        self.ui.back_to_changeSubject.clicked.connect(self.backtoSubjectEdit)
        self.ui.next_button_edit.clicked.connect(self.nextquestionEdit)
        self.ui.prev_button_edit.clicked.connect(self.prevquestionEdit)
        self.ui.end_edit.clicked.connect(self.end_edit_test)
        self.ui.return_from_finish_edit.clicked.connect(self.returnFromEdit)
        self.ui.gotodelete.clicked.connect(self.gotoDelete)
        self.ui.nextDelete.clicked.connect(self.nextDelete)
        self.ui.Back_delete.clicked.connect(self.backDelete)
        self.ui.gotoMainfromdelete.clicked.connect(self.gomainFromDelete)
        self.ui.buttonDelete.clicked.connect(self.delete)
        self.ui.openresultStudent.clicked.connect(self.openRaiting)
        self.ui.viewRaiting.clicked.connect(self.raiting)
        self.ui.backfromRaiting.clicked.connect(self.backraiting)

    def open_create_test(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.setNamesubject()
        self.setNamegroup()

    def setNamegroup(self):
        mylist = set_ngroup(self)
        for i in range(len(mylist)):
            self.ui.set_namegroup.addItem(mylist[i])

    def setNamesubject(self):
        mylist2 = set_subject(self)
        for i in range(len(mylist2)):
            self.ui.set_subject.addItem(mylist2[i])

    def setDeletesubject(self):
        mylist2 = set_subject(self)
        for i in range(len(mylist2)):
            self.ui.deleteSubject.addItem(mylist2[i])

    def next_create_test(self):
        self.nameTest = self.ui.name_testCreate.text()
        self.passwordTest = self.ui.password_test.text()
        self.countQuestions = self.ui.count_question.value()
        self.subjectName = self.ui.set_subject.currentText()
        self.groupName = self.ui.set_namegroup.currentText()
        if self.nameTest == "" or self.passwordTest == "":
            showDialog_end_create_test(self)
        else:
            check_origin_name_test(self)
            self.check_countquestion()

    def check_countquestion(self):
        if self.countQuestions == 0:
            showDialog_count(self)
        else:
            self.check_nametest()

    def check_nametest(self):
        if self.origin != ():
            showDialog_name_test(self)
        else:
            self.ui.end_create.setDisabled(True)
            self.ui.stackedWidget.setCurrentIndex(1)
            for i in range(self.countQuestions):
                self.massQuestion.append("")
                self.massAnswer1.append("")
                self.massAnswer2.append("")
                self.massAnswer3.append("")
                self.massAnswer4.append("")
                self.massTrueAnswer1.append("")
                self.massTrueAnswer2.append("")
                self.massTrueAnswer3.append("")
                self.massTrueAnswer4.append("")
                self.answerNumber.append(i + 1)
            self.ui.prev_page_create.setDisabled(True)
            self.ui.label_3.setText(" Введите " + str(self.answerNumber[0]) + " вопрос")
            if self.countQuestions == 1:
                self.ui.prev_page_create.setDisabled(True)
                self.ui.next_page_create.setDisabled(True)
                self.ui.end_create.setDisabled(False)

    def setAnswertext(self):
        self.massAnswer1[self.index] = self.ui.answer1.text()
        self.massAnswer2[self.index] = self.ui.answer2.text()
        self.massAnswer3[self.index] = self.ui.answer3.text()
        self.massAnswer4[self.index] = self.ui.answer4.text()

    def setTrueanswerText(self):
        self.massTrueAnswer1[self.index] = self.ui.is_answer_true1.currentText()
        self.massTrueAnswer2[self.index] = self.ui.is_answer_true2.currentText()
        self.massTrueAnswer3[self.index] = self.ui.is_answer_true3.currentText()
        self.massTrueAnswer4[self.index] = self.ui.is_answer_true4.currentText()


    def setTextanswer(self):
        self.ui.answer1.setText(self.massAnswer1[self.index])
        self.ui.answer2.setText(self.massAnswer2[self.index])
        self.ui.answer3.setText(self.massAnswer3[self.index])
        self.ui.answer4.setText(self.massAnswer4[self.index])

    def trueAnswertext(self):
        if self.massTrueAnswer1[self.index] == "Нет":
            self.ui.is_answer_true1.setCurrentIndex(0)
        elif self.massTrueAnswer1[self.index] == "":
            self.ui.is_answer_true1.setCurrentIndex(0)
        elif self.massTrueAnswer1[self.index] == "Да":
            self.ui.is_answer_true1.setCurrentIndex(1)

        if self.massTrueAnswer2[self.index] == "Нет":
            self.ui.is_answer_true2.setCurrentIndex(0)
        elif self.massTrueAnswer2[self.index] == "":
            self.ui.is_answer_true2.setCurrentIndex(0)
        elif self.massTrueAnswer2[self.index] == "Да":
            self.ui.is_answer_true2.setCurrentIndex(1)

        if self.massTrueAnswer3[self.index] == "Нет":
            self.ui.is_answer_true3.setCurrentIndex(0)
        elif self.massTrueAnswer3[self.index] == "":
            self.ui.is_answer_true3.setCurrentIndex(0)
        elif self.massTrueAnswer3[self.index] == "Да":
            self.ui.is_answer_true3.setCurrentIndex(1)

        if self.massTrueAnswer4[self.index] == "Нет":
            self.ui.is_answer_true4.setCurrentIndex(0)
        elif self.massTrueAnswer4[self.index] == "":
            self.ui.is_answer_true4.setCurrentIndex(0)
        elif self.massTrueAnswer4[self.index] == "Да":
            self.ui.is_answer_true4.setCurrentIndex(1)

    def nextCreate(self):
        self.ui.end_create.setDisabled(False)
        if self.index < self.countQuestions - 1:
            self.massQuestion[self.index] = self.ui.question.text()
            self.setAnswertext()
            self.setTrueanswerText()
            self.index += 1
            self.ui.question.setText(self.massQuestion[self.index])
            self.setTextanswer()
            self.trueAnswertext()
            self.ui.prev_page_create.setDisabled(False)
            self.value += 1
            self.ui.label_3.setText("Введите " + str(self.answerNumber[self.value]) + " вопрос")
            if self.value == self.countQuestions - 1:
                self.ui.next_page_create.setDisabled(True)

    def prevCreate(self):
        self.ui.next_page_create.setDisabled(False)
        if self.index != 0:
            self.massQuestion[self.index] = self.ui.question.text()
            self.setAnswertext()
            self.setTrueanswerText()
            self.index -= 1
            self.ui.question.setText(self.massQuestion[self.index])
            self.setTextanswer()
            self.trueAnswertext()
            self.value -= 1
            self.ui.label_3.setText("Введите " + str(self.answerNumber[self.value]) + " вопрос")
            if self.value == 0:
                self.ui.prev_page_create.setDisabled(True)

    def open_edit_test(self):
        mylist2 = set_subject(self)
        for i in range(len(mylist2)):
            self.ui.comboBox_change_subject_toEdit.addItem(mylist2[i])
        self.ui.stackedWidget.setCurrentIndex(2)

    def center(self):
        window_resize = self.frameGeometry()
        position = QDesktopWidget().availableGeometry().center()
        window_resize.moveCenter(position)
        self.move(window_resize.topLeft())

    def education(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        w.resize(1300, 770)
        w.center()

    def next_education(self):
        self.ui.stackedWidget_3.setCurrentIndex((self.ui.stackedWidget_3.currentIndex() + 1) % 4)

    def prev_education(self):
        self.ui.stackedWidget_3.setCurrentIndex((self.ui.stackedWidget_3.currentIndex() - 1) % 4)

    def main_menu(self):
        w.resize(1160, 680)
        self.ui.stackedWidget.setCurrentIndex(8)
        clearall(self)
        self.ui.comboBox_change_subject_toEdit.clear()
        self.ui.set_subject.clear()
        self.ui.set_namegroup.clear()

    def end(self):
        self.massQuestion[self.value] = self.ui.question.text()
        self.massAnswer1[self.value] = self.ui.answer1.text()
        self.massAnswer2[self.value] = self.ui.answer2.text()
        self.massAnswer3[self.value] = self.ui.answer3.text()
        self.massAnswer4[self.value] = self.ui.answer4.text()
        self.massTrueAnswer1[self.value] = self.ui.is_answer_true1.currentText()
        self.massTrueAnswer2[self.value] = self.ui.is_answer_true2.currentText()
        self.massTrueAnswer3[self.value] = self.ui.is_answer_true3.currentText()
        self.massTrueAnswer4[self.value] = self.ui.is_answer_true4.currentText()

        check_full_question(self)

    def opensetTest(self):
        self.setSubject = self.ui.comboBox_change_subject_toEdit.currentText()
        mylist2 = set_ntest(self)
        for i in range(len(mylist2)):
            self.ui.comboBox_change_subject_toEdit_2.addItem(mylist2[i])
        if self.ntestEdit2 != ():
            self.ui.stackedWidget.setCurrentIndex(3)
        else:
            showDialog_notest(self)

    def beginEdit(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.subjectEdit = self.ui.comboBox_change_subject_toEdit_2.currentText()
        self.setQuestionEdit()
        self.setAnswerEdit()
        self.setFirstEdit()
        self.setTrueAnswerEdit()
        self.outTrueAnswer()
        self.setTrueAnswer()
        self.setPasswordEdit()
        self.ui.prev_button_edit.setDisabled(True)

    def setPasswordEdit(self):
        editpassword = setEdit4(self)
        self.editPassword = []
        for i in range(len(editpassword)):
            self.editPassword.append(editpassword[i])
        self.ui.editPassowrd.setText(self.editPassword[0])

    def setQuestionEdit(self):
        editQuestion = setEdit(self)
        self.editQuestion = []
        for i in range(len(editQuestion)):
            self.editQuestion.append(editQuestion[i])

    def setFirstEdit(self):
        self.ui.edit_question.setText(self.editQuestion[self.count])
        self.ui.edit_answer1.setText(self.massEditAnswer[self.count][0])
        self.ui.edit_answer2.setText(self.massEditAnswer[self.count][1])
        self.ui.edit_answer3.setText(self.massEditAnswer[self.count][2])
        self.ui.edit_answer4.setText(self.massEditAnswer[self.count][3])

    def func_chunk(self, lst, n):
        for x in range(0, len(lst), n):
            e_c = lst[x: n + x]

            if len(e_c) < n:
                e_c = e_c + [None for y in range(n - len(e_c))]
            yield e_c

    def setAnswerEdit(self):
        setAnswer = setEdit2(self)
        self.editAnswer = []
        self.massEditAnswer = []
        for i in range(len(setAnswer)):
            self.editAnswer.append(setAnswer[i])
        self.massEditAnswer = list(self.func_chunk(self.editAnswer, 4))

    def setTrueAnswerEdit(self):
        setTrueAnswer = setEdit3(self)
        self.trueanser = []
        self.massAnswerTrue = []
        for i in range(len(setTrueAnswer)):
            self.trueanser.append(setTrueAnswer[i])
        self.massAnswerTrue = list(self.func_chunk(self.trueanser, 4))

    def outAnsweer(self):
        self.ui.edit_answer1.setText(self.massEditAnswer[self.count][0])
        self.ui.edit_answer2.setText(self.massEditAnswer[self.count][1])
        self.ui.edit_answer3.setText(self.massEditAnswer[self.count][2])
        self.ui.edit_answer4.setText(self.massEditAnswer[self.count][3])

    def outTrueAnswer(self):
        self.ui.edit_true1.addItem("Нет")
        self.ui.edit_true1.addItem("Да")
        self.ui.edit_true2.addItem("Нет")
        self.ui.edit_true2.addItem("Да")
        self.ui.edit_true3.addItem("Нет")
        self.ui.edit_true3.addItem("Да")
        self.ui.edit_true4.addItem("Нет")
        self.ui.edit_true4.addItem("Да")

    def setTrueAnswer(self):
        if self.massAnswerTrue[self.count][0] == "Нет":
            self.ui.edit_true1.setCurrentIndex(0)
        elif self.massAnswerTrue[self.count][0] == "Да":
            self.ui.edit_true1.setCurrentIndex(1)
        if self.massAnswerTrue[self.count][1] == "Нет":
            self.ui.edit_true2.setCurrentIndex(0)
        elif self.massAnswerTrue[self.count][1] == "Да":
            self.ui.edit_true2.setCurrentIndex(1)
        if self.massAnswerTrue[self.count][2] == "Нет":
            self.ui.edit_true3.setCurrentIndex(0)
        elif self.massAnswerTrue[self.count][2] == "Да":
            self.ui.edit_true3.setCurrentIndex(1)
        if self.massAnswerTrue[self.count][3] == "Нет":
            self.ui.edit_true4.setCurrentIndex(0)
        elif self.massAnswerTrue[self.count][3] == "Да":
            self.ui.edit_true4.setCurrentIndex(1)

    def chengedTrue(self):
        self.massAnswerTrue[self.count][0] = self.ui.edit_true1.currentText()
        self.massAnswerTrue[self.count][1] = self.ui.edit_true2.currentText()
        self.massAnswerTrue[self.count][2] = self.ui.edit_true3.currentText()
        self.massAnswerTrue[self.count][3] = self.ui.edit_true4.currentText()

    def setEditAnswer(self):
        self.massEditAnswer[self.count][0] = self.ui.edit_answer1.text()
        self.massEditAnswer[self.count][1] = self.ui.edit_answer2.text()
        self.massEditAnswer[self.count][2] = self.ui.edit_answer3.text()
        self.massEditAnswer[self.count][3] = self.ui.edit_answer4.text()

    def setchangedQuestion(self):
        self.editQuestion[self.count] = self.ui.edit_question.text()

    def nextquestionEdit(self):
        print(self.count)
        print("ok")
        if self.count < len(self.editQuestion) - 1:
            self.setchangedQuestion()
            self.setEditAnswer()
            self.chengedTrue()
            self.count += 1
            self.ui.edit_question.setText(self.editQuestion[self.count])
            self.outAnsweer()
            self.setTrueAnswer()
            self.ui.prev_button_edit.setDisabled(False)
            if self.count == len(self.editQuestion) - 1:
                self.ui.next_button_edit.setDisabled(True)

    def prevquestionEdit(self):
        if self.count != 0:
            self.setchangedQuestion()
            self.setEditAnswer()
            self.chengedTrue()
            self.count -= 1
            self.ui.edit_question.setText(self.editQuestion[self.count])
            self.outAnsweer()
            self.setTrueAnswer()
            self.ui.next_button_edit.setDisabled(False)
            if self.count == 0:
                self.ui.prev_button_edit.setDisabled(True)

    def backtoSubjectEdit(self):
        self.ui.comboBox_change_subject_toEdit_2.clear()
        self.ui.stackedWidget.setCurrentIndex(2)

    def end_edit_test(self):
        self.editQuestion[self.count] = self.ui.edit_question.text()
        self.massEditAnswer[self.count][0] = self.ui.edit_answer1.text()
        self.massEditAnswer[self.count][1] = self.ui.edit_answer2.text()
        self.massEditAnswer[self.count][2] = self.ui.edit_answer3.text()
        self.massEditAnswer[self.count][3] = self.ui.edit_answer4.text()
        self.massAnswerTrue[self.count][0] = self.ui.edit_true1.currentText()
        self.massAnswerTrue[self.count][1] = self.ui.edit_true2.currentText()
        self.massAnswerTrue[self.count][2] = self.ui.edit_true3.currentText()
        self.massAnswerTrue[self.count][3] = self.ui.edit_true4.currentText()
        self.editPassword[0] = self.ui.editPassowrd.text()

        check_Edit_question(self)

    def returnFromEdit(self):
        self.ui.stackedWidget.setCurrentIndex(8)
        clearEdit(self)

    def gotoDelete(self):
        self.ui.stackedWidget.setCurrentIndex(7)
        mylist2 = set_subject(self)
        for i in range(len(mylist2)):
            self.ui.deleteSubject.addItem(mylist2[i])

    def nextDelete(self):
        self.deleteSubject = self.ui.deleteSubject.currentText()
        mylist3 = set_ntest2(self)
        for i in range(len(mylist3)):
            self.ui.deleteTest.addItem(mylist3[i])
        if self.ntestEdit3 != ():
            self.ui.stackedWidget.setCurrentIndex(6)
        else:
            showDialog_notest(self)

    def backDelete(self):
        self.ui.deleteTest.clear()
        self.ui.stackedWidget.setCurrentIndex(7)

    def gomainFromDelete(self):
        self.ui.deleteSubject.clear()
        self.ui.stackedWidget.setCurrentIndex(8)

    def delete(self):
        self.deletetest = self.ui.deleteTest.currentText()
        deleteInfo(self)
        showDialog_exelent3(self)
        self.ui.deleteSubject.clear()
        self.ui.deleteTest.clear()
        self.ui.stackedWidget.setCurrentIndex(8)

    def openRaiting(self):
        self.ui.stackedWidget.setCurrentIndex(9)
        mylist = set_ngroup(self)
        for i in range(len(mylist)):
            self.ui.group_raiting.addItem(mylist[i])

    def raiting(self):

        self.raitingcheck()

    def raitingcheck(self):
        self.nameRaiting = self.ui.name_raiting.text().upper()
        self.secondNameRaiting = self.ui.secondName_raiting.text().upper()
        self.idgroupraiting = self.ui.group_raiting.currentText().upper()
        if self.nameRaiting == '' or self.secondNameRaiting == '':
            showDialog_end_create_test(self)
        else:
            self.check()

    def check(self):
        checkOriginName(self)
        if self.idstudentrt != ():
            self.setview()
        else:
            self.ui.tableWidget.setRowCount(0)
            showDialog_errorStudent(self)

    def setview(self):
        checkOriginName1(self)
        if self.idres != ():
            self.ui.tableWidget.setRowCount(0)
            infoStraiting(self)
            self.row = len(self.raiting)
            self.ui.tableWidget.setRowCount(self.row)
            for i in range(self.row):
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(self.nameRaiting))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(self.secondNameRaiting))
                self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(self.idgroupraiting))
                self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(str(self.resultnamesubject[i])))
                self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(self.resultnametest[i])))
                self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(str(self.raiting[i])))
        else:
            showDialog_errorStudent1(self)

    def backraiting(self):
        self.ui.stackedWidget.setCurrentIndex(8)
        self.ui.name_raiting.clear()
        self.ui.secondName_raiting.clear()
        self.ui.tableWidget.setRowCount(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    style = """
        QWidget {
            background: #19a1a1;
        }
        
        QPushButton {
            font-family: Comic Sans MS;
            font-size:18px;
            border-radius: 10px;
            padding: 5 20 5 20;
            background: #fc0;
            box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
        }
        QPushButton:hover {
            border: 2px solid #8f8f91;
            padding: 5 0 5 0;
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0, stop: 0 #f6f7fa, stop: 1 #dadbde);
        }
        
        QLabel {
            font-family: Times New Roman;
            font-size: 21px;
            background: rgba(255, 255, 255, 0.8);
            border-radius:5px;
            padding: 0 10 0 10;
        }
        QLabel#main_lb, QLabel#change_test_toEdit_lb, QLabel#education_lb {
            border-radius: 20px;
            font-size: 36px;
        }
        
         QLabel#createTest_lb {
            font-size: 36px;
            border-radius: 10px;
         }
        
        QComboBox {
            font-family: Times New Roman;
            font-size: 20px;
            background: rgba(255, 255, 255, 0.8);
        }
        
        QLineEdit {
            border-radius: 5px;
            min-height: 30px;
            background: white;
            color: black;
            font-size:16px;
        }
        
        QComboBox QAbstractItemView {
            border: 1px solid grey;
            background: white;
            selection-background-color: light blue;
        }
        
        QComboBox:active {
            background:none;
        }
        
        QGroupBox::title {
            font-family: Times New Roman;
            color: white;
        }
        
        QSpinBox {
            border: 1px solid grey;
            background: white;
            selection-background-color: light blue;
        }
        
        QTableWidget {
            border: 0px;
            
        }
              QTableWidget:item {
            background:  rgb(225, 228, 232);
            border:0px;
            
        }


        """
    app.setStyleSheet(style)
    w.resize(1160, 680)
    w.setWindowIcon(QIcon("create.png"))
    w.center()
    w.show()
    sys.exit(app.exec_())
