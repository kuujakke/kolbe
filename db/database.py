from env import environment
import psycopg2


def execute(command):

    env = environment.DATABASES['default']

    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (
            env['NAME'],
            env['USER'],
            env['HOST'],
            env['PASSWORD']))
    except:
        print("Unable to connect to the database")

    cur = conn.cursor()

    try:
        cur.execute(command)
    except:
        print("SQL command failed to execute")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

def overview():
    users = execute("""SELECT * FROM "users";""")
    pages = execute("""SELECT * FROM "pages";""")
    comments = execute("""SELECT * FROM "comments";""")
    tags = execute("""SELECT * FROM "tags";""")

    print(users, pages, comments, tags)
    return "%s %s %s %s" % (users, pages, comments, tags)
