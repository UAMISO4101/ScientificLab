function showSponsors(response) {
    var sponsorsList  =$("#patrocinador");
    var sponsor;
    sponsorsList.append(new Option("Seleccione un patrocinador", -1));
    for (var i=0; i <response.length; i++){
        sponsor = response[i];
        sponsorsList.append(new Option(sponsor.fields.nombre, 1));
    }
}
/*
function validateData(){
    if(dataIsCorrect())
        saveProject();
}
function dataIsCorrect() {
    var result = true;
    result = result || requiredField("nombre","El nombre es requerido");
    result = result || requiredField("descripcion","La descripción es requerida");
    result = result || requiredField("prioridad","La prioridad es requerida");
    result = result || requiredField("avance","El avance es requerido");
    if($("#avance").val()>100 || $("#avance").val()<0) {
        alertify.error("El avance debe ser entre 0% y 100%");
        result = false;
    }

    if($("#prioridad").val()>4 || $("#prioridad").val()<1) {
        alertify.error("La prioridad debe ser entre 1 y 4");
        result = false;
    }

    var startDate = moment($("#fechaInicio").val())
    var endDate  =moment($("#fechaFinal").val());
    if(!startDate.isValid() || !endDate.isValid()){
        alertify.error("Las fechas son requeridas");
        result = false;
    }

    if(startDate.diff(endDate)>=0) {
        alertify.error("La fecha incial debe ser menor a la fecha final");
        result = false;
    }

    if($('#estado option:selected').val() == -1) {
        alertify.error("Seleccione un estado");
        result = false;
    }

    if($('#patrocinador option:selected').val() == -1) {
        alertify.error("Seleccione un patrocinador");
        result = false;
    }
    return result;
}

function requiredField(id, message) {
    if($("#"+id).val().trim() == '') {
        alertify.error(message);
        return false;
    }
    return true;
}*/
function saveProject() {
    var project = {};
    project.nombre =$("#nombre").val();
    project.descripcion =$("#descripcion").val();
    project.fechaInicio =$("#fechaInicio").val();
    project.fechaFinal =$("#fechaFinal").val();
    project.prioridad =$("#prioridad").val();
    project.avance =$("#avance").val();
    project.estado =$('#estado option:selected').val()
    project.patrocinador =$('#patrocinador option:selected').val()

    var url = $("#formAddProject").attr("data-add-project-url");
    $.ajax({
        url: host+url,
        method:"POST",
        data:project,
        sucess:successSaveProject,
        error:errorSaveProject,
        dataType: 'json'
    });
}

function editProject() {
    var project = {};
    project.nombre =$("#nombre").val();
    project.descripcion =$("#descripcion").val();
    project.fechaInicio =$("#fechaInicio").val();
    project.fechaFinal =$("#fechaFinal").val();
    project.prioridad =$("#prioridad").val();
    project.avance =$("#avance").val();
    project.estado =$('#estado option:selected').val()
    project.patrocinador =$('#patrocinador option:selected').val()

    var url = $("#formEditProject").attr("data-edit-project-url");
    $.ajax({
        url: host+url,
        method:"POST",
        data:project,
        sucess:successSaveProject,
        error:errorSaveProject,
        dataType: 'json'
    });
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