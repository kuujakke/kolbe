\newpage
# Johdanto
Sovellus on yksinkertainen blogisovellus. Sovellukseen kirjautunut käyttäjä voi kirjoittaa ja kommentoida Markdown -merkintäkielellä sivuja sekä lisätä sivuille aihetunnisteita.

Järjestelmän tavoitteena on tuottaa käyttäjille nopea ja kevyt blogipohja moniin eri käyttötarkoituksiin.

Sovellus toteutetaan Python -ohjelmointikielellä hyödyntäen kevyttä web frameworkia nimeltä Flask.

Tietokannassa on taulut käyttäjille, sivuille, kommenteille ja aihetunnisteille. 

Alustana käytetään Kontena mikropalvelualustaa, jolla orkestroidaan sovelluksen vaatimat Docker -kontit.
Sovelluksen käyttämiä Docker kontteja ovat Python ohjelmakoodin sisältävä 'app' -kontti sekä PostgreSQL kontti 'db'.
Konttien yhteisenä pohjakuvana on Alpine Linux, joka on hyvin pieni linux kuva Docker konteille.

Kuormanjakajana käytetään Kontenan omaa load-balanceria.

