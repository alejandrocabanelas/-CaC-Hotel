const ingresar = document.querySelector('.bnt-a')
const enviar = document.querySelector('.btnenviar');
const nombre = document.querySelector('.impNombre');
const apellido = document.querySelector('.impApellido');
const fechaNacimiento = document.querySelector('.impFecha');
const usuario = document.querySelector('.impUsuario');
const mail = document.querySelector('.impMail');
const contraseña = document.querySelector('.impContraseña');
const mensajeExito = document.querySelector('.mensajeExito');

// Función para mostrar un mensaje de error
const mostrarError = (campo, mensaje) => {
  campo.classList.remove('input-success');
  campo.classList.add('input-error');
  const errorMensaje = campo.nextElementSibling;
  errorMensaje.innerText = mensaje;
  errorMensaje.style.display = 'block';
};

// Función para mostrar un mensaje de éxito
const mostrarExito = (campo) => {
  campo.classList.remove('input-error');
  campo.classList.add('input-success');
  const errorMensaje = campo.nextElementSibling;
  errorMensaje.innerText = '';
  errorMensaje.style.display = 'none';
};

enviar.addEventListener('click', (event) => {
  event.preventDefault();

  let hayErrores = false;

  // Validaciones
  const nombreValue = nombre.value.trim();
  const apellidoValue = apellido.value.trim();
  const fechaNacimientoValue = fechaNacimiento.value.trim();
  const usuarioValue = usuario.value.trim();
  const mailValue = mail.value.trim();
  const contraseñaValue = contraseña.value.trim();

  // Estilos de los campos de entrada
  nombre.style.borderColor = '#ccc';
  nombre.style.backgroundColor = '#f4f4f4';
  apellido.style.borderColor = '#ccc';
  apellido.style.backgroundColor = '#f4f4f4';
  fechaNacimiento.style.borderColor = '#ccc';
  fechaNacimiento.style.backgroundColor = '#f4f4f4';
  usuario.style.borderColor = '#ccc';
  usuario.style.backgroundColor = '#f4f4f4';
  mail.style.borderColor = '#ccc';
  mail.style.backgroundColor = '#f4f4f4';
  contraseña.style.borderColor = '#ccc';
  contraseña.style.backgroundColor = '#f4f4f4';

  // Validación del nombre
  if (nombreValue === !/^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$/.test(nombreValue)) {
    mostrarError(nombre, "No use numeros ni caracteres especiales");
    hayErrores = true;
  } else {
    mostrarExito(nombre);
  }

  // Validación del apellido
  if (apellidoValue === !/^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$/.test(apellidoValue)) {
    mostrarError(apellido, "No use numeros ni caracteres especiales");
    hayErrores = true;
  } else {
    mostrarExito(apellido);
  }

  // Validación de la fecha de nacimiento
  const fechaNacimientoDate = new Date(fechaNacimientoValue);
  if ((fechaNacimientoDate.getTime())) {
    mostrarError(fechaNacimiento, "Complete este campo");
    hayErrores = true;
  } else {
    mostrarExito(fechaNacimiento);
  }

  // Validación del usuario
  if (usuarioValue === /^\d+$/.test(usuarioValue) || /[^\w\s]/.test(usuarioValue)) {
    mostrarError(usuario, "No use caracteres especiales");
    hayErrores = true;
  } else {
    mostrarExito(usuario);
  }  

  // Validación del correo electrónico
  if (mailValue === !/^\S+@\S+\.\S+$/.test(mailValue)) {
    mostrarError(mail, "Ingrese un mail valido");
    hayErrores = true;
  } else {
    mostrarExito(mail);
  }

  // Validación de la contraseña
  if (contraseñaValue === contraseñaValue.length < 8 || /[^a-zA-Z0-9]/.test(contraseñaValue)) {
    mostrarError(contraseña, "Contraseña de al menos 8 digitos");
    hayErrores = true;
  } else {
    mostrarExito(contraseña);
  }

  if (!hayErrores) {
    mensajeExito.innerText = "✅ Sus datos fueron modificados"
    enviar.style.display = 'none';
    ingresar.style.display = 'block';
}
});
