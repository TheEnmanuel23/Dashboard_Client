dbClient.Views.app = Backbone.View.extend({
	el: $('body'),
	initialize: function(){
		console.log("inicidado");
	},
	events: {
		'click .indicador-visibles li a': 'indicador_click',
		'click .dropdown-menu li a': 'select_filter'
	},
	indicador_click: function(e){
		e.preventDefault();
		id = $(e.currentTarget).attr('id');
	},
	select_filter: function(e){
		e.preventDefault();
	 	var selText = $(e.currentTarget).text();
		$(e.currentTarget).parents('.btn-group').find('.dropdown-toggle').html(selText+' <span class="caret"></span>');
	},
	loadImage: function(){
		var workSpace = Snap("#container-image");
		var url = '../../../static/img/Guatemala_Regiones_Enmanuel.svg';
		Snap.load(url, function ( data ) {
		   	workSpace.append(data);
		});
	}
});