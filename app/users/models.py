from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import struct

from app.models import DB


class User(DB, UserMixin):
    def __init__(self, data=None):
        if data:
            self.password = ''
            self.user_id, self.email, password = data
            self.set_password(password)

    def __str__(self):
        return "ID: %s, Email: %s, Password: %s" % (self.user_id, self.email, self.password)

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
        sql = """SELECT "user_id", "email", "password" FROM "users" WHERE "user_id" = %s;"""
        rows = self.execute(sql, (user_id,))
        if rows:
            return User(rows[0])

    def get_id(self):
        return self.user_id

    def get_by_email(self, email):
        sql = """SELECT "user_id", "email", "password" FROM "users" WHERE "email" = %s;"""
        rows = self.execute(sql, (email,))
        if rows:
            return User(rows[0])
        else:
            return None

    def save(self, user):
        sql = """UPDATE users SET "email" = %s, "password" = %s WHERE "user_id" = %s;"""
        self.execute(sql, (user.user_id, user.content, user.id))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def verify(self, email, password):
        user = self.get_by_email(email)
        if user is not None:
            if check_password_hash(user.password, password):
                return user
        return None
