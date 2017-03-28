/**
 * Created by Lenovo on 26/03/2017.
 */
url="/laboratorio/protocolofiltro" ;
function listarProtocolos(){
    var buscar = $("#titulo").val();
    if(!buscar)
    {
      buscar=""
    }
    var settings = {
    "async": true,
    "crossDomain": true,
    "url": host+url+"/?titulo="+buscar,
    "method": "GET",
    "headers": {}
    }
    var html="";

     $.ajax(settings).done(function (response) {

       for(var i in response) {
            var objeto = response[i] ;
            html+="<tr class='alt'>";
            html+="<td><input type='checkbox'/></td>";
            html+="<td>"+objeto.titulo+"</td>";
            html+="<td>"+objeto.descripcion+"</td>";
            html+="<td>"+objeto.version+"</td>";
            html+="<td>"+objeto.categoria+"</td>";
            html+="<td><a href='#' class='btn btn-info btn-round'><span class='glyphicon glyphicon-plus' onclick='crearVersion("+objeto.id+")'></span></a></td>";
            html+="</tr>";
       }
       $("#myTable tbody").html(html);
        //console.log(response);
   });
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
        // alert("Responde ");
        $.ajax(settings).done(function (response) {
            alert("Se registro con exito")
            location.reload();
        });
    }else{
        return false;
    }
}