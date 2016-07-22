dbClient.Views.IndicadoresTableValues = Backbone.View.extend({
	el: $('body'),
	initialize: function(){
		this.model.on('add', this.render);
	},
	render: function(indicadorRow){
		if(indicadorRow.view == null){
			indicadorRow.view = new indicadorValueRow({
				model: indicadorRow
			});
		}
		indicadorRow.view.render();
		indicadorRow.view.$el.appendTo('#indicador-table-values');
	}
});

indicadorValueRow = Backbone.View.extend({
	render: function(){
		template = _.template($('#indicadores-tables-values-template').html())
		html = template(this.model.toJSON());
		this.setElement(html);
		return this;
	}
});