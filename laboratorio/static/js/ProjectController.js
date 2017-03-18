// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue =   decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function saveProject(){
    var project = {};
    project.nombre = $("#title").val();
    project.fechaInicio = $("#startDate").val();
    project.fechaFinal = $("#endDate").val();
    project.avance = $("#percentageCompletion").val();
    project.prioridad = $("#priority").val();
    project.descripcion = $("#description").val();
    project.estado = 'Iniciado';
    project.idPatrocinador = 1;

     var url = $("form").attr("data-create-project-url");

   var csrftoken = getCookie('csrftoken');
   $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

     $.ajax({
      type: 'POST',
      url:  url,
      data: project,//JSON.stringify(project),
      success: responseSaveProject,
      error: errorSaveProject,
      dataType: 'json',
      contentType: "application/json; charset=utf-8",
    });

}

function responseSaveProject(response) {
    alert("el proyecto se guardó")
}

function errorSaveProject(e) {
    var i=0;
}