from app.models import DB


class Comment(DB):
    def __init__(self, data=None):
        if data:
            self.comment_id, self.user_id, self.page_id, self.content = data

    def get_all_comments(self):
        rows = self.execute("""SELECT "comment_id", "user_id", "page_id", "content" FROM comments;""")
        comments = []
        for row in rows:
            comment = Comment(row)
            comments.append(comment)

        return comments

    def new_comment(self, comment):
        sql = """INSERT INTO comments ("user_id", "page_id", "content") VALUES (%s, %s, %s);"""
        self.execute(sql, (comment.user_id, comment.page_id, comment.content))

    def get_comment(self, comment):
        sql = """SELECT "comment_id", "user_id", "page_id", "content" FROM comments WHERE "comment_id" = %s;"""
        rows = self.execute(sql, (comment.id,))
        if rows:
            return Comment(rows[0])

    def save_comment(self, comment):
        sql = """UPDATE comments SET "user_id" = %s, "content" = %s WHERE "comment_id" = %s;"""
        self.execute(sql, (comment.user_id, comment.content, comment.comment_id))

    def recent_comments(self, count):
        # Tähän komento joka hakee 'count' verran viimeisimpiä kommentteja
        return self.get_all_comments()

    def get_by_page_id(self, page_id):
        sql = """SELECT "comment_id", "user_id", "page_id", "content" FROM comments WHERE "page_id" = %s;"""
        rows = self.execute(sql, (page_id,))
        comments = []
        if rows:
            for row in rows:
                comment = Comment(row)
                comments.append(comment)
            return comments
        return None
