from app.models import DB


def rows_to_tags(rows):
    tags = []
    for row in rows:
        tag = Tag(row)
        tags.append(tag)
    return tags


class Tag(DB):
    def __init__(self, data=None):
        if data:
            self.tag_id, self.content = data

    def get_all_tags(self):
        rows = self.execute("""SELECT "tag_id", "content" FROM tags;""")
        if rows:
            return rows_to_tags(rows)

    def new_tag(self, tag):
        sql = """INSERT INTO tags ("content") VALUES (%s);"""
        self.execute(sql, (tag.content,))

    def get_tag(self, tag):
        sql = """SELECT "tag_id", "content" FROM tags WHERE "tag_id" = %s;"""
        rows = self.execute(sql, (tag.id,))
        if rows:
            return Tag(rows[0])

    def save_tag(self, tag):
        sql = """UPDATE tags SET "content" = %s WHERE "tag_id" = %s;"""
        self.execute(sql, (tag.content, tag.id))

    def popular_tags(self, count):
        # Tähän komento joka hakee 'count' verran suosituimpia aihetunnisteita
        return self.get_all_tags()

    def get_by_page_id(self, page_id):
        sql = """SELECT tags.tag_id, content FROM page_tags LEFT JOIN tags ON page_tags.tag_id = tags.tag_id WHERE page_id = %s;"""
        rows = self.execute(sql, (page_id,))
        if rows:
            return rows_to_tags(rows)