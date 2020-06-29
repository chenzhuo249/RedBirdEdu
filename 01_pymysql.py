import pymysql
import random

class MyStu:
    def __init__(self):
        self.db = pymysql.connect(
            host="60.205.247.115",
            port=3306,
            user="chenzhuo",
            password="mzSFRkpvU5HIuaBGEJ6O1Ib4NZiDoIst",
            database="myStu",
            charset="utf8"
        )

        self.cur = self.db.cursor()
        self.list_course = ["语文", "数学", "英语"]


    def insert_data(self):


        stu_ins = "insert into stu (id, `name`) values (%s, %s);"
        sco_ins = "insert into sco (course, score, stu_id) values (%s, %s, %s);"
        list_name = ["彭万里","高大山","谢大海","马宏宇","林莽","黄强辉","章汉夫","范长江","林君雄","谭平山","朱希亮"]


        for i in range(1, 11):

            self.cur.execute(stu_ins, [i, list_name[i-1]])
            self.db.commit()

            for cou in self.list_course:
                score = random.randint(40, 99)
                list_res = [cou, score, i]
                self.cur.execute(sco_ins, list_res)
                self.db.commit()

        self.cur.close()
        self.db.close()

    def run(self):
        self.insert_data()


if __name__ == '__main__':
    m = MyStu()
    m.run()















