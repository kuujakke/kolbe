from app.models import DB


class Tag(DB):
    def __init__(self, data=None):
        if data:
            self.tag_id, self.page_id, self.content = data

    def get_all_tags(self):
        rows = self.execute("""SELECT "tag_id", "page_id", "content" FROM tags;""")
        tags = []
        for row in rows:
            tag = Tag(row)
            tags.append(tag)

        return tags

    def new_tag(self, tag):
        sql = """INSERT INTO tags ("page_id", "content") VALUES (%s, %s);"""
        self.execute(sql, (tag.page_id, tag.content))

    def get_tag(self, tag):
        sql = """SELECT "tag_id", "page_id", "content" FROM tags WHERE "tag_id" = %s;"""
        rows = self.execute(sql, (tag.id,))
        if rows:
            return Tag(rows[0])

    def save_tag(self, tag):
        sql = """UPDATE tags SET "page_id" = %s, "content" = %s WHERE "tag_id" = %s;"""
        self.execute(sql, (tag.user_id, tag.content, tag.id))

    def popular_tags(self, count):
        # Tähän komento joka hakee 'count' verran suosituimpia aihetunnisteita
        return self.get_all_tags()
