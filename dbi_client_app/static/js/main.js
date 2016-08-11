 $(function(){
	 app = new dbClient.Views.app();
	 app.loadImage();

	 // Esto está correcto pero se va a llamar al dar click a una region y ya no desde la carga de la ventana
	 /*
	 window.Collections.indicadoresTableValues = new dbClient.Collections.IndicadorTableValues();
	 window.Views.indicadoresTableValues = new dbClient.Views.IndicadoresTableValues({
	 		model: window.Collections.indicadoresTableValues
	 	});
	 var indicadoresTableValuesLoaded = window.Collections.indicadoresTableValues.fetch({
	 	data : {
				section: 'COII',
				idProject: '1',
				format: 'json'
			}
	 });
	 */
 });