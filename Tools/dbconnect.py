import pymysql


class DbConnect():

    # def __init__(self):
    #     pass

    def __connect(self, db):
        host = '127.0.0.1'
        conn = pymysql.connect(host=host, port=3306, user='root', db=db)
        return conn

    def selectQuery(self,db, query):
        """

        :param  db:
        :param query:
        :return:
        """
        conn = self.__connect(db)
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()

        all_rows = []
        for line in result:
            row = []
            for col in line:
                row.append(str(col))
            all_rows.append(row)

        conn.close()
        cur.close()

    def update(self, db, query):
        """
        :param db:
        :param query:
        :return:
        """
        conn = self.__connect(db)
        cur = conn.cursor()
        cur.execute(query)

        result = cur.execute(query)
        conn.commit()
        conn.close()
        cur.close()

        return result

