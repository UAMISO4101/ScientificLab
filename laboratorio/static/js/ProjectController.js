function showSponsors(response) {
    var sponsorsList  =$("#patrocinador");
    var sponsor;
    for (var i=0; i <response.length; i++){
        sponsor = response[i];
        sponsorsList.append(new Option(sponsor.fields.nombre, sponsor.pk));
    }
}

function saveProject(){
    var project = {};
    project.nombre =$("#nombre").val();
    project.descripcion =$("#descripcion").val();
    project.fechaInicio =$("#fechaInicio").val();
    project.fechaFinal =$("#fechaFinal").val();
    project.prioridad =$("#prioridad").val();
    project.avance =$("#avance").val();
    project.estado =$("#estado").attr("id");
    project.patrocinador =$("#patrocinador").attr("id");


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

function successSaveProject() {

}

function errorSaveProject(e){
    console.log(e);
}