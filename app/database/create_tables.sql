CREATE TABLE "users" (
  user_id SERIAL PRIMARY KEY,
  email text NOT NULL,
  password text NOT NULL
);

CREATE TABLE "pages" (
  page_id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES "users" ON DELETE SET NULL,
  content text
);

CREATE TABLE "comments" (
  comment_id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES "users" ON DELETE SET NULL,
  page_id INTEGER REFERENCES "pages" ON DELETE CASCADE,
  content text
);

CREATE TABLE "tags" (
  tag_id SERIAL PRIMARY KEY,
  content text
);

CREATE TABLE "page_tags" (
  page_tag_id SERIAL PRIMARY KEY,
  page_id INTEGER REFERENCES "pages" ON DELETE CASCADE,
  tag_id INTEGER REFERENCES "tags" ON DELETE CASCADE
);