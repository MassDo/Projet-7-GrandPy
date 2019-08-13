var httpRequest;
var responseZone = document.querySelector(".response");

// ACTION WHEN SUBMIT
document.getElementById("ajaxButton").onclick = function() {
    var textarea = document.getElementById("ajaxTextbox")
    var userInput = textarea.value;
    var text = userInput;
    // user new bubble chat
    bubble(userInput, responseZone, textarea);
    // ajax request
    makeRequest('/home', text, responseZone); 
};

// ADD USER CHAT BUBBLE
function bubble(userInput, responseZone, textarea) {
    // NEW USER CHAT BUBBLE (if userInput not empty)
    if (userInput != "") {
        var zone = document.createElement("div");
        zone.classList.add("zone");
        responseZone.insertAdjacentElement("beforeend", zone);
        var bubble = document.createElement("div");
        bubble.className = "bubble user";
        bubble.innerHTML = userInput;
        zone.appendChild(bubble);
    }
    // SCROLL DOWN
    responseZone.scrollTop = responseZone.scrollHeight;
    // CLEAR TEXTAREA
    textarea.value = "";    
    // restart userInput height
    textarea.style.height = "15px";
}
// AJAX REQUEST
function makeRequest(url, text) {
    httpRequest = new XMLHttpRequest();     
    if (!httpRequest) {
        alert('Abandon :( Impossible de créer une instance de XMLHTTP');
        return false;
    }
    httpRequest.onreadystatechange = callBack; // callback function
    httpRequest.open('POST', url);
    httpRequest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    httpRequest.send('userInput=' + encodeURIComponent(text));
}
// AJAX CALLBACK 
function callBack() {
    if (httpRequest.readyState === XMLHttpRequest.DONE) { // if request is done
        if (httpRequest.status === 200) { // if the ressource is find
            var response = JSON.parse(httpRequest.responseText) // transform a json into a JS object
/*            newMap(responseZone);*/
            // remplir les cases ICI
            /*document.getElementById("address").innerHTML = response.address
            document.getElementById("title").innerHTML = response.title
            document.getElementById("link").innerHTML = response.link
            document.getElementById("linkHref").href = response.link
            document.getElementById("intro").innerHTML = response.intro*/
            initMap = function initMap(latitude, longitude) {          
                // The location of address
                var position_marqueur = {
                    lat:latitude , lng:longitude
                };
                // The map, centered at address
                let mapClassNodeList = document.querySelectorAll(".map")
                let lastMap = mapClassNodeList[mapClassNodeList.length - 1];
                var map = new google.maps.Map(
                    lastMap, {
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
            
            /*document.getElementById("map").innerHTML = ""*/
            if (response.lat !== 0 && response.lng !== 0 ){
                newMap(responseZone);
                initMap(response.lat, response.lng)
            }        
        } 
        else {
          alert('Il y a eu un problème avec la requête.');
        }
    }
    // SCROLL DOWN
    var responseZone = document.querySelector(".response");
    responseZone.scrollTop = responseZone.scrollHeight;
} 
// NEW MAP
function newMap() {
    var zone = document.createElement("div");
    zone.classList.add("zone");
    responseZone.insertAdjacentElement("beforeend", zone);
    var bubble = document.createElement("div");
    bubble.className = "bubble bot map";
    zone.appendChild(bubble);
}
// Adapt text area window size to his content
function textAreaAdjust(o) { 
    o.style.height = "0px";      
    console.log(o.style.height);
    o.style.height = (o.scrollHeight)+"px";
}           
