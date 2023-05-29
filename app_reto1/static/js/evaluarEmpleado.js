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

function evaluarEmpleado() {
    // console.log("a");
    let DNI = document.getElementById("id_DNI").value;
    let nombre = document.getElementById("id_nombre").value;
    let apell1 = document.getElementById("id_apellido1").value;
    let apell2 = document.getElementById("id_apellido2").value;
    let email = document.getElementById("id_email").value;
    let telefono = document.getElementById("id_telefono").value;

    if (estavacio(DNI)==1){
        alert(" El DNI esta vacio");
    }
    if (estavacio(nombre)==1){
        alert(" El Nombre esta vacio")
    }
    if (estavacio(apell1)==1){
        alert(" El Primer apellido esta vacio")
    }
    if (estavacio(email)==1){
        alert(" El Email esta vacio");
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
function generarEmail(){
    document.getElementById("id_email").value = "";
    let nombre = document.getElementById("id_nombre").value;
    let apell1 = document.getElementById("id_apellido1").value;
    let apell2 = document.getElementById("id_apellido2").value;
    if(estavacio(apell2)==1){
        document.getElementById("id_email").value = nombre + "." + apell1 + "@deustomach.com"
    }else{
        document.getElementById("id_email").value = nombre + "." + apell1 + "-" + apell2 + "@deustomach.com"
    }
}

let formEmpleado = document.getElementById('checkEmpleado');
formEmpleado.addEventListener('click', evaluarEmpleado);
let gemail = document.getElementById('generaremail');
gemail.addEventListener('click', generarEmail); 