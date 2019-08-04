// adding the new chat buble text ! 
document.getElementById("ajaxButton").onclick = function() {
    var userInput = document.getElementById("ajaxTextbox").value;
    // création of a new div in div chatZone
    var newDiv = document.createElement("div");  
    // adding user text
    newDiv.innerHTML = userInput;
    // append this new div into the div 'chatZone'
    document.getElementById("chatZone").appendChild(newDiv)    
    // suppression of the text into id="ajaxTextbox"
    document.getElementById("ajaxTextbox").value = ""    
}



    