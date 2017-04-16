function showProyectsNames(response){
    var nameProyectList =$("#projects");
    var project;
    nameProyectList.append(new Option("Seleccione un proyecto", -1));
    for (var i=0; i <response.length; i++){
        project = response[i];
        nameProyectList.append(new Option(project.fields.nombre, project.pk));
    }
 }

 function paintChart(urlListProgress) {
     var idProject= $('#projects option:selected').val();
     if(idProject === undefined || idProject == -1) {
         alertify.error("Seleccione un proyecto para poder generar la gráfica de avance.");
         return;
     }
     urlListProgress +="?id="+idProject;
     listProgress(urlListProgress);
 }

 function listProgress(urlListProgress){

     $.ajax({
        url:host+urlListProgress,
        method:"GET",
        success:function(response){paintTableProgress(response);},
        error:errorGetProgress,
        async:true,
        crossDomain:true
    });
}

function errorGetProgress(response) {
    alertify.error("Error al obtener información del proyecto");
}

function  paintTableProgress(data) {
    $('#listProgress').removeAttr("hidden");

    var table = $('#listReportedProgress');
    table.DataTable().destroy();
    table.DataTable({
        searching:false,
        data: data,
        columns: [
            { data: "fecha" },
            { data: "reporte" },
            { data: "comentario" }
        ]
    });
}
