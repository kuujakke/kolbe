import psycopg2
from flask import current_app as app


class DB:
    def connect(self):
        env = app.config['DATABASES']['default']

        try:
            return psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (
                env['NAME'],
                env['USER'],
                env['HOST'],
                env['PASSWORD']))
        except ConnectionError:
            print("Unable to connect to the database")

    def execute(self, command, variables=None):
        conn = self.connect()
        cur = conn.cursor()

        try:
            if variables:
                sql = cur.mogrify(command, variables)
                cur.execute(sql)
            else:
                cur.execute(command)
        except SyntaxError:
            print("SQL command failed to execute")

        rows = ''

        if "SELECT" in cur.query.decode():
            rows = cur.fetchall()

        conn.commit()

        cur.close()
        conn.close()

        return rows
