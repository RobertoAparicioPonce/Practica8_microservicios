async function mostrarUsuarios() {
  const res = await fetch("http://localhost:8001/usuarios");
  const data = await res.json();
  mostrarTabla(data, ["id", "nombre", "correo"], "Usuarios");
}

async function mostrarProductos() {
  const res = await fetch("http://localhost:8002/productos");
  const data = await res.json();
  mostrarTabla(data, ["id", "nombre", "precio"], "Productos");
}

async function mostrarPedidos() {
  const res = await fetch("http://localhost:8003/pedidos");
  const data = await res.json();
  mostrarTabla(data, ["id", "usuario_id", "producto_id"], "Pedidos");
}

function mostrarTabla(data, columnas, titulo) {
  let html = `<h2 style="text-align:center;">${titulo}</h2>`;
  html += "<table><tr>";
  columnas.forEach((col) => (html += `<th>${col.toUpperCase()}</th>`));
  html += "</tr>";

  data.forEach((item) => {
    html += "<tr>";
    columnas.forEach((col) => (html += `<td>${item[col]}</td>`));
    html += "</tr>";
  });
  html += "</table>";

  document.getElementById("tabla").innerHTML = html;
}
