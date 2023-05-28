// alert("existo")

function aumentar(){
    var el = document.getElementById('tamanos');
    var style = window.getComputedStyle(el, null).getPropertyValue('font-size');
    var fontSize = parseFloat(style); 
    el.style.fontSize = (fontSize + 1) + 'px';
}
function disminuir(){
    var el = document.getElementById('tamanos');
    var style = window.getComputedStyle(el, null).getPropertyValue('font-size');
    var fontSize = parseFloat(style); 
    el.style.fontSize = (fontSize - 1) + 'px';
}
let elem1 = document.getElementById('aumentar');
elem1.addEventListener('click', aumentar);
let elem2 = document.getElementById('disminuir');
elem2.addEventListener('click', disminuir);