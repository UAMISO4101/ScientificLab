function showSponsors(response) {
    var sponsorsList  =$("#patrocinador");
    var sponsor;
    sponsorsList.append(new Option("Seleccione un patrocinador", -1));
    for (var i=0; i <response.length; i++){
        sponsor = response[i];
        sponsorsList.append(new Option(sponsor.fields.nombre, sponsor.pk));
    }
}

function saveProject() {
    var url = $("#formProject").attr("data-project-url");
    $.ajax({
        url: host+url,
        method:"POST",
        data:getData(),
        sucess:successSaveProject,
        error:errorSaveProject,
        dataType: 'json'
    });
}

function updateProject() {
    var url = $("#formProject").attr("data-project-url");
    $.ajax({
        "url": host + url,
        "method": "PUT",
        "data": JSON.stringify(getData()),
        "sucess": successSaveProject,
        "error": errorSaveProject,
        "headers": {
            "content-type": "application/json"
        }
    });
}
function getData() {
     var project = {};
    project.nombre =$("#nombre").val();
    project.descripcion =$("#descripcion").val();
    project.fechaInicio =$("#fechaInicio").val();
    project.fechaFinal =$("#fechaFinal").val();
    project.prioridad =$("#prioridad").val();
    project.avance =$("#avance").val();
    project.estado =$('#estado option:selected').val();
    project.idPatrocinador =$('#patrocinador option:selected').val();

    return project;
}

function successSaveProject(response) {
    alertify.success("El proyecto se ha guardado correctamente");
}

function errorSaveProject(e){
    console.log(e);
}

function showProjectStates(response){
    var statesList =$("#estado");
    var state;
    statesList.append(new Option("Seleccione un estado", -1));

    for (var i=0; i <response.length; i++){
        state = response[i];
        statesList.append(new Option(state.estado, state.id));
    }
}

function setDate(date, id){
    var dateValue =moment(date).format('YYYY-MM-DD')
    $("#"+id).val(dateValue);
}