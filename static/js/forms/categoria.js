$(function(){

    /*
        Get the catgories
     */
    $.getCategory = function(data)
    {
        var category = $('#bodyTableModule')
        var setData = ""
        
        $.each(data, function (index, data) 
        {
            setData += "<tr id= "+data.cat_cod+" class='text-center'>"+
                    "<td>"+(index+1)+"</td>"+
                    "<td>"+data.cat_nom+"</td>"+
                    "<td>"+data.cat_des+"</td>"+
                    "<td><button id='btnEdit"+(index+1)+"'   class='info'    onclick='$.edit($(this).parent())' >Editar</button></td>"+ 
                    "<td><button id='btnDelete"+(index+1)+"' class='danger'  onclick='$.modalDelete($(this).parent())' >Eliminar</button></td>"+
                    "</tr>";                   
        });

        category.html(setData);
    }

    $.notification = function(data)
    {
        $.notify(data.mensaje,{position:'bottom right', className:'success', autoHide:true ,
                                      autoHideDelay:3000});
    }

    var edit;
    var modalContent = //" <div class='container'>"+
            
                "<div class='row'>"+                    
                    "<div class='span5'>"+
                        
                        "<form id='formularioCategoria' enctype='multipart/form-data' class='user-inpult'>"+
                           "<fieldset>"+
                               //"<legend class='text-center'>Nuevo Producto</legend>"+
                            
                                
                               "<div class='input-control text size5' data-role='input-control'>"+
                                   "<input type='text' placeholder='Categoria' id='textCategory' name='cat_nom'>"+
                               "</div>"+
                                
                                "<br>"+
                               
                               "<div class='input-control text size5' data-role='input-control'>"+
                                   "<input type='text' placeholder='Descripcion' id='textDescription' name='cat_des'>"+
                               "</div>"+

                                "<br>"+                   
                            
                               "<div class='input-control file size5' data-role='input-control'>"+
                                   "<input type='file' id='image_file' name='cat_url'>"+
                                   "<button class='btn-file'></button>"+                                   
                               "</div>"+                            
                               
                                "<br>"+

                                "<input type='hidden' id='textIdCategory' name='cat_cod' value='0'>"+

                                "<br>"+

                                "<div class='span5'>"+
                                    "&nbsp; &nbsp; &nbsp;"+
                                    "<button type='button' class='size2 warning' id='btnCancel' onclick='$.Dialog.close()'>Cancelar</button>"+                                 
                                    "&nbsp; &nbsp; &nbsp;"+
                                    "<button type='button' class='size2 primary' id='btnSave' onclick='$.save();'>Guardar</button>"+                                  
                                "</div>"+
                                

                           "</fieldset>"+
                                
                               
                        "</form>"+                        
                       
                    "</div>"+   // close first span           
                    
                "</div>"+
            "</div>";

    $('#btnNew').click(function(){
        $.DIALOG(modalContent, 30,250, "Nuevo");
        $('#textCategory').focus();
        edit = 0;
        $.AJAX("/main/module/getCategory/","",$.getCategory,true);
    })

    $.save = function(){

      if ($('#textCategory').val() != "" && $('#textDescription').val() != "")
        {                        
            
          var formData = new FormData($("#formularioCategoria")[0]); // datos
          formData.append('edit', edit);          
          //($('#checkState').is(':checked')) ? formData.append('stateUnique',"true"):formData.append('stateUnique',"false")// nice conditional
          $('#image_file').val() != "" ? formData.append('withImage',"true"): formData.append('withImage',"false")

          $.ajax({
            async:false,
            url:'/main/module/saveCategory/',
            type: 'POST',
            data: formData,
              //necesario para subir archivos via ajax
            cache: false,
            contentType: false,
            processData: false,                        
            
            //si finalizo correctamente
            success: function(data)
            {         
              //$.Notify({style: {background: '#669900', color: 'white'}, caption: 'Info...', content: data.mensaje});
              $.notify(data.mensaje,{position:'top right', className:'success', autoHide:true ,
                                      autoHideDelay:3000});
            },      
            
          })           
          $.AJAX("/main/module/getCategory/","",$.getCategory,false);
        }
        else{
          $.notify("Hay algun campo vacío",{position:'top right', className:'error', autoHide:true ,
                    autoHideDelay:3000})
        }                 
        $.Dialog.close();
        
    }

    $.edit = function(parent)
    {
        
        var tr = $(parent).parent(); //

        $.DIALOG(modalContent, 10 , 100, "Editar"); // set Modal        

        $('#textCategory').val(tr.children()[1].textContent);        
        $('#textDescription').val(tr.children()[2].textContent);      
        $('#textCategory').focus();
        $('#textIdCategory').val(tr.attr('id'));
        edit = 1;
    }

    $.modalDelete = function(parent)
    {
        var tr = $(parent).parent();
        var modalDelete = "<p>¿Está seguro de eliminar la Categoria?</p>"+
                          "<button id='"+tr.attr('id')+"' onclick='$.deleteProduct($(this))'>Si</button>"+
                          "<button id='btnCancel' onclick='$.closeModal()'>No</button>";
        $.DIALOG(modalDelete,30 , 100 , "Eliminar");
    }

    $.deleteProduct = function(idProduct)
    {      
      $.AJAX("/main/module/deleteCategory/",{"prd_cod":$(idProduct).attr('id')} , $.notification, true);
      $.AJAX("/main/module/getCategory/","",$.getCategory,false);
      $.Dialog.close();
    }

    $.AJAX("/main/module/getCategory/","",$.getCategory,false);
})