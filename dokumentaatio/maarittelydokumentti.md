#Määrittelydokumentti
Ohjelmointikielenä Python. Vertaisarvioinnissa myös Java mahdollinen.

##Toteutettavat algoritmit ja tietorakenteet
Alustavasti vaikuttaa kurssimateriaalissa ehdotettu Bowyer-Watson -algoritmi Delanay-kolmiointiin 
huoneiden välille sopivalta. Tämä kuitenkin saattaa muuttua, jos jatkossa tulee ilmi parempia, 
jotka sopivat ongelmiin paremmin. Todennäköisimmin kuitenkin tällöin lisätään rinnakkaisia 
algoritmeja. Lisäksi reittien etsimiseen käytetään A* algoritmia.

Tietorakenteina käytetään taulukoita, joihin tallennetaan tarvittavat tiedot kartan 
generoinnissa. Tätä laajennetaan tarpeen mukaan.

##Ratkaistava ongelma
Valitulla algoritmilla pystytään laskemaan halutuille huoneille helposti minimum spanning tree 
(tarkista suomennos). Näin pystytään eri alueiden välille luomaan luotettavasti käytävät ilman 
turhia silmukoita. 

Alueiden välisten reittien etsimistä varten A* on tehokas algoritmi, jolla polut saadaan 
luotua.

##Syötteet ja käyttö
Ohjelmalle annetaan spekseinä esimerkiksi alueiden määrä, kokomääreitä, mahdollisesti peliin 
liittyviä määreitä, kuten vihollisia ja aarteita ja niiden suhteellista määrää. 

Ohjelmalle luodaan selainkäyttöliittymä Flaskia käyttäen, jossa eri määreitä säätämällä 
visualisoidaan lopputulos. 

Mahdollisesti ohjelmalle luodaan myös versio, jolla pystytään generoimaan päättymätön kartta. 
Tämä riippuu toteutuksen aikataulun riittävyydestä.

##Opinto-ohjelma ja kieli
Opinto-ohjelma: Tietojenkäsittelytieteen kandiohjelma. Kielenä suomi.
