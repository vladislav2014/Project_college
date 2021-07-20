import sys

from PyQt5.QtWidgets import QMessageBox


def showDialog(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Проверьте поля 'Ответ верен?'.\nПравильный ответ может быть только ОДИН ")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()


def showDialog_name_test(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Тест с таким название уже существует! ")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()


def showDialog_name_test_2(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Введите название теста! ")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()


def showDialog_fill_quest(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Количество вопросов не совпадает с заданным значением!\nПроверьте введенные данные")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()


def showDialog_fill_answer(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Заполните все ответы на вопросы!\nПроверьте введенные данные ")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()


def showDialog_end_create_test(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Проверьте введенность всех данных'! ")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showDialog_count(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Количество вопросов не может быть равно 0'! ")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showDialog_trueAnswer(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Правильный ответ может быть только 1!\nПроверьте введенные данные ")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showDialog_exelent(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Тест успешно создан! ")
    msgBox.setWindowTitle("Успешное создание!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showDialog_exelent2(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Тест успешно изменен! ")
    msgBox.setWindowTitle("Успешное изменение!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showDialog_exelent3(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Тест успешно удален! ")
    msgBox.setWindowTitle("Успешное удаление!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showDialog_notest(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Тестов не существует!\nПроверьте введенные данные ")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showDialog_passwordEdit(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Заполните поле пароль!")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showDialog_errorStudent(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Такого пользователя не существует!")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showDialog_errorStudent1(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Пользователь не прошел ни одного теста!")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()