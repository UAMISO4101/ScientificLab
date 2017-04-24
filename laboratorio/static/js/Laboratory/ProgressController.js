function listProgress(urlListProgress){
     $.ajax({
        url:host+urlListProgress,
        method:"GET",
        success:function(response){paintProgress(response);},
        error:errorGetProgress,
        async:true,
        crossDomain:true
    });
}

function errorGetProgress(response) {
    console.log(response);
}

function  paintProgress(data) {
      $('#listReportedProgress').DataTable({
        data: data,
        searching:false,
        columns: [
            { data: "fecha" },
            { data: "reporte" },
            { data: "comentario" }
        ]
        });
}

function saveProgress(idProject) {
    var progress = $("#projectProgress").val();
    if(progress>100 || progress<0) {
        alertify.error("El avance debe ser entre 0% y 100%", 2);
        return;
    }

    var url = $("#formProgress").attr("data-add-progress-url");
    $.ajax({
            url: host+url,
        method:"POST",
        data:getData(idProject),
        success:sucessSaveProgress,
        error:errorSaveProgress,
        dataType: "json"
    });
}

function getData(projectId) {
    var progress = {};
    progress.projectId = projectId;
    progress.date =$("#currentDate").val();
    progress.progress =$("#projectProgress").val();
    progress.comment =$("#comment").val();
    return progress;
}

function sucessSaveProgress() {
    alertify.success("El avance se ha guardado correctamente");
}

function errorSaveProgress() {
    alertify.error("Error al guardar el avance del proyecto");

}