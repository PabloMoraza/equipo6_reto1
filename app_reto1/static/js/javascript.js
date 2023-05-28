// alert("existo")

function getFontSize(){
let tamano =  document.getElementsByClassName("tamano").fontSizetamanos

    return tamano
}
function aumentar(){
    console.log(getFontSize());
}
let elem = document.getElementById('aumentar');
elem.addEventListener('click', aumentar);