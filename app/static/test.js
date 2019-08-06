// adding the new chat buble text ! 
document.getElementById("ajaxButton").onclick = function() {

    // USER INPUT
    var userInput = document.getElementById("ajaxTextbox").value;

    // NEW BUBBLE 
    var msgDiv = document.createElement("div");
    msgDiv.classList.add("msg");
    document.getElementById("chat").appendChild(msgDiv);

    var bubbleAltDiv = document.createElement("div");
    bubbleAltDiv.className = "bubble alt";
    msgDiv.appendChild(bubbleAltDiv);

    var txtDiv = document.createElement("div");
    txtDiv.classList.add("txt");
    bubbleAltDiv.appendChild(txtDiv);

    var meSpan = document.createElement("span");
    meSpan.className = "name alt";
    txtDiv.appendChild(meSpan);
    meSpan.innerHTML = "Moi"

    var timeSpan = document.createElement("span");
    timeSpan.classList.add("timestamp");
    txtDiv.appendChild(timeSpan);
    timeSpan.innerHTML = "10:44 pm"

    var messP = document.createElement("p");
    messP.classList.add("message");
    txtDiv.appendChild(messP);
    messP.innerHTML = userInput; 

    // CLEAR INPUT
    document.getElementById("ajaxTextbox").value = "";
}
// resizing the textarea
jQuery.each(jQuery('textarea[data-autoresize]'), function() {
  var offset = this.offsetHeight - this.clientHeight;
 
  var resizeTextarea = function(el) {
    jQuery(el).css('height', 'auto').css('height', el.scrollHeight + offset);
  };
  jQuery(this).on('keyup input', function() { resizeTextarea(this); }).removeAttr('data-autoresize');
});



    