async function haeToimialat() {

  console.log("haeToimialat kutsuttu")

  try {

    const vastaus = await fetch('http://localhost:3000/toimialat');

    // vastaus sisältää muutakin kuin meidän end pointin palauttaman jsonin. Se sisältää mm. http tilakoodin
    // ja siksi se json pitää vielä erikseen pyytää vastaukselta
    const jsonToimialat = await vastaus.json();
    console.log(jsonToimialat)

    taytaVetolaatikko(jsonToimialat);
  } catch (error) {
    console.log(error.message);
  } finally {
    console.log('asynchronous load complete');
  }
}

function taytaVetolaatikko(jsonToimialat) {
  // Generoidaan HTML-merkkijono jossa select tagi ja option tagi
  let htmlvetolaatikko = '<select>';
  for (let i = 0; i < jsonToimialat.length; i++) {
    let toimiala = jsonToimialat[i];
    htmlvetolaatikko = htmlvetolaatikko + '<option>' + toimiala + '</option>';
  }
  htmlvetolaatikko = htmlvetolaatikko + '</select>';

  //Lisätään äsken generoitu html-koodia sisältävä merkkijono html pohjassa olevan select tagin tilalle
  document.getElementById('toimialat').innerHTML = htmlvetolaatikko;
}

async function haeYritykset(){
  console.log("haeYritykset()")

  const toimilaVetolaatikko = document.getElementById("toimialat");
  let toimiala = toimilaVetolaatikko.value;

  try {

    const vastaus = await fetch('http://localhost:3000/toimittaneet/' + toimiala);

    const jsonYritykset = await vastaus.json();

    teeTaulukkoYrityksista(jsonYritykset)
  } catch (error) {
    console.log(error.message);
  } finally {
    console.log('asynchronous load complete');
  }

}
function teeTaulukkoYrityksista(jsonYritykset){
  // TR avaa uuden rivin, TD avaa uuden sarakkeen
  let htmltaulukko = '<tr><td>Yrityksen nimi</td></tr>';
  for (let i = 0; i < jsonYritykset.length; i++) {
    let yritys = jsonYritykset[i];
    htmltaulukko = htmltaulukko + '<tr><td>' + yritys + '</td></tr>';
  }
  htmltaulukko = htmltaulukko + ''
  document.getElementById('yritykset').innerHTML = htmltaulukko;
}

console.debug("haloo")
haeToimialat()
const haeYrityksetButton = document.getElementById("haenappula");
haeYrityksetButton.addEventListener("click", haeYritykset);





