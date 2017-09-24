from app.models import DB


class Comment(DB):
    def __init__(self, data=None):
        if data:
            self.id, self.user_id, self.page_id, self.content = data

    def get_all_comments(self):
        rows = self.execute("""SELECT "id", "user_id", "page_id", "content" FROM "comments";""")
        comments = []
        for row in rows:
            comment = Comment(row)
            comments.append(comment)

        return comments

    def new_comment(self, comment):
        sql = """INSERT INTO comments ("user_id", "page_id", "content") VALUES (%s, %s, %s);"""
        self.execute(sql, (comment.user_id, comment.page_id, comment.content))

    def get_comment(self, comment):
        sql = """SELECT "id", "user_id", "page_id", "content" FROM "comments" WHERE "id" = %s;"""
        rows = self.execute(sql, (comment.id,))
        if rows:
            return Comment(rows[0])

    def save_comment(self, comment):
        sql = """UPDATE comments SET "user_id" = %s, "content" = %s WHERE "id" = %s;"""
        self.execute(sql, (comment.user_id, comment.content, comment.id))
