function saveExperiment(){
    var experiment = {};
    experiment.nombre =$("#nombre").val();
    experiment.descripcion =$("#descripcion").val();
    experiment.fechaInicio =$("#fechaInicio").val();
    experiment.prioridad =$("#prioridad").val();
    experiment.estado =$('#estado option:selected').val();
    experiment.resultado =$('#resultado option:selected').val();
    experiment.idProyecto =$('#proyecto option:selected').val();
    experiment.idResponsable =$('#responsable option:selected').val();


    var url = $("#formAddExperiment").attr("data-add-experiment-url");
    console.log(url);
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
    console.log("El experimento se ha guardado correctamente");
}

function errorSaveExperiment(e){
    console.log("Error al guardar el experimento");
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

    function showProyectsNames(response){
    var nameProyectList =$("#proyecto");
    nameProyectList.append(new Option("Seleccione un proyecto", -1));

    for (var i=0; i <response.length; i++){
        proyecto = response[i];
        nameProyectList.append(new Option(proyecto.fields.nombre, proyecto.id));
    }
}

    function showResponsables(response){
    var responsablesList =$("#responsable");
    responsablesList.append(new Option("Seleccione un responsable", -1));

    for (var i=0; i <response.length; i++){
        responsable = response[i];
        responsablesList.append(new Option(responsable.fields.nombre, responsable.id));
    }
}
