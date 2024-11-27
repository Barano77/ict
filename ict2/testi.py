import mysql.connector
yhteys = mysql.connector.connect(
    host = "127.0.0.1",  #ip osoite
    port = 3306,   #tcp
    database = "hki",
    user = "barano", #mariadb id
    password = "1000", #mariadb salasana
    autocommit = True

)
#funktio joka hae tietokannasta toimialta ja palauta ne kutsujalle
def hae_toimialat():

    #määritelään sql-kysely.
    sql = "select * from toimiala"

    #lähetetään kysely
    kursori = yhteys.cursor()
    kursori.execute(sql)

    #"pyydetään vastaukset ja tulostetaan ne"
    tulos = kursori.fetchall()
    return tulos

#kutsutaan hae toimalat-funktiota ja käsitellään se palauttamat tulokset
tulos = hae_toimialat()
for rivi in tulos:
    print(rivi[1])


