// adding the new chat buble text ! 
/*document.getElementById("ajaxButton").onclick = function() {
    var userInput = document.getElementById("ajaxTextbox").value;
    // creation of a new div in div chatZone and adding css class
    var newDiv = document.createElement("div");
    newDiv.classList.add("chatBuble")
    // adding user text
    newDiv.innerHTML = userInput;
    // append this new div into the div 'chatZone'
    document.getElementById("chatZone").appendChild(newDiv)    
    // suppression of the text into id="ajaxTextbox"
    document.getElementById("ajaxTextbox").value = ""    
}*/
// resizing the textarea
jQuery.each(jQuery('textarea[data-autoresize]'), function() {
  var offset = this.offsetHeight - this.clientHeight;
 
  var resizeTextarea = function(el) {
    jQuery(el).css('height', 'auto').css('height', el.scrollHeight + offset);
  };
  jQuery(this).on('keyup input', function() { resizeTextarea(this); }).removeAttr('data-autoresize');
});



    