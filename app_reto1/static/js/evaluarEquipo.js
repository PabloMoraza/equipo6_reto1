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



function evaluarEquipo() {
    // console.log("a");
    let nserie = document.getElementById("id_num_serie").value;
    let marca = document.getElementById("id_marca").value;
    let modelo = document.getElementById("id_modelo").value;
    let tipo = document.getElementById("id_tipo_equipo").value;
    let fechaadq = document.getElementById("id_fecha_adquisicion").value;
    let fechapue = document.getElementById("id_fecha_puesta_marcha").value;
    let prov = document.getElementById("id_proveedor").value;
    let planta = document.getElementById("id_planta").value;

    if (estavacio(nserie)==1){
        alert(" El numero de serie esta vacio");
    }
    if (noesnumero(nserie)==1){
        alert(" El numero no es un numero")
    }
    if (menorque0(nserie)==1){
        alert(" El numero es menor que 0")
    }
    if (estavacio(marca)==1){
        alert(" La marca esta vacio");
    }
    if (estavacio(modelo)==1){
        alert(" El modelo esta vacio");
    }     
    if (estavacio(tipo)==1){
        alert(" El tipo esta vacio");
    }
    if (estavacio(fechaadq)==1){
        alert(" Fecha adquisicion no seleccionada");
    }
    if (estavacio(fechapue)==1){
        alert(" Fecha puesta en marcha no seleccionada");
    }
    if (estavacio(prov)==1){
        alert(" Proveedor no seleccionado");
    }
    if (estavacio(planta)==1){
        alert(" Planta no seleccionada");
    }
    }


let formEquipo = document.getElementById('CheckEquipo');
formEquipo.addEventListener('click', evaluarEquipo);