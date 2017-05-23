function errorGetProgress(response) {
    alertify.error("Error al obtener información del proyecto");
}

function showProyectsNames(response){
    var nameProyectList =$("#projects");
    var project;
    nameProyectList.append(new Option("Seleccione un proyecto", -1));
    for (var i=0; i <response.length; i++){
        project = response[i];
        nameProyectList.append(new Option(project.fields.nombre, project.pk));
    }
 }

 function getDates(data) {
    var dates = [];
    for(i =0; i<data.length;i++)
    {
     dates[i] = data[i].fecha;
    }
    return dates;
}

  function getListProgress(data) {
    var progressList = [];
    for(i =0; i<data.length;i++)
    {
     progressList[i] = data[i].reporte;
    }
    return progressList;
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

function paintChartProgress(data) {
    var project= $("#projects option:selected").text();
    Highcharts.chart("progressChart", {
        chart: {
            type: "line"
        },
        title: {
            text: "Avance del proyecto "+ project
        },
        xAxis: {
            categories: getDates(data)
        },
        yAxis: {
            title: {
                text: "% de avance"
            }
        },
        plotOptions: {
            line: {
                dataLabels: {
                    enabled: true
                },
                enableMouseTracking: false
            }
        },
        series: [{
            name:"avance",
            data: getListProgress(data)
        }]
    });
}

 function listProgress(urlListProgress){

     $.ajax({
        url:host+urlListProgress,
        method:"GET",
        success:function(response){
            paintTableProgress(response);
            paintChartProgress(response);
        },
        error:errorGetProgress,
        async:true,
        crossDomain:true
    });
}
 function paintChart(urlListProgress) {
     var idProject= $('#projects option:selected').val();
     if(idProject === undefined || idProject == -1) {
         alertify.error("Seleccione un proyecto para poder generar la gráfica de avance.");
         return;
     }
     urlListProgress +="?id="+idProject+'&orderBy=ASC';
     listProgress(urlListProgress);
 }






