from flask import Flask, Response
from flask_cors import CORS
import mysql.connector
import json
# Jotta end point toimii javascriptissä pitää vielä asentaa Flask Cors ja importoida se
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/toimialat')
def toimialat():
    print("kissa")
    sql = "select nimi from toimiala"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)
    paluujson = json.dumps(tulos)
    tilakoodi = 200
    # palautetaan muutakin kuin json ja siksi tehdään Response olio joka sisältää statuksen ja nimetypen
    return Response(response=paluujson, status=tilakoodi, mimetype="application/json")


@app.route('/toimitajat')
def toimitajat():
    print("kissa")
    sql = "select nimi from toimitajat"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)
    paluujson = json.dumps(tulos)
    tilakoodi = 200
    # palautetaan muutakin kuin json ja siksi tehdään Response olio joka sisältää statuksen ja nimetypen
    return Response(response=paluujson, status=tilakoodi, mimetype="application/json")


@app.route('/toimittaneet/<toimiala>')
def toimittaneet(toimiala):
    sql = ("select DISTINCT toimittaja.nimi "
           "from toimittaja, osto, toimiala "
           "where toimittaja.toimittaja_id = osto.toimittaja_id "
           "AND osto.toimiala_id = toimiala.toimiala_id "
           "AND toimiala.nimi = '" + toimiala + "'")

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    paluujson = json.dumps(tulos)
    tilakoodi = 200
    # palautetaan muutakin kuin json ja siksi tehdään Response olio joka sisältää statuksen ja nimetypen
    return Response(response=paluujson, status=tilakoodi, mimetype="application/json")

@app.route('/toimittaneet/<toimiala>')
def toimitajatToimialalla(toteuma):
    sql = ("select DISTINCT osto.toteuma "
           "from  osto, toimitaja "
           "where toimittaja.toimittaja_id = osto.toimittaja_id ")

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    paluujson = json.dumps(tulos)
    tilakoodi = 200
    # palautetaan muutakin kuin json ja siksi tehdään Response olio joka sisältää statuksen ja nimetypen
    return Response(response=paluujson, status=tilakoodi, mimetype="application/json")

yhteys = mysql.connector.connect(
    host="127.0.0.1",  # tietokantapalvelimen ip-osoite (tässä "localhost")
    port=3306,  # TCP-porttinumero (oletuksena 3306)
    database="hki",  # käytettävän tietokannan nimi
    user="barano",  # mariadb:n käyttäjätunnus
    password="1000",  # mariadb:n salasana
    autocommit=True,
    collation="utf8mb4_general_ci"
)
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
