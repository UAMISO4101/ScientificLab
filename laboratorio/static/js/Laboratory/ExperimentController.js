function saveExperiment(){
    var experiment = {};
    experiment.nombre =$("#nombre").val();
    experiment.descripcion =$("#descripcion").val();
    experiment.fechaInicio =$("#fechaInicio").val();
    experiment.prioridad =$("#prioridad").val();
    experiment.estado =$("#estado").attr("id");
    experiment.resultado =$("#resultado").attr("id");
    experiment.proyecto =$("#proyecto").attr("id");
    experiment.responsable =$("#responsable").attr("id");


    var url = $("#formAddExperiment").attr("data-add-experiment-url");
    $.ajax({
        url: host+url,
        method:"POST",
        data:experiment,
        sucess:successSaveExperiment,
        error:errorSaveExperiment,
        dataType: 'json'
    });
}

function successSaveExperiment() {
    alertify.success("El experimento se ha guardado correctamente");
}

function errorSaveExperiment(e){
    console.log(e);
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
