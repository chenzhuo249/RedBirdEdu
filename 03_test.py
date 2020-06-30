import random

from tools.my_psycopg2 import PgSQL
from tools.create_name import create_name

class Student:

    def __init__(self):
        self.pg = PgSQL(
            host="112.74.33.64",
            port="5432",
            user="postgres",
            password="redbird@123",
            database="zz"
        )

    def create_data(self, count):
        list_res = []
        for i in range(1, count + 1):
            name = create_name(1).__next__()
            age = random.randint(17, 20)
            score = random.randint(50, 99)
            tup = (i, name, age, score)
            list_res.append(tup)
        return list_res


    def run(self):
        print("数据生成中...")
        list_data = self.create_data(50)
        print("{}条数据生成成功!".format(len(list_data)))
        print("插入数据库中...")
        self.pg.insert_many_rows_data(
            table_name="stu",
            str_tuple_fileds="(id, name, age, score)",
            fileds_count=4,
            list_values=list_data
        )



if __name__ == '__main__':
    s = Student()
    s.run()


