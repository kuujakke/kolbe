CREATE TABLE "users" (
  id SERIAL PRIMARY KEY,
  email text NOT NULL,
  password text NOT NULL
);

CREATE TABLE "pages" (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES "users",
  content text
);

CREATE TABLE "comments" (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES "users",
  page_id INTEGER REFERENCES "pages",
  content text
);

CREATE TABLE "tags" (
  id SERIAL PRIMARY KEY,
  page_id INTEGER REFERENCES "pages",
  content text
);