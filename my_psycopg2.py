import psycopg2

class PgSQL:
    def __init__(self, host, port, user, password, database):
        self.db = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

        self.cur = self.db.cursor()


    # 获取所有行所有字段数据
    def all_data(self, table_name):
        self.cur.execute("select * from {}".format(table_name))
        list_res = self.cur.fetchall()
        return list_res


    # 插入一行数据
    def insert_one_row_data(self, table_name, str_tuple_fileds, tuple_values, num):
        str_s = "%s,"*num
        str_ins = "insert into {} {} values ({})".format(table_name, str_tuple_fileds, str_s.rstrip(","))
        self.cur.execute(str_ins, tuple_values)
        self.db.commit()


    # 插入多行数据
    def insert_many_rows_data(self, table_name, str_tuple_fileds, list_values, fileds_count):
        str_s = "%s," * fileds_count
        str_ins = "insert into {} {} values ({})".format(table_name, str_tuple_fileds, str_s.rstrip(","))
        self.cur.executemany(str_ins, list_values)
        self.db.commit()



if __name__ == '__main__':
    pg = PgSQL(
        host="112.74.33.64",
        port="5432",
        user="postgres",
        password="redbird@123",
        database="zz"
    )

    # pg.insert_one_row_data("stu", "(id, name)", (7, "李77"), 2)

    pg.insert_many_rows_data(
        table_name="stu",
        str_tuple_fileds="(id, name)",
        list_values=[(11, "小张"), (12, "李四"), (13, "赵六")],
        fileds_count=2
    )
    print(pg.all_data("stu"))

    pg.cur.close()
    pg.db.close()










