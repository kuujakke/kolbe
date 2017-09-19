import psycopg2
from flask import current_app as app


def connect():
    env = app.config['DATABASES']['default']

    try:
        return psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (
            env['NAME'],
            env['USER'],
            env['HOST'],
            env['PASSWORD']))
    except:
        print("Unable to connect to the database")


def execute(command):
    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(command)
    except:
        print("SQL command failed to execute")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows


def get_all_pages():
    rows = execute("""SELECT "id", "user_id", "content" FROM "pages";""")
    pages = []
    for row in rows:
        page = Page(row)
        pages.append(page)

    return pages


def get_all_comments():
    rows = execute("""SELECT "id", "user_id", "page_id", "content" FROM "comments";""")
    comments = []
    for row in rows:
        comment = Comment(row)
        comments.append(comment)

    return comments


def get_all_users():
    rows = execute("""SELECT "id", "email", "password" FROM "users";""")
    users = []
    for row in rows:
        user = User(row)
        users.append(user)

    return users


def get_all_tags():
    rows = execute("""SELECT "id", "page_id", "content" FROM "tags";""")
    tags = []
    for row in rows:
        tag = Tag(row)
        tags.append(tag)

    return tags


def get_page_by_id(id):
    sql = """SELECT "id", "user_id", "content" FROM "pages" WHERE "id" = {0};"""
    rows = execute(sql.format(id))
    if rows:
        page = Page(rows[0])

    return page


def get_comment_by_id(id):
    sql = """SELECT "id", "user_id", "page_id", "content" FROM "comments" WHERE "id" = {0};"""
    rows = execute(sql.format(id))
    if rows:
        comment = Comment(rows[0])

    return comment


def get_tag_by_id(id):
    sql = """SELECT "id", "page_id", "content" FROM "tags" WHERE "id" = {0};"""
    rows = execute(sql.format(id))
    if rows:
        tag = Tag(rows[0])

    return tag


def get_user_by_id(id):
    sql = """SELECT "id", "email", "password" FROM "users" WHERE "id" = {0};"""
    rows = execute(sql.format(id))
    if rows:
        user = User(rows[0])


def save_page_content(page):
    sql = """UPDATE "pages" SET "content" = '{0}' WHERE "id" = {1};"""
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql.format(page.content, page.id))
    conn.commit()
    cur.close()
    conn.close()

class Page:
    def __init__(self, row):
        self.id = row[0]
        self.user_id = row[1]
        self.content = row[2]


class Comment:
    def __init__(self, row):
        self.id = row[0]
        self.user_id = row[1]
        self.page_id = row[2]
        self.content = row[3]


class Tag:
    def __init__(self, row):
        self.id = row[0]
        self.page_id = row[1]
        self.content = row[2]


class User:
    def __init__(self, row):
        self.id = row[0]
        self.email = row[1]
        self.password = row[2]

