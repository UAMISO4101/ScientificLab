function paintLoginElements(data) {
    console.log(data)
    if (data.mensaje === 'no') {
        $("#lst_menu").hide();
        $("#cerrar_sesion").hide();
        $("#registrar_usuario").show();
        $("#iniciar_sesion").show();
        $("#usuario_sesion").hide();
        $("#nombre_usuario").text('');
    }
    else {
        $("#lst_menu").show();
        $("#cerrar_sesion").show();
        $("#registrar_usuario").hide();
        $("#iniciar_sesion").hide();
        $("#usuario_sesion").show();
        $("#nombre_usuario").text(data.mensaje);
    }
}

function showLoginElements(){
    var url = $("#iniciar_sesion").attr("is-logged-url");
    $.ajax({
        url: host+url,
        method:"GET",
        success:function(data){paintLoginElements(data);},
        error:errorPaintLoginElements,
        async:true,
        crossDomain:true
    });
}


function errorPaintLoginElements() {
        alertify.error("No es posible obtener el estado de logueo del usuario");
}

function responseSuccessLogout(data) {
    console.log(data)
    if (data.mensaje == 'ok') {
        location.reload();
    }
    else {
        alertify.error("No es posible realizar el logout");
    }
}

function doLogout(){
    var url = $("#cerrar_sesion").attr("logout-url");
    $.ajax({
        url: host+url,
        method:"GET",
        success:function(data){responseSuccessLogout(data);},
        error:errorLogout,
        async:true,
        crossDomain:true
    });
}

function errorLogout() {
        alertify.error("No es posible obtener el resultado de logout");
}

function saveUser() {
    var url = $("#formUsuario").attr("save-user-url");
    $.ajax({
        url: host+url,
        method:"POST",
        data:JSON.stringify(getData()),
        success:successSaveUser,
        error:errorSaveUser,
        dataType: "json"
    });
}

function trySaveUser() {
    if(dataUserIsCorrect()) {
        saveUser();
    }
}

function getData() {
    var user = {};
    user.username =$("#username").val();
    user.first_name =$("#first_name").val();
    user.last_name =$("#last_name").val();
    user.email =$("#email").val();
    user.password =$("#password").val();
    user.password2 =$("#password2").val();
    return user;
}

function successSaveUser(response) {
    alertify.success("El usuario se ha guardado correctamente");
}

function errorSaveUser(e){
    alertify.error("Error al guardar el usuario");
}

function dataUserIsCorrect() {

    if($("#username").val().trim() === '') {
        alertify.error("El nombre de usuario es requerido",2);
        return false;
    }

    else if($("#first_name").val().trim() === '') {
        alertify.error("Los nombres son requeridos",2);
        return false;
    }

    else if($("#last_name").val().trim() === '') {
        alertify.error("Los apellidos son requeridos",2);
        return false;
    }

    else if($("#email").val().trim() === '') {
        alertify.error("El correo electrónico es requerido",2);
        return false;
    }

    else if($("#password").val().trim() === '') {
        alertify.error("La clave es requerida",2);
        return false;
    }

    else if($("#password2").val().trim() === '') {
        alertify.error("La verificación de clave es requerida",2);
        return false;
    }

    else if($("#password").val() !== $("#password2").val()) {
        alertify.error("Las contraseñas no coinciden",2);
        return false;
    }

    else {
        return true;
    }
}

function tryLoginUser() {
    if(dataLoginIsCorrect()) {
        loginUser();
    }
}

function getDataLogin() {
    var user = {};
    user.username =$("#username").val();
    user.password =$("#password").val();
    return user;
}

function loginUser() {
    var url = $("#formLogin").attr("login-user-url");
    $.ajax({
        url: host+url,
        method:"POST",
        data:JSON.stringify(getDataLogin()),
        success:successLoginUser,
        error:errorLoginUser,
        dataType: "json"
    });
}

function successLoginUser(response) {
    if (response.mensaje == "ok")
        window.location = $("#formLogin").attr("index-url");
    else
        alertify.error(response.mensaje);
}

function errorLoginUser(e){
    alertify.error("Error al iniciar sesion el usuario");
}

function dataLoginIsCorrect() {

    if($("#username").val().trim() == '') {
        alertify.error("El nombre de usuario es requerido",2);
        return false;
    }

    if($("#password").val().trim() == '') {
        alertify.error("La clave es requerida",2);
        return false;
    }

    return true;
}

function ListUsersProject(urlListUsers) {
     $.ajax({
        url:host+urlListUsers,
        method:"GET",
        success:function(response){paintUsers(response);},
        error:errorListUsers,
        async:true,
        crossDomain:true
    });

}

function errorListUsers(response) {
        console.log(response);
}

function  paintUsers(data) {
        $('#listUserProject').DataTable({
        data: data,
        searching:false,
        columns: [
            { data: "nombre"},
            { data: "username" },
            { data: "email" },
            { data: "celular" },
            { data: "cargo" }
        ]
        });
}