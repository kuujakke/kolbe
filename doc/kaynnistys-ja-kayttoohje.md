# Käynnistys- / käyttöohje

Harjoitustyö on asennettuna osoitteessa: http://kolbe.eu-central-1.elasticbeanstalk.com

## Tunnukset

Käyttäjätunnus | Salasana
---------------|---------
testi@helsinki.fi | salaisuus

## Ympäristömuuttujat

Jos haluat ajaa sovellusta paikallisesti omalta koneeltasi tarvitset testausta varten  ympäristömuuttujat.

Muuttuja | Arvo
---------|-----
FLASK_APP | application.py
FLASK_CONFIG | development
RDS_HOSTNAME | kolbe-db.c7jodkrsqzdr.eu-central-1.rds.amazonaws.com
RDS_PASSWORD | W7S+13SRcdfcOoMXAi7SlBrjih3eAyfj
RDS_PORT | 5432
RDS_DB_NAME | kolbe
RDS_USERNAME | kuujakke
SECRET_KEY | R4/OyNkVoYWZRibbSqQoSZlR6xqLi9Qw

## Sovelluksen käynnistäminen

- Asenna riippuvuudet komennolla: ```sudo pip install -r requirements.txt```

- Aja komennolla ```export YMPÄRISTÖMUUTTUJAT python application.py```
