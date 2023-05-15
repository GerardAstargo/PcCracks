var nombre = document.getElementById("name");
var correo = document.getElementById("email");
var clave = document.getElementById("password");
var celular = document.getElementById("number");

const formulario = document.getElementById("register");


var msj = document.getElementById("warnings");

formulario.addEventListener('submit',e =>{
    let msjMostrar = "";
    let enviar = false;

    e.preventDefault();

    if(nombre.value.length < 5 || nombre.value.length > 15){
        msjMostrar = msjMostrar + "El nombre debe tener entre 5 y 15 caracteres, solo letras";
        enviar = true;
    }

    var letra = nombre.value.charAt(0);
    if(!esMayuscula(letra)){
        msjMostrar += "<br>La primera letra debe ser mayúscula";
        enviar = true;
    }

    if (celular.value.length < 8 || celular.value.length > 12){
        msjMostrar = msjMostrar + " El número debe tener los 12 digitos incluyendo el simbolo +";
        enviar = true;
    }

    if(clave.value.length < 5 || clave.value.length > 15){
        msjMostrar = msjMostrar + "La contraseña debe tener entre 5 y 15 caracteres";
        enviar = true;
    }

    if(enviar){
        msj.innerHTML = msjMostrar;
    }
    else{
        msj.innerHTML = "Cuenta creada correctamente!!";
    }

});

function esMayuscula(letra){
    if(letra == letra.toUpperCase()){
        return true;
    }
    else{
        return false;
    }
}
