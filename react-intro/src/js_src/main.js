function append(form) {
    if (form.input.value) {
       var newItem = document.createElement("LI");
       newItem.appendChild(document.createTextNode(form.input.value));
       document.getElementById("myUL").appendChild(newItem);
    }
 }
 
 function replace(form) {
    if (form.input.value) {
       var newItem = document.createElement("LI");
       var lastChild = document.getElementById("myUL").lastChild;
       newItem.appendChild(document.createTextNode(form.input.value));
       document.getElementById("myUL").replaceChild(newItem, lastChild);
    }
 }
 
 function restore() {
    var oneChild;
    var mainObj = document.getElementById("myUL");
    while (mainObj.childNodes.length > 2) {
       oneChild = mainObj.lastChild;
       mainObj.removeChild(oneChild);
    }
 }