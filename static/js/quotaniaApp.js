var quotApp = angular.module('quotania', []);
quotApp.controller('quotController', function($scope, $http){
	$scope.submitStatus = 0;
	$scope.quote = {quo:"This is my quote", auth:"And I'm the author"};
	$scope.submit = function() {
		$scope.quote = $scope.submit;
		try{
			$http({
	        	url : submit_quote_url,
	        	method : 'POST',
	        	params : {quote : $scope.submit.quo, author : $scope.submit.auth}
	        }).then(function(response) {
	        	if (response.status){
	        		$scope.submitStatus = 1;
	        	} else {
	        		$scope.submitStatus = -1;
	        	}
	        });
		} catch(err) {
			$scope.submitStatus = -1;
		}
        $scope.submit = null;
	};
});