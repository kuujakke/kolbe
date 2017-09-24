from app.models import DB


class User(DB):
    def __init__(self, data=None):
        if data:
            self.id, self.email, self.password = data

    def get_all_users(self):
        rows = self.execute("""SELECT "id", "email", "password" FROM "users";""")
        users = []
        for row in rows:
            user = User(row)
            users.append(user)

        return users

    def new_user(self, user):
        sql = """INSERT INTO users ("email", "password") VALUES (%s, %s);"""
        self.execute(sql, (user.user_id, user.password))

    def get_user(self, user):
        sql = """SELECT "id", "email", "password" FROM "users" WHERE "id" = %s;"""
        rows = self.execute(sql, (user.id,))
        if rows:
            return User(rows[0])

    def save_user(self, user):
        sql = """UPDATE users SET "email" = %s, "password" = %s WHERE "id" = %s;"""
        self.execute(sql, (user.user_id, user.content, user.id))
