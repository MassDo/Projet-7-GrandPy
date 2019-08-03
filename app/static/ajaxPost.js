

var httpRequest;
document.getElementById("ajaxButton").onclick = function() { 
    var userInput = document.getElementById("ajaxTextbox").value;
    makeRequest('/form', userInput); 
};

function makeRequest(url, userInput) {
    httpRequest = new XMLHttpRequest();     
    if (!httpRequest) {
      alert('Abandon :( Impossible de créer une instance de XMLHTTP');
      return false;
    }
    httpRequest.onreadystatechange = callBack; // callback function
    httpRequest.open('POST', url);
    httpRequest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    httpRequest.send('userInput=' + encodeURIComponent(userInput));
}
// response callback function
function callBack() {
  if (httpRequest.readyState === XMLHttpRequest.DONE) { // if request is done
    if (httpRequest.status === 200) { // if the ressource is find
        var response = JSON.parse(httpRequest.responseText) // transform a json into a JS object
        // remplir les cases ICI
        document.getElementById("address").innerHTML = response.address
        document.getElementById("title").innerHTML = response.title
        document.getElementById("link").innerHTML = response.link
        document.getElementById("linkHref").href = response.link
        document.getElementById("intro").innerHTML = response.intro
        initMap = function initMap(latitude, longitude) {          
            // The location of address
            var position_marqueur = {
                lat:latitude , lng:longitude
            };
            // The map, centered at address
            var map = new google.maps.Map(
                document.getElementById('map'), {
                    zoom: 10,
                    center: position_marqueur
                }
            );
            // The marker, positioned at address
            var marker = new google.maps.Marker({
                position: position_marqueur,
                map: map
            });             
        }; 
        document.getElementById("map").innerHTML = ""
        if (response.lat !== 0 && response.lng !== 0 ){
           initMap(response.lat, response.lng)
        }        
    } 
    else {
      alert('Il y a eu un problème avec la requête.');
    }
  }
}            
