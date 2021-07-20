from main import *


def generate_login(self):
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
                cursor.execute("SELECT id_group FROM name_group WHERE name_group = (%s)",
                               self.set_name_group)
                self.id_group = cursor.fetchone()["id_group"]
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("SELECT name_group FROM name_group WHERE id_group = (%s)", self.id_group)
                self.name_group = cursor.fetchone()['name_group']
                connection.commit()
        finally:
            connection.close()

    except Exception as ex:
        print(ex)


def check_origin_login(self):
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
                cursor.execute("SELECT login_student FROM info_student WHERE login_student = (%s)", self.result_login)
                self.origin_login = cursor.fetchall()
                connection.commit()
        finally:
            connection.close()

    except Exception as ex:
        print(ex)


def check_origin_password(self):
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
                cursor.execute("SELECT password_student FROM info_student WHERE password_student = (%s)",
                               self.password_student)
                self.origin_password = cursor.fetchall()
                connection.commit()
        finally:
            connection.close()

    except Exception as ex:
        print(ex)


def check_origin_name_and_secondName(self):
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
                cursor.execute("SELECT id_group FROM name_group WHERE name_group = (%s)",
                               self.set_name_group)
                self.id_group = cursor.fetchone()["id_group"]
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("SELECT `name_student`,`secondName_student` FROM info_student WHERE id_group = (%s) "
                               "AND `name_student` = (%s) AND `secondName_student` = (%s)",
                               (self.id_group, self.origin_name, self.origin_secondName))
                self.origin_student = cursor.fetchall()
                connection.commit()

        finally:
            connection.close()

    except Exception as ex:
        print(ex)


def insert_login_password(self):
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
                cursor.execute("SELECT id_group FROM name_group WHERE name_group = (%s)",
                               self.set_name_group)
                self.id_group = cursor.fetchone()["id_group"]
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO info_student (name_student, secondName_student, login_student, "
                               "password_student, id_group) VALUES (%s,%s,%s,%s,%s)",
                               (self.name_edit, self.secondName, self.itog_login, self.itog_password,
                                self.id_group))
                connection.commit()
        finally:
            connection.close()

    except Exception as ex:
        print(ex)


def change_group(self):
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
                cursor.execute("SELECT name_group FROM name_group ")
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


def remind_login_password_sql(self):
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
                cursor.execute("SELECT id_group FROM name_group WHERE name_group = (%s)",
                               self.remind_nameGroup)
                self.id_group = cursor.fetchone()["id_group"]
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("SELECT `login_student`, `password_student` FROM info_student WHERE name_student = ("
                               "%s) AND secondName_student = (%s) AND id_group = (%s)", (self.remind_name,
                                                                                         self.remind_secondName,
                                                                                         self.id_group))
                self.allInfo = cursor.fetchall()
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("SELECT `login_student` FROM info_student WHERE name_student = ("
                               "%s) AND secondName_student = (%s) AND id_group = (%s)", (self.remind_name,
                                                                                         self.remind_secondName,
                                                                                         self.id_group))
                self.rlogin = cursor.fetchone()["login_student"]
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("SELECT `password_student` FROM info_student WHERE name_student = ("
                               "%s) AND secondName_student = (%s) AND id_group = (%s)", (self.remind_name,
                                                                                         self.remind_secondName,
                                                                                         self.id_group))
                self.rpassword = cursor.fetchone()["password_student"]
                connection.commit()

        finally:
            connection.close()
    except Exception as ex:
        print(ex)

def check_deleteUser(self):
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
                cursor.execute("SELECT id_group FROM name_group WHERE name_group = (%s)",
                               self.deleteGroup)
                self.id_group = cursor.fetchone()["id_group"]
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("SELECT `login_student`, `password_student` FROM info_student WHERE name_student = ("
                               "%s) AND secondName_student = (%s) AND id_group = (%s)", (self.name_delete,
                                                                                         self.secondName_delete,
                                                                                         self.id_group))
                self.allInfo = cursor.fetchall()
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("SELECT `login_student` FROM info_student WHERE name_student = ("
                               "%s) AND secondName_student = (%s) AND id_group = (%s)", (self.name_delete,
                                                                                         self.secondName_delete,
                                                                                         self.id_group))
                self.dlogin = cursor.fetchone()["login_student"]
                connection.commit()
            with connection.cursor() as cursor:
                cursor.execute("SELECT `password_student` FROM info_student WHERE name_student = ("
                               "%s) AND secondName_student = (%s) AND id_group = (%s)", (self.name_delete,
                                                                                         self.secondName_delete,
                                                                                         self.id_group))
                self.dpassword = cursor.fetchone()["password_student"]
                connection.commit()

        finally:
            connection.close()
    except Exception as ex:
        print(ex)


def deleteUser(self):
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
                cursor.execute("SELECT id_group FROM name_group WHERE name_group = (%s)",
                               self.deleteGroup)
                self.id_group = cursor.fetchone()["id_group"]
                connection.commit()

            with connection.cursor() as cursor:
                cursor.execute("delete from info_student where id_group = (%s) and name_student = (%s) and "
                               "secondName_student = (%s)",
                               (self.id_group, self.name_delete, self.secondName_delete))
                connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print(ex)