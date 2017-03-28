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
     //alert(host+url)
     $.ajax(settings).done(function (response) {
        //alert("Responde Ajax "+response);
       for( i in response) {
            var objeto = response[i] ;
            console.log(objeto.titulo+" * "+objeto.descripcion);

            html+="<tr class='alt'>";
            html+="<td><input type='checkbox'/></td>";
            html+="<td>"+objeto.titulo+"</td>";
            html+="<td>"+objeto.descripcion+"</td>";
            html+="<td>"+objeto.version+"</td>";
            html+="<td>"+objeto.categoria+"</td>";
            html+="<td><a href='url+'laboratorio:editarProyecto' class='btn btn-info btn-round'><span class='glyphicon glyphicon-pencil'></span></a></td>";
            html+="</tr>";


//       console.log(objeto.fields.titulo);  // (o el campo que necesites)
        //html+=objeto.fields.titulo ;
           // console.log(response);
   //data.artists.items[i].href
       }
       $("#myTable tbody").html(html);
        //console.log(response);
   });
}