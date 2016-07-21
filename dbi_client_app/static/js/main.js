 $(function(){
	 app = new dbClient.Views.app();
	 window.Collections.indicadoresTableValues = new dbClient.Collections.IndicadorTableValues();
	 var indicadoresTableValuesLoaded = window.Collections.indicadoresTableValues.fetch({
	 	data : {
				section: 'PET',
				idProject: '1',
				format: 'json'
			}
	 });
	 indicadoresTableValuesLoaded.then(function(){
	 	console.log(window.Collections.indicadoresTableValues.toJSON());
	 });
 });