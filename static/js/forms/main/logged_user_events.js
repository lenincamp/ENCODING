$(function () {
	
	$("#txtDateEvent").datepicker({
        
        format: "yyyy-mm-dd", // set output format
        effect: "slide", // none, slide, fade
        position: "bottom", // top or bottom,
        locale: 'es', // 'ru' or 'en', default is $.Metro.currentLocale
    });

    /*===VALIDACIONES===*/
    $('#frmImg').validate({
        rules: {            
            nameEvent: {minlength: 8,required: true},
            txtDateEvent: {required: true},
            imageEvent: {required:true},
            informationEvent: {minlength: 8,required: true}
        },
        messages: {
		    nameEvent: "",
		    txtDateEvent: "",
		    imageEvent:"",
		    informationEvent:""
	    },
        highlight: function (element) {
            $(element).parent().removeClass('info-state');
            $(element).parent().addClass('error-state');
            $(element).popover('show');                
        },
        success: function (element) {
          //element.text('OK!');
          $(element).parent().removeClass('error-state');
          $(element).parent().addClass('info-state');
        }
        
    });
    /*=============================*/

    $("#frmImg").submit(function(event){
    	if ($("#frmImg").validate().numberOfInvalids()==0 && $("#dateEvent").val()!='' && $.isImage(fileExtension)){
    		var formData = new FormData($("#frmImg")[0]);       
	        $.ajax({
	        	url: '/main/logged_user/create_event/add_event/',  
	            type: 'POST',
	            data: formData,
	            //necesario para subir archivos via ajax
	            cache: false,
	            contentType: false,
	            processData: false,
	            // mientras se envia el archivo
	            beforeSend: function(){               
	                $.Notify({style: {background: '#008287', color: 'white'}, caption: 'Info...', content: "Subiendo la imagen, por favor espere..."});
	            },
	            //si finalizo correctamente
	            success: function(data){
	                message = $("<span class='success'>La imagen ha subido correctamente.</span>");
	                console.log(message);
	                if (data.save){
	                  $.Notify({style: {background: '#008287', color: 'white'}, caption: 'Info...', content: "Guardado Correctamente..."});
	                }
	            },
	            //si ocurrido un error
	            error: function(){
	                $.Notify({style: {background: '#008287', color: 'white'}, caption: 'Info...', content: "Error al almacenar imagen..."});
	            }
	        });
    	}
    	else {
    		if ($("#dateEvent").val()==''){
    			$("#txtDateEvent").popover('show');
    		}
    		if (!$.isImage(fileExtension)){
    			$("#txtImageEvent").popover('show');
    		}
    		
    	}
    	return false;
    });

	//global variable to know if it is image 
    var fileExtension = "";
    var fileName = "";
    //función que observa los cambios del campo file y obtiene información
    $(':file').change(function()
    {
        //obtenemos un array con los datos del archivo
        var file = $("#txtImageEvent")[0].files[0];
        //obtenemos el nombre del archivo
        fileName = file.name;
        //obtenemos la extensión del archivo
        fileExtension = fileName.substring(fileName.lastIndexOf('.') + 1);
        //obtenemos el tamaño del archivo
        var fileSize = file.size;
        //obtenemos el tipo de archivo image/png ejemplo
        var fileType = file.type;
        //mensaje con la información del archivo
        console.log("<span class='info'>Archivo para subir: "+fileName.replace(".png", "")+", peso total: "+fileSize+" bytes.</span>");
    });
  
	//comprobamos si el archivo a subir es una imagen
  	//para visualizarla una vez haya subido
  	$.isImage = function(extension)
  	{
    	switch(extension.toLowerCase()) 
    	{
      		case 'jpg': case 'gif': case 'png': case 'jpeg':
          		return true;
      			break;
      		default:
          		return false;
      			break;
    	}
  	}

    /*=======*/
    $("#btnEvents").click(function(event) {
        return false;
    });

});