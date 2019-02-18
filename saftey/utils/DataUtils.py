from django.db import connection


class MySQLUtils(object):
    def __init__(self):
        self.cursor = connection.cursor()

    def get_dict_data(self, sql):
        self.cursor.execute(sql)
        raw_data = self.cursor.fetchall()
        col_names = [desc[0] for desc in self.cursor.description]
        result = []
        for row in raw_data:
            obj = dict(zip(col_names, row))
            result.append(obj)
        return result

    def get_list_data(self, sql):
        self.cursor.execute(sql)
        raw_data = self.cursor.fetchall()
        return raw_data

    def __no_query(self, sql):
        raw = self.cursor.execute(sql)

    def delet_date(self, sql):
        return self.__no_query(sql)

    def insert_date(self, sql):
        return self.__no_query(sql)

    def update_date(self, sql):
        return self.__no_query(sql)
