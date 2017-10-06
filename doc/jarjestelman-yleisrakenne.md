\newpage

# Järjestelmän yleisrakenne

Järjestelmää suunniteltaessa on pyritty MVC -mallin mukaiseen hakemistorakenteeseen.
Pääasiassa sivuston ohjelmakoodi sijaitsee hakemistossa `app`. 
Jokaiselle Kontrollerille on oma Python -modulinsa (hakemisto) tämän hakemiston sisällä.
Modulit sisältävät `models.py` tiedoston, johon Mallin Luokka tietokanta yhteyksineen on määritelty.
Moduleissa on myös `views.py` tiedosto, jonka avulla HTTP kutsut reititetään sopivaan Näkymään.
Modulin Näkymät sijaitsevat hakemistossa `app/templates/<modulin_nimi>`.

## Riippuvuudet

Sovelluksen käynnistämistä varten on asennettava riippuvuuksia, jotka on määritelty sovelluksen juurihakemistosta löytyvästä tiedostosta nimeltä `requirements.txt`.

## Asetukset

Sovellus käyttää isäntäjärjestelmän tarjoamia ympäristömuuttujia asetuksien saamiseksi.
Tarkempi listaus sovelluksen tarvitsemista ympäristömuuttujista Käynnistys- ja Käyttöohjeessa.
Asetuksien noutaminen ympäristömuuttujista on määritelty tiedostossa `config.py`.

## Tietokanta

Tietokannan luomis- ja tuhoamislausekkeet sekä testidatan syöttämislauseke löytyvät hakemistosta `app/database`.