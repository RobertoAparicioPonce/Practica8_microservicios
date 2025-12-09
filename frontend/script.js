const API_USUARIOS = "http://3.145.23.235:5001/usuarios";
const API_PRODUCTOS = "http://3.145.23.235:5002/productos";
const API_PEDIDOS = "http://3.145.23.235:5003/pedidos";

async function mostrarUsuarios() {
  const res = await fetch(API_USUARIOS);
  const data = await res.json();
  mostrarTabla(data, ["id", "nombre", "correo"], "Usuarios", "usuarios");
}

async function mostrarProductos() {
  const res = await fetch(API_PRODUCTOS);
  const data = await res.json();
  mostrarTabla(data, ["id", "nombre", "precio"], "Productos", "productos");
}

async function mostrarPedidos() {
  const res = await fetch(API_PEDIDOS);
  const data = await res.json();
  mostrarTabla(data, ["id", "usuario_id", "producto_id"], "Pedidos", "pedidos");
}

function mostrarTabla(data, columnas, titulo, tipo) {
  let html = `<h2 style="text-align:center;">${titulo}</h2>`;
  html += "<table><tr>";

  columnas.forEach(col => html += `<th>${col.toUpperCase()}</th>`);
  html += "</tr>";

  data.forEach(item => {
    html += "<tr>";
    columnas.forEach(col => html += `<td>${item[col]}</td>`);
    html += "</tr>";
  });

  html += "</table>";
  html += generarFormulario(tipo);

  document.getElementById("tabla").innerHTML = html;
}

function generarFormulario(tipo) {
  let campos = "";

  if (tipo === "usuarios") {
    campos = `
      <input id="nombre" placeholder="Nombre" />
      <input id="correo" placeholder="Correo" />
    `;
  } else if (tipo === "productos") {
    campos = `
      <input id="nombre" placeholder="Nombre del producto" />
      <input id="precio" placeholder="Precio" type="number" />
    `;
  } else if (tipo === "pedidos") {
    campos = `
      <input id="usuario_id" placeholder="ID Usuario" type="number" />
      <input id="producto_id" placeholder="ID Producto" type="number" />
    `;
  }

  return `
    <form onsubmit="agregarElemento(event, '${tipo}')">
      ${campos}
      <button type="submit">Agregar</button>
    </form>
  `;
}

async function agregarElemento(event, tipo) {
  event.preventDefault();

  const datos = {};
  document.querySelectorAll("form input").forEach(input => {
    datos[input.id] = input.value;
  });

  let url = "";
  if (tipo === "usuarios") url = API_USUARIOS;
  if (tipo === "productos") url = API_PRODUCTOS;
  if (tipo === "pedidos") url = API_PEDIDOS;

  await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos)
  });

  if (tipo === "usuarios") mostrarUsuarios();
  if (tipo === "productos") mostrarProductos();
  if (tipo === "pedidos") mostrarPedidos();
}
