$(function(){
	
	var content =''+ 
    	'<form id="frmChangePassword">'+
	    	'<label>Contraseña Anterior:</label>'+
	    	'<div class="input-control password">'+
		    	'<input type="password" name="passwordLost" maxlength="16" pattern=".{8,16}" required title="Debe tener entre 8 a 16 caracteres">'+
		    	'<button class="btn-reveal"></button>'+
	    	'</div>'+
	    	'<label>Nueva Contraseña:</label>'+
		    '<div class="input-control password">'+
		    	'<input type="password" name="passwordNew" maxlength="16" pattern=".{8,16}" required title="Debe tener entre 8 a 16 caracteres">'+
		    	'<button class="btn-reveal"></button>'+
		    '</div>'+
		    '<div class="form-actions">'+
		    	'<button class="button primary">Guardar</button>&nbsp;'+
		    	'<button class="button warning" type="button" onclick="$.Dialog.close()">Cancelar</button>'+
		    '</div>'+
	    '</form>';

	$("#changePassword").click(function(){
		$.DIALOG(content,15,250,"Modificar Contraseña","icon-cog");
	});
	
	$("#changePasswordTb").click(function(){
		$.DIALOG(content,15,250,"Modificar Contraseña","icon-cog");
	});
	
});