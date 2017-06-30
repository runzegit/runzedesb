$.post('/desbbusca/', {busca: ''}, function(data){
	$('#table-clientes').html(data);
});

$('li.active').removeClass('active');
$('a[href="' + location.pathname + '"]').closest('li').addClass('active'); 
$('.cliente').on('click', function(e){
	e.preventDefault();
	$.post('', {cliente_id: $(this).attr('id')}, function(data){
		$('#cliente_list').html(data);
	});
});
// $('.bloqueado').on('click', function(e){
// 	$.post('/cliente/bloqueado/', {id: $(this).attr('alt')}, function(data){});	
// 	if($(this).is(':checked'))
// 		$(this).siblings('div').html("Bloqueado");
// 	else
// 		$(this).siblings('div').html("Desbloqueado");
// });
// $('.ativo').on('click', function(e){
// 	$.post('/cliente/bloqueado/', {id: $(this).attr('alt'), status: 'ativo'}, function(data){});	
// 	if($(this).is(':checked'))
// 		$(this).siblings('div').html("Inativo");
// 	else
// 		$(this).siblings('div').html("Ativo");
// });
$('#busca').keyup(function(){
	var texto = $(this).val();
	if (texto.length>3){
		$.post('busca/', {busca: texto}, function(data){
			$('#side-menu').html(data);
		});	
	}else if(texto.length==0){
		$.post('busca/', {busca: ''}, function(data){
			$('#side-menu').html(data);
		});
	}
});
$('#busca-cliente').keyup(function(){
	var texto = $(this).val();
	if (texto.length>3){
		$.post('/desbbusca/', {busca: texto}, function(data){
			$('#table-clientes').html(data);
		});	
	}else if(texto.length==0){
		$.post('/desbbusca/', {busca: ''}, function(data){
			$('#table-clientes').html(data);
		});
	}
});

$('#btn-salvar-modal').on('click', function(e){
	e.preventDefault();
	if ($('#data-pag').val()=="" || $('#mesref').val()=="" || $('#id-cliente').val()==""){
		return;	
	}
	var parse = $('#data-pag').val().split('/');
	var data = parse[2]+'-'+parse[1]+'-'+parse[0];
	var mes = $('#mesref').val();
	var id = $('#id-cliente').val();
	$.post('/bloqueado/', {id: id, data: data, mes: mes, pagamento: 'pagamaneto'}, function(dados){
		$('table tbody tr').each(function(){
			var colunas =  $(this).children();
			if ($(colunas[3]).find('button').attr('alt')==id){	
				$(colunas[3]).find('.span-data').html(dados.datPagF);
				$(colunas[3]).find('.span-mes').html(dados.mesRef);
				//$(colunas[3]).html(dados);
				var parse = $(colunas[4]).attr('alt').split('||');
				$(colunas[4]).attr('alt', parse[0]+'||'+data+'||'+mes);
				var parse = $(colunas[4]).attr('alt').split("||");
				var diaVen = (parse[0].trim().length==1?'0'+parse[0].trim():parse[0].trim());
				var datPag = new Date(parse[1]);
				var mesRef = (parse[2].trim().length==1?'0'+parse[2].trim():parse[2].trim());
				var stringDataParse = datPag.getFullYear()+'-'+mesRef+'-'+diaVen;
				var dataRef = new Date(stringDataParse);
				dataRef.setDate(dataRef.getDate()+45);
				var dias = Math.round((dataRef- new Date())/(1000 * 60 * 60 * 24));
				if(dias<11 && dias >=0)
					$(this).addClass('bg-warning');
				else if (dias < 0)
					$(this).addClass('bg-danger');
				$(colunas[4]).html(dias);
			}
		});

	});
	$('#myModal').modal('toggle');	
});

$(function () {
	$('#datetimepicker1').datepicker({
	    format: 'dd/mm/yyyy',
	    todayHighlight: true,
	    autoclose: true,
	}).datepicker("setDate", new Date());
	$('#mesref').val(new Date().getMonth()+1);
});