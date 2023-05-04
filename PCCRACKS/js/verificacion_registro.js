$(document).ready(function(){
    $("#register").submit(function(e){
        e.preventDefault();
        var nombre = $("#name").val();
        var correo = $("#number").val();
        var correo = $("#email").val();
        var correo = $("#password").val();


        let msjMostrar = "";
        let enviar = false;

        if(nombre.trim().lenght < 5 || nombre.trim().lenght > 10){
            msjMostrar += "El nombre debe tener entre 5 y 10 caracteres";
        }

        
        var letra = nombre.trim().charAt(0);
        if(!esMayuscula(letra)){
        msjMostrar += "<br>La primera letra debe ser mayúscula";
        enviar = true;
        }

        if(enviar){
            $("#warnings").html(msjMostrar)
        }
        else{
            $("#warnings").html("Cuenta creada correctamente")
        }

        function esMayuscula(letra){
            if(letra == letra.toUpperCase()){
                return true;
            }
            else{
                return false;
            }
    
    }
});

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   


});