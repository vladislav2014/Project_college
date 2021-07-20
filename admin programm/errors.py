import sys

from PyQt5.QtWidgets import QMessageBox


def showDialog(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Такой пользователь уже зарегестрирован!")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showInfo(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Заполните все поля!")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showInfouser(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Такого пользователя не существует!")
    msgBox.setWindowTitle("Ошибка ввода данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showSave(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Пользователь зарегестрирован!")
    msgBox.setWindowTitle("Успешное сохранение!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showDelete(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Пользователь успешно удален!")
    msgBox.setWindowTitle("Успешное удаление!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()

def showError(self):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Логин и пароль не сгенерированы!")
    msgBox.setWindowTitle("Ошибка данных!")
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.exec()