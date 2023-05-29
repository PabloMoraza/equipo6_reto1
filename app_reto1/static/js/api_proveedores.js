const API_URL = "http://127.0.0.1:8000/aplicacion/proveedores_api/"

fetch(API_URL)
    .then(response => response.json())
    .then( json => {
        addRows(json.data);
    });

    function addRows(proveedores) {
        tbody = document.getElementById("tbody");
        proveedores.forEach(element => {
            tbody.appendChild(createProveedorRow(element))

        });
    }
    function createProveedorRow(proveedor){
        let row = document.createElement("tr")
    
        let name = document.createElement("td")
            name.textContent = proveedor.nombre;
            row.appendChild(name);
    
        let lastname = document.createElement("td");
            lastname.textContent = proveedor.telefono;
            row.appendChild(lastname);
    

        return row;
    }