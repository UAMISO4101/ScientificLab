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

function deshabilitarProtocolo(id, urlDisable)
{
    var url = urlDisable.replace(0,id);
    var settings = {
    "async": true,
    "crossDomain": true,
    "url": host+url,
    "method": "POST",
    "headers": {}
    }

    if(confirm("Esta seguro de deshabilitar el protocolo ?")) {
        $.ajax(settings).done(function (response) {
            alert("Se deshabilito con exito")
            location.reload();
        });
    }else{
        return false;
    }
}

function crearVersion(id, urlNewVersion) {
    var url = urlNewVersion.replace(0, id);
    var settings = {
    "async": true,
    "crossDomain": true,
    "url": host+url,
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

var  listarProtocolos= function(urlDetails,urlEdit, urlNewVersion,urlDisable,urlFilter){
    var btnDetallar = "<a href='"+urlDetails +"' id='Details_0'  class='btn btn-info btn-round'><span class='glyphicon glyphicon-cog'></span></a>";
    var btnEdit="<a href='"+ urlEdit +" ' class='btn btn-info btn-round' ><span class='glyphicon glyphicon-pencil'></span></a>";
    var btnNewVersion="<a href='#'  id='btn' class='btn btn-info btn-round' title='Agregar Version'><span class='glyphicon glyphicon-plus'></span></a>";
    var btnDisable="<a href='#'  id='deshabilitar' class='btn btn-info btn-round' title='Deshabilitar'><span class='glyphicon glyphicon-remove'></span></a>";
    var table = $("#myTable").DataTable( {
        "ajax": {
            "url":  host+urlFilter,
            "dataSrc": ""
        },
        "columns": [
            { data: "titulo" },
            { data: "descripcion" },
            { data: "version" },
            { data: "categoria" },
            { data: "habilitado" },
            { sortable: false,
              "render": function ( data, type, row, meta ) {
               return btnNewVersion+ btnDisable+btnEdit.replace (/0/g,row.id)+btnDetallar.replace (/0/g,row.id);
              }
             }
        ]
        } );

        $("#myTable tbody").on( "click", "#btn", function () {
            var data = table.row( $(this).parents("tr") ).data();
            crearVersion(data.id, urlNewVersion);

        } );

        $("#myTable tbody").on( "click", "#deshabilitar", function () {
            var data = table.row( $(this).parents("tr") ).data();
            deshabilitarProtocolo(data.id, urlDisable);

        } );
}

function successSaveProtocolo(response) {
    alertify.success("El protocolo se ha guardado correctamente");
}

function errorSaveProtocolo(e){
    alertify.error("Error al guardar el protocolo");
}

function updateProtocol() {
    if(!dataProtocoloIsCorrect()) {
        return;
    }
    var protocol = getData();
    protocol.id = $("#formProtocolo").attr("id-protocol-data");

    var url = $("#formProtocolo").attr("edit-protocol-url").replace(0,protocol.id);
    $.ajax({
        url: host+url,
        method:"PUT",
        data:JSON.stringify(protocol),
        success:successSaveProtocolo,
        error:errorSaveProtocolo,
        dataType: "json"
    });
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

function trySaveProtocolo() {
    if(dataProtocoloIsCorrect()) {
        saveProtocolo();
    }
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

function showCategorias(response) {
    var categoriasList  =$("#categoria");
    var categoria;
    categoriasList.append(new Option("Seleccione una categoria", -1));
    for (var i=0; i <response.length; i++){
        categoria = response[i];
        categoriasList.append(new Option(categoria.nombre, categoria.id));
    }
}

