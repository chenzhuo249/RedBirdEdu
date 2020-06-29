
from my_psycopg2 import PgSQL

class Student:

    def __init__(self):
        self.pg = PgSQL(
            host="112.74.33.64",
            port="5432",
            user="postgres",
            password="redbird@123",
            database="zz"
        )

    def run(self):
        list_res = []
        for i in range(1, 101):






