$(function(){
	$("#kwd_search").keyup(function(){
        // When value of the input is not blank
        if( $(this).val() != "")
        {
            // Show only matching TR, hide rest of them
            $("#tblEvents tbody>tr").hide();
            $("#tblEvents td:contains-ci('" + $(this).val() + "')").parent("tr").show();
        }
        else
        {
            // When there is no input or clean again, show everything back
            $("#tblEvents tbody>tr").show();
        }
    });
    /*===========================================*/
    $.showImage = function (btn) {
        var pathFtp = "ftp://ftp.encodingideas.heliohost.org/evento/";
        var pathImg = $($($(btn).parent('td')).children('span')).text();
        var urlImg  = $.trim(pathFtp + pathImg);
        console.log("URL=>>>>> ", urlImg);
        //
        var content = "<img src='"+urlImg+"' class='shadow' style='width: 620px; height: 400px;''>"
        $.DIALOG(content,0,250,"Imagen Evento","icon-pictures");
    }


    $.infoEvent = function (btn) {
        var idTr =  $($($(btn).parent('td')).parent()).attr('id');
        var posting = $.post( "/main/logged_user/events/info_event/", { eCod: idTr } );
        posting.done(function( response ) {
            console.log( response );
        });
        posting.fail(function( data ) {
            $.Notify({style: {background: '#008287', color: 'white'}, caption: 'Info...', content: "Error en el Server..."});
        });
    }

    $.loadEvents = function(response){
        var events = $("#tbodyEvents");
        var datos = "";           
            
        $.each(response, function(i, item){

            datos+= "<tr id="+item.eve_cod+" class='text-center'>"+
                        "<td>"+(i+1)+"</td>"+
                        "<td class='text-left'>"+item.eve_nom+"</td>"+
                        "<td>"+$.trim(item.eve_fch)+"</td>"+
                        "<td class='text-left'>"+$.trim(item.eve_inf)+"</td>"+
                        "<td id="+item.eve_url_img+">"+
                            '<span style="display:none;">'+item.eve_url_img+'</span>'+
                            '<button class="default" title="Ver" onclick="$.showImage(this);">'+
                                '<i class="icon-pictures" title="Ver"></i>'+
                            '</button>'+
                        "</td>"+                            
                        "<td>"+
                            '<button class="bg-darkOrange fg-white" title="Información" onclick="$.infoEvent(this);">'+
                                '<i class="icon-list" title="Información"></i>'+
                            '</button>'+
                        "</td>"+
                        "<td>"+
                            '<button class="primary" title="Editar" onclick="$.editEvent(this);">'+
                                '<i class="icon-pencil" title="Editar"></i>'+
                            '</button>'+
                        "</td>"+
                        "<td>"+
                            "<button class='danger' title='Eliminar' onclick='$.deleteEvent(this);'>"+
                                "<i class='icon-remove' title='Eliminar'></i>"
                            "</button>"+
                        "</td>"+  
                    "</tr>";               

        });
        events.html(datos);
    
    }
    $.AJAX("/main/logged_user/events/load_events/","", $.loadEvents,true);
    /*===========================================*/
});

$.extend($.expr[":"], 
{
    "contains-ci": function(elem, i, match, array) 
    {
        return (elem.textContent || elem.innerText || $(elem).text() || "").toLowerCase().indexOf((match[3] || "").toLowerCase()) >= 0;
    }
});