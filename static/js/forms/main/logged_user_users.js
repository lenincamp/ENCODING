$(function(){
    /*===VALIDACIONES===*/
    $('#frmUsers').validate({
        rules: {
            ci:{required:true,minlength:10,maxlength:10,digits:true},
            name: {minlength: 8,required: true},
            lastname: {minlength: 8,required: true},
            phone:{rangelength:[7,10],required:true,digits:true},
            address:{minlength: 8,required: true},
            typeUser:{required:true},
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
    ///VALIDACION CEDULA
    var invalid = false;
    $.validateCi = function(id){
       $(id).validarCedulaEC({
            strict: true,
            events: "change",
            onValid: function () {
                invalid = false;
            },
            onInvalid: function () {
                invalid = true;
                $(id).popover('show');
            }
        }); 
    };

    $.validateCi("#txtCi");
    /*=============================*/

    $.loadUsers = function(response){
        var users = $("#tbodyUsers");
        var datos = "";           
            
        $.each(response, function(i , item){

            datos+= "<tr id="+item.usu_cod+" class='text-center'>"+
                        "<td>"+(i+1)+"</td>"+
                        "<td>"+item.usu_ced+"</td>"+
                        "<td class='text-right'>"+$.trim(item.usu_nom)+"</td>"+
                        "<td class='text-left'>"+$.trim(item.usu_ape)+"</td>"+
                        "<td>"+item.usu_tel+"</td>"+
                        "<td>"+item.usu_dir+"</td>"+
                        "<td>"+item.tip_cod__tip_des+"</td>"+
                        "<td>"+
                            '<button class="primary" title="Editar" onclick="$.editForm(this, this.id);" id="'+item.tip_cod+'">'+
                                '<i class="icon-pencil" title="Editar"></i>'+
                            '</button>'+                                           
                        "</td>"+
                        "<td>"+
                            "<button class='danger' title='Eliminar' onclick='$.deleteUser(this);'>"+
                                "<i class='icon-remove' title='Eliminar'></i>"
                            "</button>"+
                        "</td>"+  
                    "</tr>";               

        });
        users.html(datos);
    }
    $.AJAX("/main/logged_user/create_user/load_users/","", $.loadUsers,true);

    $.unlockForm = function(){
        $("input[type='text']").removeAttr('disabled');
        $("select").removeAttr('disabled');
    }
    $.lockForm=function(){
        $("input[type='text']").attr('disabled','true').val('');
        $("select").attr('disabled','true').val('0');
    }

    $("#btnNuevo").click(function(event) {
        $.unlockForm();
        $("#btnGuardar").removeClass('disabled');
        $("#btnCancelar").removeClass('disabled');
        $("#btnBuscar").addClass('disabled');
        $(this).addClass('disabled');

    });

    $.responseSaveUsers = function(response){
        if (response.save) {
            $.Notify.show("Guardado Correctamente!!!");
        }
        else {
            $.Notify.show("Error, Problemas al almacenar usuario!!!");
        }
    }

    $.edit = function() {
        activeEdit=false;
        $("input[type='button']").removeClass('disabled');
        $("input[type='button']").addClass('disabled');
        $("#btnGuardar").removeClass('disabled');
        $("#btnGuardar").addClass('disabled');
        $("#btnNuevo").removeClass('disabled');
        $("#btnBuscar").removeClass('disabled');        
        $.lockForm();
        $.AJAX("/main/logged_user/create_user/load_users/","", $.loadUsers,false);
    }

    $("#frmUsers").submit(function(event) {
        if (!$("#btnGuardar").hasClass('disabled')){

            if (activeEdit && !invalid && $("#frmUsers").validate().numberOfInvalids()==0 && $("#cmbTypeUser").val()!=0){

                $.AJAX("/main/logged_user/create_user/add_users/?edit="+activeEdit+"&cdu="+idU,$(this).serialize(),$.responseSaveUsers,false);
                $.edit();
            } 
            else {             
                if (!activeEdit) {
                    $.AJAX("/main/logged_user/create_user/add_users/?edit="+activeEdit+"&cdu="+idU,$(this).serialize(),$.responseSaveUsers,false);
                    $.edit();
                }
                else if (invalid) { $("#txtCi").popover('show'); }
                else if ($("#cmbTypeUser").val()==0) { $("#cmbTypeUser").popover('show'); }
            }

            
        }
        return false;
    });

    $("#btnCancelar").click(function(event) {
        $.lockForm();
        $("input[type='button']").removeClass('disabled');
        $("input[type='button']").addClass('disabled');
        $("#btnGuardar").removeClass('disabled');
        $("#btnGuardar").addClass('disabled');
        $("#btnNuevo").removeClass('disabled');
        $("#btnBuscar").removeClass('disabled');
        if (activeEdit){
            $.AJAX("/main/logged_user/create_user/load_users/","", $.loadUsers,true);
            activeEdit=false;
        }
    });

    $("#btnBuscar").click(function(event) {
        $("input[type='button']").removeClass('disabled');
        $("input[type='button']").addClass('disabled');
        $("#btnGuardar").removeClass('disabled');
        $("#btnGuardar").addClass('disabled');
        $("#btnBuscar").removeClass('disabled');
        $("#btnCancelar").removeClass('disabled');
        $.unlockForm();
    });

    var idU = 0;
    var activeEdit = false;
    $.editForm = function(button, typeU){
        var tr = $(button).parent().parent();
        idU = tr.attr('id');
        $("#txtCi").val(tr.children()[1].innerHTML);
        $("#txtName").val($.trim(tr.children()[2].innerHTML));
        $("#txtLastname").val($.trim(tr.children()[3].innerHTML));
        $("#txtPhone").val($.trim(tr.children()[4].innerHTML));
        $("#txtAddress").val($.trim(tr.children()[5].innerHTML));
        $("#cmbTypeUser").val(typeU);
        $.unlockForm();
        $("input[type='button']").removeClass('disabled');
        $("input[type='button']").addClass('disabled');
        $("#btnGuardar").removeClass('disabled');
        $("#btnCancelar").removeClass('disabled');
        activeEdit = true;
    }

    $.deleteUser = function(button){
        var tr = $(button).parent().parent();
        idU = tr.attr('id');
        
        $.post("/main/logged_user/create_user/delete_users/", {"idU":idU})
        .done(function( response ) {
            if(response.delete){
                $.Notify.show("Eliminado Correctamente!!!");
            }else{
                $.Notify.show("Error al Eliminar usuario!!!");
            }
            $("#"+idU).fadeOut('fast', function() {
               $(this).remove(); 
            });
        });
    }

});