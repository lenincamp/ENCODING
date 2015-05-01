$(function(){

    $.getProduct = function (response)
    {
        //console.log(response);
        var modulo = $('#bodyTableModule')
        var setData = "";
        $.each(response, function(index, val) 
        {
            setData+= "<tr id="+val.prd_cod+" class='text-center'>"+
                       "<td id="+(index+1)+">"+(index+1)+"</td>"+
                       "<td>"+val.prd_nom+"</td>"+
                       "<td>"+val.prd_des+"</td>"+
                       "<td>"+val.prd_pre+"</td>"+
                       "<td>"+val.prd_nro_piezas+"</td>"+                       
                       "<td id="+val.cat_cod+">"+val.cat_cod__cat_nom+"</td>"+
                       "<td style='display:none'>"+val.prd_est+"</td>"+
                       "<td><button id='btnEdit"+(index+1)+"'   class='info'    onclick='$.edit($(this).parent())' >Editar</button></td>"+ 
                       "<td><button id='btnDelete"+(index+1)+"' class='danger'  onclick='$.modalDelete($(this).parent())' >Eliminar</button></td>"+
                       "</tr>"     
        });
        modulo.html(setData);
    }

    var modalContent = //" <div class='container'>"+
            
                "<div class='row'>"+                    
                    "<div class='span5'>"+
                        
                        "<form id='formularioProduct' enctype='multipart/form-data' class='user-inpult'>"+
                           "<fieldset>"+
                               //"<legend class='text-center'>Nuevo Producto</legend>"+
                            
                                
                               "<div class='input-control text size5' data-role='input-control'>"+
                                   "<input type='text' placeholder='Producto' id='textProduct' name='product'>"+
                               "</div>"+
                                
                                "<br>"+
                               
                               "<div class='input-control text size5' data-role='input-control'>"+
                                   "<input type='text' placeholder='Descripcion' id='textDescription' name='description'>"+
                               "</div>"+

                                "<br>"+
                            
                               "<div class='input-control text size5' data-role='input-control'>"+
                                   "<input type='text' placeholder='0.00' id='textPrice' name='price'>"+
                               "</div>"+
                            
                                "<br>"+
                            
                               "<div class='input-control text size5' data-role='input-control'>"+
                                   "<input type='text' placeholder='# Piezas' id='textPieces' name='pieces'>"+
                               "</div>"+

                                "<br>"+
                            
                               "<div class='input-control file size5' data-role='input-control'>"+
                                   "<input type='file' id='image_file' name='imageFile'>"+
                                   "<button class='btn-file'></button>"+                                   
                               "</div>"+
                               
                               
                              
                                "<br>"+
                            
                                "<div class='input-control select size5' data-role='input-control'>"+
                                    "<select id='cmbCategory' name='category'>"+                                                        
                                    "</select>"+
                                "</div>"+

                                "<br>"+

                                "<input type='hidden' id='textIdProduct' name='codeProduct' value='0'>"+                                
                                
                                "<div class='span5'>"+
                                    "&nbsp; &nbsp; &nbsp;"+
                                    "<button type='button' class='size2 warning' id='btnCancel' onclick='$.Dialog.close()'>Cancelar</button>"+                                 
                                    "&nbsp; &nbsp; &nbsp;"+
                                    "<button type='button' class='size2 primary' id='btnSave' onclick='$.save();'>Guardar</button>"+                                  
                                "</div>"+
                                

                           "</fieldset>"+
                                
                               
                        "</form>"+                        
                       
                    "</div>"+   // close first span
                    
                    "<div class='span5'>"+
                    "</div>"+
                "</div>"+
            "</div>";
                          
        //"</div> ";
    

    $.modal = function(content, pad, width,title){
        $.Dialog({
            overlay: true,
            shadow: true,
            flat: true,
            icon: '',
            title: title,
            content: '',
            padding: 10,
            width:width,
            draggable:true,
            onShow: function(){
                $.Dialog.content(content);
                $.Metro.initInputs();
          }
        });
    }

    $('#btnNew').click(function(){
        $.modal(modalContent, 30,250, "Nuevo");
        $('#textProduct').focus();
        edit = 0;
        $.AJAX("/main/module/getCategory/","",$.getCategory,true);
    })


    $.getCategory = function(response)
    {        
        //console.log(response);
        var category = $('#cmbCategory')
        var setData = "";
        $.each(response, function(index,val)
        {
            setData +="<option value="+val.cat_cod+">"+val.cat_nom+"</option>";

        });
        category.html(setData);
    }

    var edit=0;

    $.edit = function(parent)
    {
        
        var tr = $(parent).parent(); //

        $.modal(modalContent, 10 , 100, "Editar"); // set Modal
        $.AJAX("/main/module/getCategory/","",$.getCategory,false); //fill out Categories

        $('#textProduct').val(tr.children()[1].textContent);        
        $('#textDescription').val(tr.children()[2].textContent);
        $('#textPrice').val(tr.children()[3].textContent);
        $('#textPieces').val(tr.children()[4].textContent);
        $('#cmbCategory').val(tr.children()[5].id);
        
        if (tr.children()[6].textContent == "true")
        {
          $('#checkState').attr('checked',true);
        }
        else
        {
          $('#checkState').attr('checked',false); 
        }
        
        $('#textProduct').focus();
        $('#textIdProduct').val(tr.attr('id'));
        edit = 1;
    }

    $.modalDelete = function(parent)
    {
        var tr = $(parent).parent();
        var modalDelete = "<p>¿Está seguro de eliminar el Producto?</p>"+
                          "<button id='"+tr.attr('id')+"' onclick='$.deleteProduct($(this))'>Si</button>"+
                          "<button id='btnCancel' onclick='$.closeModal()'>No</button>";
        $.modal(modalDelete,30 , 100 , "Eliminar");
    }

    $.notification = function(response)
    {
        
          $.notify(response.mensaje,{position:'top right', className:'success', autoHide:true ,
                                      autoHideDelay:3000});
          //console.log("Hola soy una notificacion");
    }

    $.deleteProduct = function(idProduct)
    {      
      $.AJAX("/main/module/deleteProduct/",{"prd_cod":$(idProduct).attr('id')} , $.notification, true);
      $.AJAX("/main/module/getProduct/","",$.getProduct,false);
      $.Dialog.close();
    }

    $.closeModal = function()
    {
      $.Dialog.close()
    }
    

    $.save = function(){

      if ($('#textProduct').val() != "" && $('#textDescription').val() != "" && $('#textPrice').val() != "")
        {                        
            
          var formData = new FormData($("#formularioProduct")[0]); // datos
          formData.append('edit', edit);          
          //($('#checkState').is(':checked')) ? formData.append('stateUnique',"true"):formData.append('stateUnique',"false")// nice conditional
          $('#image_file').val() != "" ? formData.append('withImage',"true"): formData.append('withImage',"false")

          $.ajax({
            async:false,
            url:'/main/module/saveProduct/',
            type: 'POST',
            data: formData,
              //necesario para subir archivos via ajax
            cache: false,
            contentType: false,
            processData: false,            
            //mientras se envia el archivo            
            // beforeSend: function(){               
            //       $.Notify({style: {background: '#008287', color: 'white'}, caption: 'Info...', content: "Subiendo la imagen, por favor espere..."});
            //   },
            
            //si finalizo correctamente
            success: function(data)
            {         
              //$.Notify({style: {background: '#669900', color: 'white'}, caption: 'Info...', content: data.mensaje});
              $.notify(data.mensaje,{position:'top right', className:'success', autoHide:true ,
                                      autoHideDelay:3000});
            },
            
            //si ocurrido un error
            // error: function(){
            //     $.Notify({style: {background: '#a80000', color: 'white'}, caption: 'Info...', content: "Error al almacenar imagen..."});
            // },                       
          
          })           
          $.AJAX("/main/module/getProduct/","",$.getProduct,false);
        }
        else{
          $.notify("Hay algun campo vacío",{position:'top right', className:'error', autoHide:true ,
                    autoHideDelay:3000})
        }                 
        $.Dialog.close();
        
    }
    
    $.AJAX("/main/module/getProduct/","",$.getProduct,true);
})