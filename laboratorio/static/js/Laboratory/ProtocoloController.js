/**
 * Created by Lenovo on 26/03/2017.
 */
url="/laboratorio/protocolofiltro" ;
var table ;
var data ;

function crearVersion(id)
{
    var settings = {
    "async": true,
    "crossDomain": true,
    "url": host+"/laboratorio/protocolos/"+id+"/nuevaVersion/",
    "method": "POST",
    "headers": {}
    }

    if(confirm("Esta seguro de crear una nueva version ?")) {
        $.ajax(settings).done(function (response) {
            alert("Se registro con exito")
            location.reload();
        });
    }else{
        return false;
    }
}

var  listarProtocolos= function(){
 var table = $("#myTable").DataTable( {
        "ajax": {
            "url":  host+url,
            "dataSrc": ""
        },
        "columns": [
            { data: "titulo" },
            { data: "descripcion" },
            { data: "version" },
            { data: "categoria" },
            { data: "habilitado" },
            { "defaultContent": "<a href='#'  id='btn' class='btn btn-info btn-round'><span class='glyphicon glyphicon-plus'></span></a>" },
        ]
        } );

        $("#myTable tbody").on( "click", "#btn", function () {
            var data = table.row( $(this).parents("tr") ).data();
            crearVersion(data.id)

        } );
}

function trySaveProtocolo() {
    if(dataProtocoloIsCorrect()) {
        saveProtocolo();
    }
}

function dataProtocoloIsCorrect() {

    if($("#titulo").val().trim() === "") {
        alertify.error("El titulo del protocolo es requerido",2);
        return false;
    }

    if($("#version").val()<0) {
        alertify.error("La version debe ser mayor a 1",2);
        return false;
    }

    if($("#categoria option:selected").val() === "-1") {
        alertify.error("Seleccione una categoria",2);
        return false;
    }

    if($("#descripcion").val().trim() === "") {
        alertify.error("La descripcion no debe ser nula",2);
        return false;
    }

    return true;
}

function getData() {
    var protocolo = {};
    protocolo.titulo =$("#titulo").val();
    protocolo.version =$("#version").val();
    protocolo.categoria =$("#categoria option:selected").val();
    protocolo.habilitado =$("#habilitado").is(":checked");
    protocolo.descripcion =$("#descripcion").val();
    return protocolo;
}

function saveProtocolo() {
    var url = $("#formProtocolo").attr("save-protocolo-url");
    $.ajax({
        url: host+url,
        method:"POST",
        data:JSON.stringify(getData()),
        success:successSaveProtocolo,
        error:errorSaveProtocolo,
        dataType: "json"
    });
}

function successSaveProtocolo(response) {
    alertify.success("El protocolo se ha guardado correctamente");
}

function errorSaveProtocolo(e){
    alertify.error("Error al guardar el protocolo");
}


function showCategorias(response) {
    var categoriasList  =$("#categoria");
    var categoria;
    categoriasList.append(new Option("Seleccione una categoria", -1));
    for (var i=0; i <response.length; i++){
        categoria = response[i];
        categoriasList.append(new Option(categoria.nombre, categoria.id));
    }
}

