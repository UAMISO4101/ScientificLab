function showProyectsNames(response){
    var nameProyectList =$("#projects");
    var project;
    nameProyectList.append(new Option("Seleccione un proyecto", -1));
    for (var i=0; i <response.length; i++){
        project = response[i];
        nameProyectList.append(new Option(project.fields.nombre, project.pk));
    }
 }

 function paintChart() {
     var idProject= $('#projects option:selected').val();
 }