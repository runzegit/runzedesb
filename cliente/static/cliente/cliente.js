$('.cliente').on('click', function(e){
	e.preventDefault();
	$.post('', {cliente_id: $(this).attr('id')}, function(data){
		$('#cliente_list').html(data);
	});
});
$('.bloqueado').on('click', function(e){
	$.post('/bloqueado/', {id: $(this).attr('alt')}, function(data){});	
	if($(this).is(':checked'))
		$(this).siblings('div').html("Bloqueado");
	else
		$(this).siblings('div').html("Desbloqueado");
});
$('.ativo').on('click', function(e){
	$.post('/bloqueado/', {id: $(this).attr('alt'), status: 'ativo'}, function(data){});	
	if($(this).is(':checked'))
		$(this).siblings('div').html("Inativo");
	else
		$(this).siblings('div').html("Ativo");
});
$('table tbody tr').each(function(){
	var colunas =  $(this).children();
	var parse = $(colunas[4]).attr('alt').split("||");
	var diaVen = (parse[0].trim().length==1?'0'+parse[0].trim():parse[0].trim());
	var datPag = new Date(parse[1]);
	var mesRef = (parse[2].trim().length==1?'0'+parse[2].trim():parse[2].trim());
	var stringDataParse = datPag.getFullYear()+'-'+mesRef+'-'+diaVen;
	var dataRef = new Date(stringDataParse);
	dataRef.setDate(dataRef.getDate()+45);
	var dias = Math.round((dataRef-new Date())/(1000 * 60 * 60 * 24));
	if(dias<11 && dias >=0)
		$(this).addClass('bg-warning');
	else if (dias < 0)
		$(this).addClass('bg-danger');

	$(colunas[4]).html(dias);
});

$('.btn-modal').on('click', function(){
	$('#id-cliente').val($(this).attr('alt'));
	//$(this).click();
});

$('#cliente_btn_excluir').on('click', function(e){
	e.preventDefault();
	var resultado = confirm("Deseja remover o cliente?");
	if (resultado)
		$.post('/delete/', {id: $(this).attr('alt')}, function(data){
			$.post('busca/', {busca: ''}, function(data){
				$('#cliente_list').html('');
				$('#side-menu').html(data);
			});
		});
});