function showProyectsNames(response){
    var nameProyectList =$("#projects");
    var project;
    nameProyectList.append(new Option("Seleccione un proyecto", -1));
    for (var i=0; i <response.length; i++){
        project = response[i];
        nameProyectList.append(new Option(project.fields.nombre, project.pk));
    }
 }
 function paintTraza(urlProyectMembers, urlProyectProto, urlProyectExpe) {
     var idProject= $('#projects option:selected').val();
     if(idProject === undefined || idProject === -1) {
         alertify.error("Seleccione un proyecto para presentar el informe");
         return;
     }
     urlProyectMembers +="?id="+idProject;
     listIntegrantes(urlProyectMembers);

     urlProyectProto +="?id="+idProject;
     listProto(urlProyectProto);

     urlProyectExpe +="?id="+idProject;
     listExperimentos(urlProyectExpe);

     avance();
}

 function listIntegrantes(urlProyectMembers){
     $.ajax({
        url:host+urlProyectMembers,
        method:"GET",
        success:function(response){
            participacion(response);
        },
        error:errorGetProgress,
        async:true,
        crossDomain:true
    });
}

 function listProto(urlProyectProto){
     $.ajax({
        url:host+urlProyectProto,
        method:"GET",
        success:function(response){
            protocolos(response);
        },
        error:errorGetProgress,
        async:true,
        crossDomain:true
    });
}

 function listExperimentos(urlProyectProto){
     $.ajax({
        url:host+urlProyectProto,
        method:"GET",
        success:function(response){
            experimentos(response);
        },
        error:errorGetProgress,
        async:true,
        crossDomain:true
    });
}
 function getMembers(data) {
    var members = [];
    var registro = new Object();
    for(i =0; i<data.length;i++)
    {
        var pos = -1;
        for (j=0; j<members.length;j++)
        {
            registro = members[j];
            if(registro.name=== data[i].nombre)
            {
                pos = j;
                break;
            }
        }
        if(pos>=0) { // Existe en el arreglo
            registro.y++;
            members[j]= registro;
        }
        else{
            registro = new Object();
            registro.name = data[i].nombre;
            registro.y = 1;
            members[i]= registro;
        }
    }
    return members;
}

function getProto(data){
    var proto = [];
    var ejecutado = new Object();
    var pendiente = new Object();
    ejecutado.name = "Ejecutado";
    ejecutado.y=0;
    pendiente.name="Pendiente";
    pendiente.y=0;
    for(i =0; i<data.length;i++)
    {
        if(data[i].resultado===0)
        {
            ejecutado.y++;
        }
        if(data[i].resultado===1)
        {
            pendiente.y++;
        }
    }
    proto[0]= ejecutado;
    proto[1]= pendiente;
    return proto;
}

function getExpe(data){
    var expe = [];
    var ejecutado = new Object();
    var pendiente = new Object();
    ejecutado.name = "Ejecutado";
    ejecutado.y=0;
    pendiente.name="Pendiente";
    pendiente.y=0;
    for(i =0; i<data.length;i++)
    {
        if(data[i].resultado===0)
        {
            ejecutado.y++;
        }
        if(data[i].resultado===1)
        {
            pendiente.y++;
        }
    }
    expe[0]= ejecutado;
    expe[1]= pendiente;
    return expe;
}

function errorGetProgress(response) {
    alertify.error("Error al obtener información del proyecto");
}

var project = $("#projects option:selected").text();
 Highcharts.setOptions({
    colors: [ '#058DC7', '#50B432', '#ED561B', '#DDDF00', '#24CBE5','#64E572', '#FF9655', '#FFF263']
});

function avance(data){
     Highcharts.chart("AvanceChart", {
        chart: {
            backgroundColor: '#eee',
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {text: "Avance del proyecto "+ project},
        tooltip: {pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'},
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: false,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                },
                connectorColor: 'silver'
                },
                showInLegend: true
            }
        },
        series: [{
            name: 'Brands',
            colorByPoint: true,
            data: [{
                name: 'Ejecutado', y: 56.33}, {
                name: 'Pendiente', y: 43.67}]
            }]
    });
 }
     function experimentos(data) {
    var expe = []
    expe = getExpe(data);
     Highcharts.chart("ExperimentosChart", {
        chart: {
            backgroundColor: '#eee',
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie',
        },
        title: {text: "Experimentos ejecutados"},
        tooltip: {pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'},
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: false,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                },
                connectorColor: 'silver'
                },
                showInLegend: true
            }
        },
        series: [{
            name: 'Brands',
            colorByPoint: true,
            data: expe
            }]
    });
     }
function protocolos(data) {
    var proto = []
    proto = getProto(data);
     Highcharts.chart("ProtocolosChart", {
        chart: {
            backgroundColor: '#eee',
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie',
        },
        title: {text: "Protocolos realizados"},
        tooltip: {pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'},
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: false,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                },
                connectorColor: 'silver'
                },
                showInLegend: true
            }
        },
        series: [{
            name: 'Brands',
            colorByPoint: true,
            data: proto
            }]
    });
     }
function participacion(data) {
    var members = []
    members = getMembers(data);
     Highcharts.chart("ParticipantesChart", {
        chart: {
            backgroundColor: '#eee',
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie',
        },
        title: {text: "Participación de los integrantes"},
        tooltip: {pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'},
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: false,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                },
                connectorColor: 'silver'
                },
                showInLegend: true
            }
        },
        series: [{
            name: 'Brands',
            colorByPoint: true,
            data: members
            }]
    });
     }



