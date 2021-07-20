import sys

from PyQt5.QtWidgets import QMessageBox

def showDialog(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Проверьте введенные данные!")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showDialog2(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Тесты отсутствуют!")
    msgBox.setWindowTitle("Проверьте данные!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()


def authOk(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Успешная авторизация!")
    msgBox.setWindowTitle("Авторизация!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def setAnswer(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Выберите ответ!")
    msgBox.setWindowTitle("Выберите ответ!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def resultDialog(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Вы завершили тест!")
    msgBox.setWindowTitle("Окончание теста!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def badpassword(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Вы ввели неверный пароль!")
    msgBox.setWindowTitle("Неверный пароль!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()