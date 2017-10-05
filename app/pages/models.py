from app.comments.models import Comment
from app.models import DB


class Page(DB):
    def __init__(self, data=None):
        if data:
            self.page_id, self.user_id, self.content = data

    def get_all_pages(self):
        rows = self.execute("""SELECT "page_id", "user_id", "content" FROM "pages";""",)
        pages = []
        for row in rows:
            page = Page((row[0], row[1], row[2]))
            pages.append(page)

        return pages

    def get_recent(self, count):
        # Tähän haku joka hakee 'count' määrän verran viimeisimpiä sivuja
        return self.get_all_pages()

    def new_page(self, data):
        sql = """INSERT INTO pages ("user_id", "content") VALUES (%s, %s);"""
        self.execute(sql, (data.user_id, data.content))

    def get_page(self, page_id):
        sql = """SELECT "page_id", "user_id", "content" FROM "pages" WHERE "page_id" = %s;"""
        rows = self.execute(sql, (page_id,))
        if rows:
            return Page((rows[0][0], rows[0][1], rows[0][2]))

    def save_page(self):
        sql = """UPDATE pages SET "user_id" = %s, "content" = %s WHERE "page_id" = %s""";
        self.execute(sql, (self.user_id, self.content, self.page_id))

    def delete_page(self):
        sql = """DELETE FROM pages WHERE "page_id" = %s;"""
        self.execute(sql, (self.page_id,))

    def get_comments(self):
        return Comment.get_by_page_id(Comment(), self.page_id)