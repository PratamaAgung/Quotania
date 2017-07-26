// Author 		: Pratamamia Agung P
// Description	: Module for running angularJS application

var currentQuoteId = 0;
var quotApp = angular.module('quotania', []);
var no_data = false;
//Controller for submitting quotes
quotApp.controller('submitController', function($scope, $http){
	$scope.submitStatus = 0;

	//Function for submit a quote
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
		        		if (no_data == true){
		        			location.reload();
		        		}
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

//Controller for handling viewing function
quotApp.controller('viewController', function($scope, $http){
	//Initializer
	$scope.showQuote = true;
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
			$scope.showBefore = response.data.before;
			$scope.showNext = response.data.next;
			currentQuoteId = response.data.id;
		} else {
			$scope.showQuote = false;
			no_data = true;
		}
	});

	//Function for getting next quote in ranking
	$scope.next = function() {
		$http({
			url : next_quote_url,
			method : 'POST',
			params : {id : currentQuoteId}
		}).then(function(response) {
			if (response.data.quote != null){
				$scope.quote = {
					quo : response.data.quote,
					auth : response.data.author,
					nbLike : response.data.nbLike
				};
				$scope.showBefore = response.data.before;
				$scope.showNext = response.data.next;
				currentQuoteId = response.data.id;
			}
		});
	};
	
	//Function for getting preceding quote in ranking
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
				$scope.showBefore = response.data.before;
				$scope.showNext = response.data.next;
				currentQuoteId = response.data.id;
			}
		});
	};

	//Function for handling like
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

	$scope.refreshnavigator = function() {
		$http({
			url : refresh_navigator_url,
			method : 'POST',
			params : {id : currentQuoteId}
		}).then(function(response) {
			$scope.quote.nbLike = response.data.nbLike;
			$scope.showNext = response.data.next;
			$scope.showBefore = response.data.before;
		});
	}

	setInterval(function(){
		$scope.refreshnavigator();
	}, 1000);
});