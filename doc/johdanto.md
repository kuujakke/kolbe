\newpage
# Johdanto
Sovellus on yksinkertainen blogisovellus. Sovellukseen kirjautunut käyttäjä voi kirjoittaa ja kommentoida Markdown -merkintäkielellä sivuja sekä lisätä sivuille aihetunnisteita.

Järjestelmän tavoitteena on tuottaa nopea ja kevyt blogipohja moniin eri käyttötarkoituksiin.

Sovellus toteutetaan Python -ohjelmointikielellä hyödyntäen kevyttä web frameworkia nimeltä Flask.
Tietokantana käytetään Amazon RDS palvelun PostgreSQL -tietokantaa.
Tietokanta on mahdollista vaihtaa, jos huolehtii siitä että sovelluksen käyttämät SQL -komennot toimivat myös uudessa tietokannassa.

Tietokannassa on taulut käyttäjille, sivuille, kommenteille ja aihetunnisteille. 

Alustana käytetään Amazonin webpalvelualustaa,
jolla orkestroidaan sovelluksen vaatima infrastruktuuri käyttäen Elastic Beanstalk palvelua.
AMI -pohjakuvana käytetään Amazonin tarjoamaa Python3 kuvaa.

Jatkuva tuotantoon vieminen hoituu automatisoidusti Amazonin CodePipelinea käyttäen.
Palvelu hakee muutoksen tapahtua Github repositoriosta uusimman version lähdekoodista.
Uuden tuotantoon viemisen hoitaa Amazonin CodeDeploy palvelu,
joka asentaa tarvittavat muutokset tuotantoympäristöön.
