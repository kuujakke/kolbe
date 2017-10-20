\newpage

# Asennustiedot

Sovellus on asennettuna Amazonin ElasticBeanstalk palveluun. 
Sovellus käynnistyy Amazonin tekemässä Python3 AMI-virtuaalikonekuvassa.
Käynnistys- ja käyttöohjeessa on ohjeet sovelluksen ajamiseksi paikallisesti ja
näitä ohjeita voidaan soveltaa myös kun sovellusta asennetaan uudelle palvelimelle.
Lisäksi sovellus on mahdollista rakentaa Docker -kontiksi juurikansiossa sijaitsevan `Dockerfile`n avulla ja
täten on siirrettävissä mille tahansa alustalle, joka pystyy käynnistämään Docker -kontin.

Tietokantayhteyden sovellus muodostaa käynnistyksen yhteydessä annetuilla ympäristömuuttujilla.
Nämä muuttujat ovat määritelty tarkemmin käynnistys- ja käyttöohjeessa.
