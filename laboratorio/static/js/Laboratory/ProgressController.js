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

     $("#countProjectReportedProgress").html("<input type=\"label\" id=\"counterProgress\" disabled value=\""+data.length+"\" hidden>");
      $('#listReportedProgress').DataTable({
        data: data,
        columns: [
            { data: "fecha" },
            { data: "reporte" },
            { data: "comentario" }
        ]
        });
}