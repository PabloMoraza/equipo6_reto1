const API_URL = "http://127.0.0.1:8000/aplicacion/proveedores_api/"

fetch(API_URL)
    .then(response => response.json())
    .then(json => {
        addRows(json);
    });

function addRows(proveedores) {
    tbody = document.getElementById("tbody");
    proveedores.forEach(element => {
        tbody.appendChild(createProveedorRow(element))

    });
}
function createProveedorRow(proveedor) {
    let row = document.createElement("tr")

    let nombre = document.createElement("td")
        nombre.textContent = proveedor.nombre;
        row.appendChild(nombre);

    let telefono = document.createElement("td");
        telefono.textContent = proveedor.telefono;
        row.appendChild(telefono);

    let enlace_cosas = document.createElement("td")
    let enlace = document.createElement("a")
        enlace.setAttribute("href", "http://127.0.0.1:8000/aplicacion/proveedores/" + proveedor.id)
        enlace.innerHTML = "Ver detalles"
        enlace.className = "enlace"
        enlace_cosas.appendChild(enlace);
        row.appendChild(enlace_cosas);
    return row;
}