window.addEventListener('popstate', function() {
    // Forza il ricaricamento della pagina quando l'utente usa il tasto indietro
    window.location.reload();
  });

  // Verifica se la pagina è stata caricata dallo storico del browser (tasto indietro)
  if (performance.getEntriesByType('navigation')[0].type === 'back_forward') {
    window.location.reload();  // Ricarica la pagina se è stata caricata dal tasto indietro
  }
  
function mostraTextbox1() {
    document.getElementById("textbox1").style.display = "block"
    document.getElementById("textbox2").style.display = "none"
    document.getElementById("textbox3").style.display = "none"
    document.getElementById("file2").style.visibility = "visible"
    document.querySelectorAll(".file1").forEach(function(el) {
        el.style.visibility = "visible";
    });
}

function mostraTextbox2() {
    document.getElementById("textbox1").style.display = "none"
    document.getElementById("textbox2").style.display = "block"
    document.getElementById("textbox3").style.display = "none"
    document.getElementById("file2").style.visibility = "hidden"
    document.querySelectorAll(".file1").forEach(function(el) {
        el.style.visibility = "visible";
    });
}

function mostraTextbox3() {
    document.getElementById("textbox1").style.display = "none"
    document.getElementById("textbox2").style.display = "none"
    document.getElementById("textbox3").style.display = "block"
    document.getElementById("file2").style.visibility = "hidden"
    document.querySelectorAll(".file1").forEach(function(el) {
        el.style.visibility = "hidden";
    });
}

function refresh() {
    document.getElementById("textbox1").style.display = "none"
    document.getElementById("textbox2").style.display = "none"
    document.getElementById("textbox3").style.display = "none"
    document.getElementById("file2").style.visibility = "visible"
    document.querySelectorAll(".file1").forEach(function(el) {
        el.style.visibility = "visible";
    });

    var colonne = document.querySelectorAll('.colonnaUP');
    colonne.forEach(function(colonna) {
        colonna.style.display = 'block';
    });
    var tipologie = document.querySelectorAll('.tipologiaUP');
    tipologie.forEach(function(tipologia) {
        tipologia.style.display = 'none';
    });

    document.getElementById("colonnaDOWN").style.display = "block"
    document.getElementById("tipologiaDOWN").style.display = "none"
    document.getElementById("colonnaDOWNscelta3").style.display = "none"

}

function checkboxUP() {
    const upTipologia = document.querySelectorAll(".tipologiaUP");
    const upElements = document.querySelectorAll(".colonnaUP");

    upTipologia.forEach(function(element) {
        if (element.style.display === 'block') {
            element.style.display = "none";
        } else {
            element.style.display = "block";
        }
    });

    upElements.forEach(function(element2) {
        if (element2.style.display === 'none') {
            element2.style.display = "block";
        } else {
            element2.style.display = "none";
        }
    });
}

function checkboxDOWN() {
    if (document.getElementById("tipologiaDOWN").style.display == 'block'){
        document.getElementById("tipologiaDOWN").style.display = "none"
        document.getElementById("colonnaDOWN").style.display = "block"
    }else{
        document.getElementById("tipologiaDOWN").style.display = "block"
        document.getElementById("colonnaDOWN").style.display = "none"
    }
}

function openSegnale(){
    if (document.getElementById("colonnaDOWNscelta3").style.display == 'block'){
        document.getElementById("colonnaDOWNscelta3").style.display = "none"
    }else{
        document.getElementById("colonnaDOWNscelta3").style.display = 'block'
    }
}

