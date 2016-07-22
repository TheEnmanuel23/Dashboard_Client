 $(function(){
	 app = new dbClient.Views.app();
	 window.Collections.indicadoresTableValues = new dbClient.Collections.IndicadorTableValues();
	 window.Views.indicadoresTableValues = new dbClient.Views.IndicadoresTableValues({
	 		model: window.Collections.indicadoresTableValues
	 	});
	 var indicadoresTableValuesLoaded = window.Collections.indicadoresTableValues.fetch({
	 	data : {
				section: 'PET',
				idProject: '1',
				format: 'json'
			}
	 });
 });