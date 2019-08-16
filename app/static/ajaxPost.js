var httpRequest;
var responseZone = document.querySelector(".response");

// ACTION WHEN SUBMIT
document.getElementById("ajaxButton").onclick = function() {
    var textarea = document.getElementById("ajaxTextbox")
    var userInput = textarea.value;
    var text = userInput;
    // user new bubble chat
    if (text != "") {
        bubble(userInput, responseZone, textarea);
        // ajax request
        makeRequest('/home', text, responseZone); 
    }
    else {
        // faire une bulle réponse du bot qui demande de saisir du texte
    }    
};

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
            var response = JSON.parse(httpRequest.responseText) // json into a JS object
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
            botResponse(response);
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

/*FUNCTIONS USED*/
// add user chat bubble
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
// new map
function newMap() {
    var zone = document.createElement("div");
    zone.classList.add("zone");
    responseZone.insertAdjacentElement("beforeend", zone);
    var bubble = document.createElement("div");
    bubble.className = "bubble bot map";
    zone.appendChild(bubble);
}
// new bot response
function botResponse(response) {
    var dataList = [
        response.address,
        response.title,        
        response.intro
    ]
    for (let data of dataList) {
        if (data) {
            let info = document.createTextNode(data);
            var zone = document.createElement("div");
            if (data === response.intro) {
                responseZone.insertAdjacentElement("beforeend", zone);
                var bubble = document.createElement("div");
                zone.appendChild(bubble);
                bubble.className = "bubble bot";
                var aElt = document.createElement("a");
                bubble.appendChild(info);
                var brElt = document.createElement("br");
                bubble.appendChild(brElt);
                var brElt2 = document.createElement("br");
                bubble.appendChild(brElt2);
                bubble.appendChild(aElt);
                aElt.href = response.link;
                aElt.setAttribute("target","_blank");        
                aElt.innerHTML = response.link; 
            }
            else {
                zone.classList.add("zone");
                responseZone.insertAdjacentElement("beforeend", zone);
                var bubble = document.createElement("div");
                bubble.className = "bubble bot";
                zone.appendChild(bubble);
                bubble.appendChild(info);
            }    
        }
        else {
            console.log(data + "pas d'informations")
        }  
    }
}
// Adapting textarea window size to his content.
function textAreaAdjust(o) { 
    o.style.height = "0px";      
    console.log(o.style.height);
    o.style.height = (o.scrollHeight)+"px";
}           
