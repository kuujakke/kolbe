from flask_login import UserMixin
import struct

from app.models import DB


class User(DB, UserMixin):
    def __init__(self, data=None):
        if data:
            self.id, self.email, self.password = data

    def all(self):
        rows = self.execute("""SELECT "id", "email", "password" FROM "users";""")
        users = []
        for row in rows:
            user = User(row)
            users.append(user)

        return users

    def new(self, user):
        sql = """INSERT INTO users ("email", "password") VALUES (%s, %s);"""
        self.execute(sql, (user.user_id, user.password))

    def get(self, user_id):
        sql = """SELECT "id", "email", "password" FROM "users" WHERE "id" = %s;"""
        rows = self.execute(sql, (user_id,))
        if rows:
            return User(rows[0])

    def get_id(self):
        return self.id

    def get_email(self, email):
        sql = """SELECT "id", "email", "password" FROM "users" WHERE "email" = %s;"""
        rows = self.execute(sql, (email,))
        if rows:
            return User(rows[0])

    def save(self, user):
        sql = """UPDATE users SET "email" = %s, "password" = %s WHERE "id" = %s;"""
        self.execute(sql, (user.user_id, user.content, user.id))
