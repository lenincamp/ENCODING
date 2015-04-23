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
                       "<td><button id='btnDelete"+(index+1)+"' class='danger'  onclick='$.delete($(this).parent())' >Eliminar</button></td>"+
                       "</tr>"     
        });
        modulo.html(setData);
    }

    var modalContent = " <div class='container'>"+
            "<div class='grid'>"+
                "<div class='row'>"+
                    "<div class='span4'></div>"+
                    "<div class='span7'>"+
                        
                        "<form id='formularioProduct' enctype='multipart/form-data'>"+
                           "<fieldset>"+
                               //"<legend>Nuevo Producto</legend>"+
                            
                            
                               "<div class='input-control text size7' data-role='input-control'>"+
                                   "<input type='text' placeholder='Producto' id='textProduct' name='product'>"+
                               "</div>"+
                                
                            
                               
                               "<div class='input-control text size7' data-role='input-control'>"+
                                   "<input type='text' placeholder='Descripcion' id='textDescription' name='description'>"+
                               "</div>"+

                            
                               "<div class='input-control text size7' data-role='input-control'>"+
                                   "<input type='text' placeholder='0.00' id='textPrice' name='price'>"+
                               "</div>"+
                            
                            
                               "<div class='input-control text size7' data-role='input-control'>"+
                                   "<input type='text' placeholder='# Piezas' id='textPieces' name='pieces'>"+
                               "</div>"+

                            
                               "<div class='input-control file size7' data-role='input-control'>"+
                                   "<input type='file' id='image_file' name='imageFile'>"+
                                   "<button class='btn-file'></button>"+                                   
                               "</div>"+
                                
                                
                            
                                "<div class='input-control select size7' data-role='input-control'>"+
                                    "<select id='cmbCategory' name='category'>"+                                                        
                                    "</select>"+
                                "</div>"+

                                "<div class='input-control checkbox size7'>"+
                                    "<label>"+
                                    "Estado: "+
                                        "<input type='checkbox' id='checkState' name='state'/>"+
                                        "<span class='check'></span>"+
                                        
                                    "</label>"+
                                "</div>"+

                                
                                "<input type='hidden' id='textIdProduct' name='codeProduct' value='0'>"+                                
                                
                                "<button type='button' class='warning' id='btnCancel' onclick='$.Dialog.close()'>Cancelar</button>"+                                                                
                                "<button type='button' class='primary' id='btnSave' onclick='$.save();'>Guardar</button>"+

                           "</fieldset>"+
                                
                               
                        "</form>"+                        
                       
                    "</div>"+
                "</div>"+
            "</div>"+
                          
        "</div> ";

    $.modal = function(content, pad, wid,title){
        $.Dialog({
            overlay: true,
            shadow: true,
            flat: true,
            icon: '',
            title: title,
            content: '',
            padding: pad,
            width:wid,
            onShow: function(_dialog){
                $.Dialog.content(content);
                $.Metro.initInputs();
          }
        });
    }

    $('#btnNew').click(function(){
        $.modal(modalContent, 30,350 , "Nuevo");
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

    $.delete = function(parent)
    {
        var tr = parent(parent);
    }

    $.message = function(response)
    {
        $('#message').fadeIn('fast');
        $('#message').html(response.mensaje);
        $('#message').fadeOut(400);
    }

    $.save = function(){

      if ($('#textProduct').val() != "" && $('#textDescription').val() != "" && $('#textPrice').val() != "")
        {
            // var producto    = $('#textProduct').val()
            // var descripcion = $('#textDescription').val()
            // var precio      = $('#textPrice').val()
            // var estado      = $('#checkState').val()
            // var categoria   = $('#cmbCategory').val()
            // var nro_piezas  = $('#textPieces').val()
            // var image       = $('#textFile').val()            
            // $.AJAX("/main/module/saveProduct/",
            //   {"prd_nom": producto , "prd_des" : descripcion , "prd_pre":precio ,
            //    "prd_est":estado , "cat_cod":categoria, "prd_cod":$('#textIdProduct').val() , 
            //    "prd_url": image , "prd_nro_piezas":nro_piezas ,"edit" : edit },$.message,false);
          var formData = new FormData($("#formularioProduct")[0]); // datos
          formData.append('edit', edit);
          $.ajax({
            url:'/main/module/saveProduct/',
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
          })

        }         

        
        $.Dialog.close();
        $.AJAX("/main/module/getProduct/","",$.getProduct,false);
    }
    
    $.AJAX("/main/module/getProduct/","",$.getProduct,true);    
})