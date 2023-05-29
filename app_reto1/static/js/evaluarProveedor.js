function estavacio(valor) {
    // El numero de serie esta vacio
    if (valor === "") {
        return 1;
    }
}
function noesnumero(valor) {
    // El numero no es un numero
    if (isNaN(valor)) {
        return 1;
    }
}

function menorque0(valor) {
    // El numero es menor que 0
    if (valor < 0) {
        return 1;
    }
}
function evaluarProveedor(){
    let nombre = document.getElementById("id_nombre").value;
    let telefono = document.getElementById("id_telefono").value;
    if (estavacio(nombre)==1){
        alert(" El Nombre esta vacio")
    }
    if (estavacio(telefono)==1){
        alert(" El telefono esta vacio");
    }
    if (noesnumero(telefono)==1){
        alert(" El telefono no es un numero");
    }
    if (menorque0(telefono)==1){
        alert(" El telefono es menor que 0");
    }
}



let formProveedor = document.getElementById('checkProveedor');
formProveedor.addEventListener('click', evaluarProveedor);