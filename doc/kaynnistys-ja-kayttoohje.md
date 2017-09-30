\newpage
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

\newpage

## Sovelluksen käynnistäminen paikallisesti

Ohjeet on yhteensopivia Cubbli/Ubuntu käyttöjärjestelmien kanssa.

### Esivalmistelut

- Asenna [Python3](https://www.python.org/) ja [virtualenv](https://virtualenv.pypa.io/en/stable/) komennolla:

	```sudo apt install python3-dev python3-pip -y && sudo pip install virtualenv```

- Luo uusi virtuaaliympäristö ja ota ympäristö käyttöön komennolla:
	
	```virtualenv kolbe-env && source kolbe-env/bin/activate```


### Sovelluksen lataaminen

- Kloonaa git repository komennolla ja siirry sovelluksen kansioon:

	```git clone https://github.com/kuujakke/kolbe.git && cd kolbe```

### Riippuvuuksien asentaminen

- Asenna riippuvuudet komennolla: 

	```pip install -r requirements.txt```

### Käynnistäminen

- Sovelluksen käynnistäminen käy helposti skriptillä: 

	```./scripts/start.sh```
