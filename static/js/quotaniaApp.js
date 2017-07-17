var quotApp = angular.module('quotania', []);
quotApp.controller('submitController', function($scope, $http){
	$scope.submitStatus = 0;
	$scope.submit = function() {
		if ($scope.submit.quo == '' || $scope.submit.auth == '') {
			$scope.submitStatus = 2;
		} else {
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
		}
        $scope.submit.quo = '';
        $scope.submit.auth = '';
	};
});

quotApp.controller('viewController', function($scope, $http){
	$http({
		url : get_quote_after_url,
		method : 'POST',
		params : {}
	});
});