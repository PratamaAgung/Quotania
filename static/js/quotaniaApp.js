var currentQuoteId = 0;

var quotApp = angular.module('quotania', []);
quotApp.controller('submitController', function($scope, $http){
	$scope.submitStatus = 0;
	$scope.submit = function() {
		if (!$scope.submit.quo.length || !$scope.submit.auth.length) {
			$scope.submitStatus = 2;
		} else {
			try{
				$http({
		        	url : submit_quote_url,
		        	method : 'POST',
		        	params : {quote : $scope.submit.quo, author : $scope.submit.auth}
		        }).then(function(response) {
		        	if (response.data.status){
		        		$scope.submitStatus = 1;
		        	} else {
		        		$scope.submitStatus = -1;
		        	}
		        });
			} catch(err) {
				$scope.submitStatus = -1;
			}
		}
        $scope.submit.quo = '';
        $scope.submit.auth = '';
	};
});

quotApp.controller('viewController', function($scope, $http){
	$http({
		url : init_quote_url,
		method : 'GET'
	}).then(function(response){
		if (response.data.quote != null){
			$scope.quote = {
				quo : response.data.quote,
				auth : response.data.author,
				nbLike : response.data.nbLike
			};
			currentQuoteId = response.data.id;
		}
	});
	$scope.showQuote = true;

	$scope.next = function() {
		$http({
			url : next_quote_url,
			method : 'POST',
			params : {id : currentQuoteId}
		}).then(function(response) {
			if (response.data.quote != null){
				$scope.showQuote = false;
				$scope.quote = {
					quo : response.data.quote,
					auth : response.data.author,
					nbLike : response.data.nbLike
				};
				currentQuoteId = response.data.id;
			}
		});
	};
	
	$scope.before = function() {
		$http({
			url : before_quote_url,
			method : 'POST',
			params : {id : currentQuoteId}
		}).then(function(response) {
			if (response.data.quote != null){
				$scope.quote = {
					quo : response.data.quote,
					auth : response.data.author,
					nbLike : response.data.nbLike
				};
				currentQuoteId = response.data.id;
			}
		});
	};

	$scope.like = function() {
		$http({
			url : like_url,
			method : 'POST',
			params : {id : currentQuoteId}
		}).then(function(response) {
			if (response.data.status) {
				$scope.quote.nbLike++;
			}
		});
	};
});