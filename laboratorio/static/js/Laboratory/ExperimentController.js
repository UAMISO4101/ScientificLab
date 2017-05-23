function dataIsCorrect() {
    if($("#nombre").val().trim() === "") {
        alertify.error("El nombre es requerido",2);
        return false;
    }

    var startDate = moment($("#fechaInicio").val());
    if(startDate.isValid() ){
        var today = moment({hour:0, minutes:0});
        if(today.diff(startDate)>=0) {
            alertify.error("La fecha inicial es del pasado", 2);
            return false;
        }
    }

    if($("#responsable option:selected").val() ==="-1") {
        alertify.error("Seleccione un responsable",2);
        return false;
    }

    if($("#estado option:selected").val() === "-1") {
        alertify.error("Seleccione un estado",2);
        return false;
    }

    if($("#prioridad").val().trim() === "") {
        alertify.error("La prioridad es requerida",2);
        return false;
    }

    if($("#prioridad").val()>10 || $("#prioridad").val()<1) {
        alertify.error("La prioridad debe ser entre 1 y 10",2);
        return false;
    }

    if($("#descripcion").val().trim() === "") {
        alertify.error("La descripción es requerida",2);
        return false;
    }
    return true;
}

function successSaveExperiment(response) {
    alertify.success("El experimento se ha guardado correctamente");
}

function errorSaveExperiment(response){
    alertify.error("Error al guardar el experimento");
}

function getData() {
    var experiment = {};
    experiment.nombre =$("#nombre").val();
    experiment.fechaInicio =$("#fechaInicio").val();
    experiment.idProyecto =$('#proyecto').val();
    experiment.idResponsable =$("#responsable option:selected").val();
    experiment.estado =$("#estado option:selected").val();
    experiment.prioridad =$("#prioridad").val();
    experiment.resultado =$("#resultado option:selected").val();
    experiment.descripcion =$("#descripcion").val();
    return experiment;
}

function saveExperiment(){
    var url = $("#formAddExperiment").attr("data-add-experiment-url");
    $.ajax({
        url: host+url,
        method:"POST",
        data:getData(),
        success:successSaveExperiment,
        error:errorSaveExperiment,
        dataType: "json"
    });
}

function updateExperiment() {
    var url = $("#formEditExperiment").attr("data-edit-experiment-url");
    $.ajax({
        url: host + url,
        async:true,
        method: "PUT",
        data: JSON.stringify(getData()),
        success: successSaveExperiment,
        error: errorSaveExperiment
    });
}

function validateData(createExperiment){
    if(dataIsCorrect()) {
        if(createExperiment){
            saveExperiment();}
        else {
            updateExperiment();
        }
    }
}

function showResponsables(response){
    var responsablesList =$("#responsable");
    var responsable;
    responsablesList.append(new Option("Seleccione un responsable", -1));
    for (var i=0; i <response.length; i++){
        responsable = response[i];
        responsablesList.append(new Option(responsable.fields.nombre, responsable.pk));
    }
}

function showResultados(response){
    var resultadosList =$("#resultado");
    var resultado;
    resultadosList.append(new Option("Seleccione un resultado", -1));
    for (var i=0; i <response.length; i++){
        resultado = response[i];
        resultadosList.append(new Option(resultado.resultado, resultado.id));
    }
}

function showExperimentStates(response){
    var statesList =$("#estado");
    var state;
    statesList.append(new Option("Seleccione un estado", -1));
    for (var i=0; i <response.length; i++){
        state = response[i];
        statesList.append(new Option(state.estado, state.id));
    }
}

function setDate(date, id){
    var dateValue =moment(date).format("YYYY-MM-DD");
    $("#"+id).val(dateValue);
}

var table;
var data;


function listarExperiments(urlAll, urlEdit, urlDetails, urlVerProtocolos,urlStartExp){
    var btnEditar = "<a href='"+ urlEdit + "' class='btn btn-info btn-round' title='Editar'><span class='glyphicon glyphicon-pencil'></span></a>";
    var btnDetallar = "<a href='"+urlDetails +"'  class='btn btn-info btn-round' title='Detallar'><span class='glyphicon glyphicon-cog'></span></a>";
    var btnIniciar = "<a href='' onclick='iniciar(0, urlAll, urlEdit, urlDetails,urlStartExp)' class='btn btn-info'  title='Iniciar'>Iniciar</a>";
    var btnVerProtocolo = "<a href='"+urlVerProtocolos +"'  class='btn btn-info btn-round' title='Ver Protocolos'><span class='glyphicon glyphicon-list'></span></a>";
    var table = $('#myTable').DataTable( {
        "ajax": {
            "url":  host+urlAll,
            "dataSrc": ""
        },
        "columns": [
            { data: "nombre" },
            { data: "estado" },
            { data: "prioridad" },
            { "render": function(data, type, row, meta){
                if(row.fechaInicio == null){
                    btnIniciar= btnIniciar.replace (/0/g,row.id);

                     return btnIniciar
                    }
                    else {
                        return row.fechaInicio;
                    }
                }
            },
            { data: "proyecto" },
            { data: "responsable" },
            { data: "resultado" },
            { sortable: false,
              "render": function ( data, type, row, meta ) {
               return btnEditar.replace ("0",row.id)+
                      btnDetallar.replace ("0",row.id)+
                      btnVerProtocolo.replace("0",row.id)
                      ;
                 }
             },
        ]
        } );
}

function startExperiment(id,urlAll, urlEdit, urlDetails,urlStartExp){
    $.ajax({
        url: urlStartExp.replace("{idExp}", id),
        method:"POST",
        data:JSON.stringify({id:id}),
        success:function () {
            showAllExperiments(urlAll, urlEdit, urlDetails,urlStartExp)
        },
        error:errorSaveExperiment,
        dataType: "json"
    });
}

function iniciar(id,  urlAll, urlEdit, urlDetails,urlStartExp) {
    startExperiment(id, urlAll ,urlEdit.replace("0",id), urlDetails.replace("0",id),urlStartExp.replace("0",id));
}
