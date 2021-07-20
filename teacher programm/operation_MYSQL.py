from main import *


def insert_test(self):  # работа с таблицей "ВОПРОСЫ"
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO `вопросы` (вопрос, id_теста, id_вопроса) VALUES (%s,%s,%s)",
                               (self.question, self.rows, self.id_question))  # добавление вопросов в таблицу "вопросы"
                connection.commit()

        finally:
            connection.close()

    except Exception as ex:
        print(ex)


def check_origin_name_test(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT `id_предмета` FROM `название_предмета` WHERE `название_предмета` = (%s)",
                               self.subjectName)  # выборка id_предмета
                self.id_subject = cursor.fetchone()['id_предмета']
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("SELECT `название_теста` FROM `название тестов` WHERE `название_теста` = (%s) AND "
                               "`id_предмета` = (%s) and `id_group` = (%s)",
                               (self.nameTest, self.id_subject, self.groupName))  # выборка id_предмета
                self.origin = cursor.fetchall()

        finally:
            connection.close()
    except Exception as ex:
        print(ex)
    return 0


def set_ngroup(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT `name_group` FROM `name_group`")
                self.n_group = cursor.fetchall()
                mylist = []
                for i in self.n_group:
                    mylist.append(i['name_group'])
                connection.commit()
        finally:
            connection.close()
            return mylist
    except Exception as ex:
        print(ex)


def set_ntest(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT `id_предмета` FROM `название_предмета` where `название_предмета` = (%s)",
                               self.setSubject)
                self.idsubject = cursor.fetchone()['id_предмета']

            with connection.cursor() as cursor:
                cursor.execute("SELECT `название_теста` FROM `название тестов` where id_предмета = (%s)",
                               self.idsubject)
                self.ntestEdit = cursor.fetchall()
                mylist2 = []
                for i in self.ntestEdit:
                    mylist2.append(i['название_теста'])
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("SELECT `название_теста` FROM `название тестов` where id_предмета = (%s)",
                               self.idsubject)
                self.ntestEdit2 = cursor.fetchall()
                connection.commit()
        finally:
            connection.close()
            return mylist2
    except Exception as ex:
        print(ex)


def set_ntest2(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT `id_предмета` FROM `название_предмета` where `название_предмета` = (%s)",
                               self.deleteSubject)
                self.idsubject = cursor.fetchone()['id_предмета']

            with connection.cursor() as cursor:
                cursor.execute("SELECT `название_теста` FROM `название тестов` where id_предмета = (%s)",
                               self.idsubject)
                self.ntestEdit = cursor.fetchall()
                mylist3 = []
                for i in self.ntestEdit:
                    mylist3.append(i['название_теста'])
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("SELECT `название_теста` FROM `название тестов` where id_предмета = (%s)",
                               self.idsubject)
                self.ntestEdit3 = cursor.fetchall()
                connection.commit()
        finally:
            connection.close()
            return mylist3
    except Exception as ex:
        print(ex)


def set_subject(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT `название_предмета` FROM `название_предмета`")
                self.n_subject = cursor.fetchall()
                mylist2 = []
                for i in self.n_subject:
                    mylist2.append(i['название_предмета'])
                connection.commit()
        finally:
            connection.close()
            return mylist2
    except Exception as ex:
        print(ex)


def insert_test(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("select `id_предмета` from название_предмета where название_предмета = (%s)",
                               self.subjectName)
                self.idsubject = cursor.fetchone()['id_предмета']
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("select id_group from name_group where name_group = (%s)",
                               self.groupName)
                self.idgroup = cursor.fetchone()['id_group']
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute(
                    "insert into `название тестов` (название_теста, id_предмета, id_group) VAlUES (%s,%s,%s)",
                    (self.nameTest, self.idsubject, self.idgroup))
            with connection.cursor() as cursor:
                cursor.execute(" select `id_теста` from `название тестов` where `название_теста` = (%s)",
                               self.nameTest)
                self.idtest = cursor.fetchone()['id_теста']
            with connection.cursor() as cursor:
                cursor.execute("insert into `password_for_test` (password, id_теста) VAlUES (%s,%s)",
                               (self.passwordTest, self.idtest))
            for i in range(self.countQuestions):
                with connection.cursor() as cursor:
                    cursor.execute(
                        "insert into `вопросы` (id_вопроса, вопрос, id_теста) VAlUES (%s,%s,%s)",
                        (i + 1, self.massQuestion[i], self.idtest))
                connection.commit()
            q = 0
            for i in range(self.countQuestions):
                for k in range(4):
                    q += 1
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "insert into `ответы на вопросы` (id,ответ_на_вопрос, верность_ответа, id_вопроса,"
                            "id_теста) VAlUES (%s,%s,%s,%s,%s)",
                            (q, self.answerMass[i][k], self.mass[i][k], i + 1, self.idtest))
                    connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print(ex)


def setEdit(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_теста FROM `название тестов` where название_теста = (%s)",
                               self.subjectEdit)
                self.idEdit = cursor.fetchone()['id_теста']
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("SELECT `Вопрос` FROM `вопросы` where id_теста = (%s)",
                               self.idEdit)
                self.question = cursor.fetchall()
                mylistQuestion = []
                for i in self.question:
                    mylistQuestion.append(i['Вопрос'])
                connection.commit()
        finally:
            connection.close()
            return mylistQuestion
    except Exception as ex:
        print(ex)


def setEdit2(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT `id_теста` FROM `название тестов` where название_теста = (%s)",
                               self.subjectEdit)
                self.idEdit = cursor.fetchone()["id_теста"]
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("SELECT `ответ_на_вопрос` FROM `ответы на вопросы` where id_теста = (%s)",
                               self.idEdit)
                self.answer = cursor.fetchall()
                mylistAnswer = []
                for i in self.answer:
                    mylistAnswer.append(i['ответ_на_вопрос'])
                connection.commit()
        finally:
            connection.close()
            return mylistAnswer
    except Exception as ex:
        print(ex)


def setEdit3(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT `id_теста` FROM `название тестов` where название_теста = (%s)",
                               self.subjectEdit)
                self.idEdit = cursor.fetchone()["id_теста"]
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("SELECT `верность_ответа` FROM `ответы на вопросы` where id_теста = (%s)",
                               self.idEdit)
                self.trueanswer = cursor.fetchall()
                mylistAnswerTrue = []
                for i in self.trueanswer:
                    mylistAnswerTrue.append(i['верность_ответа'])
                connection.commit()
        finally:
            connection.close()
            return mylistAnswerTrue
    except Exception as ex:
        print(ex)


def setEdit4(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_теста FROM `название тестов` where название_теста = (%s)",
                               self.subjectEdit)
                self.idEdit = cursor.fetchone()['id_теста']
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("SELECT `password` FROM `password_for_test` where id_теста = (%s)",
                               self.idEdit)
                self.password = cursor.fetchall()
                mylistPassword = []
                for i in self.password:
                    mylistPassword.append(i['password'])
                connection.commit()
        finally:
            connection.close()
            return mylistPassword
    except Exception as ex:
        print(ex)


def updateTest(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE password_for_test set `password` = (%s) where id_теста = (%s)",
                               (self.editPassword[0], self.idEdit))
                connection.commit()
            for i in range(len(self.editQuestion)):
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE вопросы set `вопрос` = (%s) where id_теста = (%s) and id_вопроса = (%s)",
                                   (self.editQuestion[i], self.idEdit, i + 1))
                    connection.commit()
            for i in range(len(self.editQuestion)):
                q = 0
                for k in range(4):
                    q += 1
                    with connection.cursor() as cursor:
                        cursor.execute("UPDATE `ответы на вопросы` set `ответ_на_вопрос` = (%s) where id_теста = (%s) "
                                       "and id = (%s) and id_вопроса = (%s)",
                                       (self.massEditAnswer[i][k], self.idEdit, q, i+1))
                    connection.commit()
            for i in range(len(self.editQuestion)):
                w = 0
                for k in range(4):
                    w += 1
                    with connection.cursor() as cursor:
                        cursor.execute("UPDATE `ответы на вопросы` set `верность_ответа` = (%s) where id_теста = (%s) "
                                       "and id = (%s) and id_вопроса = (%s)",
                                       (self.massAnswerTrue[i][k], self.idEdit, w,  i+1))
                        connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print(ex)


def deleteInfo(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_теста FROM `название тестов` where название_теста = (%s)",
                               self.deletetest)
                self.idEdit = cursor.fetchone()['id_теста']
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM `ответы на вопросы` where id_теста = (%s)",
                               self.idEdit)
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("SELECT `password` FROM `password_for_test` where id_теста = (%s)",
                               self.idEdit)
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM `вопросы` where id_теста = (%s)",
                               self.idEdit)
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM `password_for_test` where id_теста = (%s)",
                               self.idEdit)
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM `result_student` where id_test = (%s)",
                               self.idEdit)
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM `название тестов` where id_теста = (%s)",
                               self.idEdit)
                connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print(ex)


