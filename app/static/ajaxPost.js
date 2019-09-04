/*Function used*/

// remove function
Element.prototype.remove = function() {
    this.parentElement.removeChild(this);
}
NodeList.prototype.remove = HTMLCollection.prototype.remove = function() {
    for(var i = this.length - 1; i >= 0; i--) {
        if(this[i] && this[i].parentElement) {
            this[i].parentElement.removeChild(this[i]);
        }
    }
}
// AJAX REQUEST
function makeRequest(url, text, responseZone) {
    return new Promise((resolve, reject) => {
        httpRequest = new XMLHttpRequest();     
        if (!httpRequest) {
            alert('Abandon :( Impossible de créer une instance de XMLHTTP');
            return false;
        }
        httpRequest.onreadystatechange = function() {
            if (httpRequest.readyState === XMLHttpRequest.DONE) { // if request is done
                if (httpRequest.status === 200) { // if the ressource is find
                    resolve(httpRequest)
                }else {
                    reject(httpRequest)
                }
            }else {
                reject(httpRequest)
            }
        }
        httpRequest.open('POST', url);
        httpRequest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        httpRequest.send('userInput=' + encodeURIComponent(text)); 
    })    
}
// AJAX CALLBACK 
function callBack(httpRequest) {
    var response = JSON.parse(httpRequest.responseText); // json into a JS object
    var initMap = function (latitude, longitude) {          
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
    botResponse(response);
    if (response.lat !== 0 && response.lng !== 0 ){
        newMap(responseZone);
        initMap(response.lat, response.lng)
    }        
    // SCROLL DOWN
    var responseZone = document.querySelector(".response");
    responseZone.scrollTop = responseZone.scrollHeight;
} 
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
                let title = document.createTextNode(
                    "Voila voila..." + response.title + ". ");
                bubble.appendChild(title);
                bubble.appendChild(info);                
            }    
        }
        else {
            console.log(data + "pas d'informations")
        }  
    }
}
// Adapting textarea window size to his content.
function textAreaAdjust(e) { 
    e.style.height = "0px";      
    e.style.height = (e.scrollHeight)+"px";
}
function runScript(e) {
    //See notes about 'which' and 'key'
    if (e.keyCode == 13) {
        var tb = document.getElementById("ajaxButton");
        eval(tb.value);
        return false;
    }
}
// LOADER during ajax request
function load() {
    let body = document.querySelector("body")
    // loader creation
    let loader = document.createElement("div")
    loader.className = "loader"
    // rajouter la div id loader au milieu de la fenetre
    let box = document.createElement("div")
    box.id = "loader"
    let divElt = document.createElement("div")
    box.appendChild(divElt)
    loader.appendChild(box)
    body.appendChild(loader)
}
// SEARCH (lauching the ajax and loader)
function search(loader_function) {
    var textarea = document.getElementById("ajaxTextbox")
    var userInput = textarea.value
    var text = userInput    
    // user new bubble chat if there is text
    if ((text != "") && (text.replace(/\s/g, '').length)) {
        bubble(userInput, responseZone, textarea)
        loader_function();
        // ajax request
        makeRequest('/', text, responseZone)
        .then((response) => {
            callBack(response);
            var loader = document.getElementsByClassName("loader")
            loader.remove();
        })
        .catch((response) => {
            var loader = document.getElementsByClassName("loader")
            loader.remove();
        });
    }
    else {
        // faire une bulle réponse du bot qui demande de saisir du texte
    }   
}
// ACTION WHEN CLICKING ON SUBMIT OR ENTER
var httpRequest;
var responseZone = document.querySelector(".response")
var validation = document.getElementById("ajaxButton")

validation.onclick = () => {
    search(load); 
}
document.addEventListener("keydown", function(e) {
    if (e.code === 'Enter') {
        search(load);   
    }
})




