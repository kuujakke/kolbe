INSERT INTO "users" (email, password) VALUES ('testi@helsinki.fi', 'salaisuus');
INSERT INTO "pages" (user_id, content) VALUES (1, '# Testisivu 1 \n Tämä on *testi*');
INSERT INTO "comments" (page_id, user_id, content) VALUES (1, 1, 'Testikommentti **painokkaasti** ilmaistuna');
INSERT INTO "tags" (page_id, content) VALUES (1, 'Testiaiheentunnistin');