def infoStraiting(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("select id_group from name_group where name_group = (%s)",
                               self.idgroupraiting)
                self.idgrp = cursor.fetchone()['id_group']
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("select id_student from info_student where name_student = (%s) and secondName_student "
                               "= (%s) and id_group = (%s)",
                               (self.nameRaiting, self.secondNameRaiting, self.idgrp))
                self.idStudent = cursor.fetchone()['id_student']
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute(
                    "select id_result from result_student where id_student = (%s)",
                    self.idStudent)
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
                        (self.idStudent, i + 1))
                    self.k = cursor.fetchall()
                    for k in self.k:
                        self.raiting.append(k['itog_student'])
                    connection.commit()

                with connection.cursor() as cursor:
                    cursor.execute("select id_test from result_student where id_student = (%s) and id_result = (%s)",
                                   (self.idStudent, i + 1))
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


def checkOriginName(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_group  FROM `name_group` where name_group = (%s) ",
                               self.idgroupraiting)
                self.idgrp = cursor.fetchone()['id_group']
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_student  FROM `info_student` where name_student = (%s) "
                               "and secondName_student = (%s) and id_group = (%s)",
                               (self.nameRaiting, self.secondNameRaiting, self.idgrp))
                self.idstudentrt = cursor.fetchall()
                connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print(ex)

def checkOriginName1(self):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            database=db_name,
            password=password,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_student  FROM `info_student` where name_student = (%s) "
                               "and secondName_student = (%s) and id_group = (%s)",
                               (self.nameRaiting, self.secondNameRaiting, self.idgrp))
                self.idstudentrt = cursor.fetchone()['id_student']
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_result  FROM `result_student` where id_student = (%s) ",

                               self.idstudentrt)
                self.idres = cursor.fetchall()
                connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print(ex)

