import pymysql

from connect_testBD import password_2
from main import *

import pymysql


def check_login(self):
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
                cursor.execute("SELECT id_group FROM info_student WHERE login_student = (%s) AND password_student = ("
                               "%s)", (self.login_student, self.password_student))
                self.id_group_check = cursor.fetchall()
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_group FROM info_student WHERE login_student = (%s) AND password_student = ("
                               "%s)", (self.login_student, self.password_student))
                self.id_group_check2 = cursor.fetchone()['id_group']
                connection.commit()
        finally:
            connection.close()

    except Exception as ex:
        print(ex)


def take_infoStudent(self):
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
                cursor.execute("select id_student from info_student where login_student = (%s) and password_student "
                               "= (%s) and id_group = (%s)",
                               (self.login_student, self.password_student, self.id_group_check2))
                self.studentId = cursor.fetchone()['id_student']
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("SELECT name_student FROM info_student WHERE login_student = (%s) AND password_student "
                               "= ( "
                               "%s)", (self.login_student, self.password_student))
                self.tns = cursor.fetchone()['name_student']
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("SELECT secondName_student FROM info_student WHERE login_student = (%s) AND "
                               "password_student "
                               "= ( "
                               "%s)", (self.login_student, self.password_student))
                self.tsns = cursor.fetchone()['secondName_student']
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_group FROM info_student WHERE login_student = (%s) AND "
                               "password_student "
                               "= ( "
                               "%s)", (self.login_student, self.password_student))
                self.idgroupStudent = cursor.fetchone()['id_group']
                connection.commit()

        finally:
            connection.close()

    except Exception as ex:
        print(ex)


def change_subject(self):
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
                cursor.execute("SELECT `название_предмета` FROM `название_предмета` ")
                self.n_subject = cursor.fetchall()
                mylist = []
                for i in self.n_subject:
                    mylist.append(i['название_предмета'])
                connection.commit()
        finally:
            connection.close()
            return mylist
    except Exception as ex:
        print(ex)


def set_nameTest(self):
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
                cursor.execute("SELECT id_предмета FROM `название_предмета` WHERE `название_предмета` = (%s) ",
                               self.name_subject)
                self.set_idSubject = cursor.fetchone()["id_предмета"]
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT `название_теста` FROM `название тестов` WHERE `id_предмета` = (%s) and id_group = (%s)",
                    (self.set_idSubject, self.idgroupStudent))
                self.n_test = cursor.fetchall()
                name_test = []
                for i in self.n_test:
                    name_test.append(i['название_теста'])
                connection.commit()
        finally:
            connection.close()
            return name_test
    except Exception as ex:
        print(ex)


def insert_result(self):
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
                cursor.execute("INSERT INTO `result_student` (id_student, "
                               "id_test, itog_student) values (%s,%s,%s)",
                               (self.studentId, self.idtest,  self.raiting
                                ))
                connection.commit()

        finally:
            connection.close()

    except Exception as ex:
        print(ex)


def check_result(self):
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
                cursor.execute(
                    "select id_result from result_student where id_student = (%s)",
                    self.studentId)
                self.resultId = cursor.fetchall()
                self.result = []
                for i in self.resultId:
                    self.result.append(i['id_result'])
                connection.commit()
            self.resultnamesubject = []
            self.resultnametest = []
            self.raiting = []
            self.idtest = []
            self.idsubject = []
            for i in range(len(self.result)):
                with connection.cursor() as cursor:
                    cursor.execute(
                        "select itog_student from result_student where id_student = (%s) and id_result = (%s)",
                        (self.studentId, i+1))
                    self.k = cursor.fetchall()
                    for k in self.k:
                        self.raiting.append(k['itog_student'])
                    connection.commit()

                with connection.cursor() as cursor:
                    cursor.execute("select id_test from result_student where id_student = (%s) and id_result = (%s)",
                                   (self.studentId, i + 1))
                    self.k = cursor.fetchall()
                    for k in self.k:
                        self.idtest.append(k['id_test'])
                    connection.commit()

                with connection.cursor() as cursor:
                    cursor.execute("select id_предмета from `название тестов` where id_теста = (%s)",
                                   self.idtest[i])
                    self.k = cursor.fetchall()
                    for k in self.k:
                        self.idsubject.append(k['id_предмета'])
                    connection.commit()

                for k in range(len(self.raiting)):
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "select название_предмета from название_предмета where id_предмета = (%s)",
                            self.idsubject[k])
                        self.k = cursor.fetchall()
                        for j in self.k:
                            self.resultnamesubject.append(j['название_предмета'])
                        connection.commit()
                for k in range(len(self.raiting)):
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "select `название_теста` from `название тестов` where id_теста = (%s)",
                            self.idtest[i])
                        self.k = cursor.fetchall()
                        for j in self.k:
                            self.resultnametest.append(j['название_теста'])
                        connection.commit()
        finally:
            connection.close()

    except Exception as ex:
        print(ex)


def set_password(self):
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
                cursor.execute("select `id_теста` from `название тестов` where id_предмета = (%s)",
                               self.set_idSubject)
                self.setidTest = cursor.fetchone()['id_теста']
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("SELECT `password` FROM `password_for_test` where id_теста = (%s)", self.setidTest)
                self.setpassword = cursor.fetchone()['password']
                connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print(ex)


