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
    except ConnectionError:
        print("Unable to connect to the database")


def execute(command, variables=None):
    conn = connect()
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


def new_page(page):
    sql = """INSERT INTO pages ("user_id", "content") VALUES (%s, %s);"""
    execute(sql, (page.user_id, page.content))


def new_comment(comment):
    sql = """INSERT INTO comments ("user_id", "page_id", "content") VALUES (%s, %s, %s);"""
    execute(sql, (comment.user_id, comment.page_id, comment.content))


def new_tag(tag):
    sql = """INSERT INTO tags ("page_id", "content") VALUES (%s, %s);"""
    execute(sql, (tag.page_id, tag.content))


def new_user(user):
    sql = """INSERT INTO users ("email", "password") VALUES (%s, %s);"""
    execute(sql, (user.user_id, user.password))


def get_page(page):
    sql = """SELECT "id", "user_id", "content" FROM "pages" WHERE "id" = %s;"""
    rows = execute(sql, (page.id,))
    if rows:
        return Page(rows[0])


def get_comment(comment):
    sql = """SELECT "id", "user_id", "page_id", "content" FROM "comments" WHERE "id" = %s;"""
    rows = execute(sql, (comment.id,))
    if rows:
        return Comment(rows[0])


def get_tag(tag):
    sql = """SELECT "id", "page_id", "content" FROM "tags" WHERE "id" = %s;"""
    rows = execute(sql, (tag.id,))
    if rows:
        return Tag(rows[0])


def get_user(user):
    sql = """SELECT "id", "email", "password" FROM "users" WHERE "id" = %s;"""
    rows = execute(sql, (user.id,))
    if rows:
        return User(rows[0])


def save_page(page):
    sql = """UPDATE pages SET "user_id" = %s, "content" = %s WHERE "id" = %s""";
    execute(sql, (page.user_id, page.content, page.id))


def save_comment(comment):
    sql = """UPDATE comments SET "user_id" = %s, "content" = %s WHERE "id" = %s;"""
    execute(sql, (comment.user_id, comment.content, comment.id))


def save_tag(tag):
    sql = """UPDATE tags SET "page_id" = %s, "content" = %s WHERE "id" = %s;"""
    execute(sql, (tag.user_id, tag.content, tag.id))


def save_user(user):
    sql = """UPDATE users SET "email" = %s, "password" = %s WHERE "id" = %s;"""
    execute(sql, (user.user_id, user.content, user.id))


def delete_page(page_id):
    sql = """DELETE FROM pages WHERE "id" = %s;"""
    execute(sql, (page_id,))


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

