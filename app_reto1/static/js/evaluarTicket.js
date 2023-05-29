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
function evaluarTicket(){
    let equipo = document.getElementById("id_equipo_a_reparar").value;
    let nref = document.getElementById("id_num_referencia").value;
    let descrip = document.getElementById("id_descripcion").value;
    let detalles = document.getElementById("id_detalles").value;
    let Fape = document.getElementById("id_fecha_apertura").value;
    let Freso = document.getElementById("id_fecha_resolucion").value;
    let urgencia = document.getElementById("id_urgencia").value;
    let tipo = document.getElementById("id_tipo_ticket").value;
    let estado = document.getElementById("id_estado_ticket").value;
    let empleado = document.getElementById("id_empleado_asignado").value;
    let comentarios = document.getElementById("id_comentarios_ticket").value;
    if (estavacio(equipo)==1){
        alert(" El Empleado no se ha seleccionado")
    }
    if (estavacio(nref)==1){
        alert(" El Numero de referencia esta vacio");
    }
    if (noesnumero(nref)==1){
        alert(" El Numero de referencia no es un numero");
    }
    if (menorque0(nref)==1){
        alert(" El Numero de referencia es menor que 0");
    }
    if (estavacio(descrip)==1){
        alert(" La descripcion esta vacia");
    }
    if (estavacio(detalles)==1){
        alert(" El detalle esta vacio");
    }
    if (estavacio(Fape)==1){
        alert(" La fecha de apertura esta vacio");
    }
    if (estavacio(urgencia)==1){
        alert(" La urgencia no se ha seleccionado");
    }
    if (estavacio(tipo)==1){
        alert(" El Tipo no se ha seleccionado");
    }
    if (estavacio(estado)==1){
        alert(" El Estado no se ha seleccionado");
    }
    if (estavacio(empleado)==1){
        alert(" El Empleado no se ha seleccionado");
    }

}



let formTicket = document.getElementById('checkTicket');
formTicket.addEventListener('click', evaluarTicket);