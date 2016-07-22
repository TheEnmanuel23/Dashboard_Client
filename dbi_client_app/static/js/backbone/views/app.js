dbClient.Views.app = Backbone.View.extend({
	el: $('body'),
	initialize: function(){
		console.log("inicidado");
	},
	events: {
		'click .indicador-visibles li a': 'indicador_click',
	},
	indicador_click: function(e){
		e.preventDefault();
		id = $(e.currentTarget).attr('id');
	},
	loadImage: function(){
		var workSpace = Snap("#container-image");
		var url = '../../../static/img/Guatemala_Regiones_Enmanuel.svg';
		Snap.load(url, function ( data ) {
		   	workSpace.append(data);
		});
	}
});