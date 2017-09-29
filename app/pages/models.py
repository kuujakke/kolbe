from app.models import DB


class Page(DB):
    def __init__(self, data=None):
        if data:
            self.id, self.user_id, self.content = data

    def get_all_pages(self):
        rows = self.execute("""SELECT "id", "user_id", "content" FROM "pages";""",)
        pages = []
        for row in rows:
            page = Page((row[0], row[1], row[2]))
            pages.append(page)

        return pages

    def new_page(self, data):
        sql = """INSERT INTO pages ("user_id", "content") VALUES (%s, %s);"""
        self.execute(sql, (data.user_id, data.content))

    def get_page(self, page_id):
        sql = """SELECT "id", "user_id", "content" FROM "pages" WHERE "id" = %s;"""
        rows = self.execute(sql, (page_id,))
        if rows:
            return Page((rows[0][0], rows[0][1], rows[0][2]))

    def save_page(self):
        sql = """UPDATE pages SET "user_id" = %s, "content" = %s WHERE "id" = %s""";
        self.execute(sql, (self.user_id, self.content, self.id))

    def delete_page(self):
        sql = """DELETE FROM pages WHERE "id" = %s;"""
        self.execute(sql, (self.id,))
