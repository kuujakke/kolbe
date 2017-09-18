import psycopg2
from flask import current_app as app

def execute(command):

    env = app.config['DATABASES']['default']

    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (
            env['NAME'],
            env['USER'],
            env['HOST'],
            env['PASSWORD']))
        cur = conn.cursor()
    except:
        print("Unable to connect to the database")


    try:
        cur.execute(command)
    except:
        print("SQL command failed to execute")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows


def get_pages():
    return execute("""SELECT * FROM "pages";""")


def get_comments():
    return execute("""SELECT * FROM "comments";""")


def get_users():
    return execute("""SELECT * FROM "users";""")


def get_tags():
    return execute("""SELECT * FROM "tags";""")
