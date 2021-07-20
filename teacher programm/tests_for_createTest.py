import sys

from messageBox import *
from main import *
from operation_MYSQL import *


def check_full_question(self):
    counter = 0
    for i in range(self.countQuestions):
        if self.massQuestion[i] != '':
            counter += 1
    if counter != self.countQuestions:
        showDialog_fill_quest(self)
    else:
        check_full_answer(self)


def check_full_answer(self):
    counter = 0
    for i in range(self.countQuestions):
        if self.massAnswer1[i] != '':
            counter += 1
        if self.massAnswer2[i] != '':
            counter += 1
        if self.massAnswer3[i] != '':
            counter += 1
        if self.massAnswer4[i] != '':
            counter += 1
    if counter != self.countQuestions * 4:
        showDialog_fill_answer(self)
    else:
        check_trueAnswer(self)


def check_trueAnswer(self):
    self.answerMass = []
    newmass2 = []
    newmass = []
    counter = 0
    itog = 0
    self.mass = []
    newmass2.append(self.massAnswer1)
    newmass2.append(self.massAnswer2)
    newmass2.append(self.massAnswer3)
    newmass2.append(self.massAnswer4)
    newmass.append(self.massTrueAnswer1)
    newmass.append(self.massTrueAnswer2)
    newmass.append(self.massTrueAnswer3)
    newmass.append(self.massTrueAnswer4)
    for i in range(self.countQuestions):
        a = []
        b = []
        for k in range(4):
            a.append(newmass[k][i])
            b.append(newmass2[k][i])
        self.answerMass.append(b)
        self.mass.append(a)
    for i in range(self.countQuestions):
        counter = 0
        for k in range(4):
            if self.mass[i][k] == "Да":
                counter += 1
        if counter != 1:
            itog += 0
        else:
            itog += 1
    if itog == self.countQuestions:
        operation_MYSQL.insert_test(self)
        showDialog_exelent(self)
        self.ui.stackedWidget.setCurrentIndex(8)
        clearall(self)

    else:
        showDialog_trueAnswer(self)


def clearall(self):
    self.value = 0
    self.counter_value = self.value
    self.index = 0
    self.counter = 0
    self.count = 0
    self.ui.question.clear()
    self.ui.answer1.clear()
    self.ui.answer2.clear()
    self.ui.answer3.clear()
    self.ui.answer4.clear()
    self.ui.name_testCreate.clear()
    self.ui.password_test.clear()
    self.ui.count_question.setValue(0)
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
    self.ui.is_answer_true1.setCurrentIndex(0)
    self.ui.is_answer_true2.setCurrentIndex(0)
    self.ui.is_answer_true3.setCurrentIndex(0)
    self.ui.is_answer_true4.setCurrentIndex(0)
    self.ui.next_page_create.setDisabled(False)


# -----------------------------------------

def check_Edit_question(self):
    counter = 0
    for i in range(len(self.editQuestion)):
        if self.editQuestion[i] != '':
            counter += 1
    if counter != len(self.editQuestion):
        showDialog_fill_quest(self)
    else:
        check_Edit_answer(self)


def check_Edit_answer(self):
    counter = 0
    for i in range(len(self.editQuestion)):
        if self.massEditAnswer[i][0] != '':
            counter += 1
        if self.massEditAnswer[i][1] != '':
            counter += 1
        if self.massEditAnswer[i][2] != '':
            counter += 1
        if self.massEditAnswer[i][3] != '':
            counter += 1
    if counter != len(self.editQuestion) * 4:
        showDialog_fill_answer(self)
    else:
        check_password(self)

def check_password(self):
    if self.editPassword[0] != '':
        check_Edit_trueAnswer(self)
    else:
        showDialog_passwordEdit(self)


def check_Edit_trueAnswer(self):
    itog = 0
    for i in range(len(self.editQuestion)):
        counter = 0
        for k in range(4):
            if self.massAnswerTrue[i][k] == "Да":
                counter += 1
        if counter != 1:
            itog += 0
        else:
            itog += 1
    if itog == len(self.editQuestion):
        showDialog_exelent2(self)
        operation_MYSQL.updateTest(self)
        self.ui.stackedWidget.setCurrentIndex(8)
        clearEdit(self)
    else:
        showDialog_trueAnswer(self)

def clearEdit(self):
    self.ui.comboBox_change_subject_toEdit.setCurrentIndex(0)
    self.ui.comboBox_change_subject_toEdit.clear()
    self.ui.comboBox_change_subject_toEdit_2.clear()
    self.editQuestion.clear()
    self.massEditAnswer.clear()
    self.massAnswerTrue.clear()
    self.editQuestion = []
    self.value = 0
    self.counter_value = self.value
    self.index = 0
    self.counter = 0
    self.count = 0
    self.massEditAnswer = []
    self.trueanser = []
    self.massAnswerTrue = []
    self.editPassword = []
    self.ui.edit_true1.clear()
    self.ui.edit_true2.clear()
    self.ui.edit_true3.clear()
    self.ui.edit_true4.clear()
    self.ui.next_button_edit.setDisabled(False)
