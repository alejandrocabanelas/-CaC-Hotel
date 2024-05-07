const ham = document.querySelector(".ham");
const lista = document.querySelector("nav ul");
const barras = document.querySelectorAll(".ham span");

// Funcion de modificacion al hacer click
ham.addEventListener("click", () => {
  lista.classList.toggle("activado");
  barras.forEach((child) => {
    child.classList.toggle("animado");
  });
});
