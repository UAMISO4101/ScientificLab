/**
 * Created by Lenovo on 26/03/2017.
 */
url="/laboratorio/protocolofiltro" ;
var table ;
var data ;
var  listarProtocolos= function(urlDetails){
    var btnDetallar = "<a href='"+urlDetails +"' id='Details_0'  class='btn btn-info btn-round'><span class='glyphicon glyphicon-cog'></span></a>"
    var table = $('#myTable').DataTable( {

        "ajax": {
            "url":  host+url,
            "dataSrc": ""
        },
        "columns": [
            { data: "titulo" },
            { data: "descripcion" },
            { data: "version" },
            { data: "categoria" },
            { sortable: false,
              "render": function ( data, type, row, meta ) {
               return btnDetallar.replace (/0/g,row.id);
                 }
             },
        ]
        } );

        $('#myTable tbody').on( 'click', '#btn', function () {
            var data = table.row( $(this).parents('tr') ).data();
            crearVersion(data.id)

        } );
}

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

function showCategorias(response) {
    var categoriasList  =$("#categoria");
    var categoria;
    categoriasList.append(new Option("Seleccione una categoria", -1));
    for (var i=0; i <response.length; i++){
        categoria = response[i];
        categoriasList.append(new Option(categoria.nombre, categoria.id));
    }
}