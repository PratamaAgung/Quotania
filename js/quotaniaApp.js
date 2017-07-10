var quotApp = angular.module('quotania', []);
quotApp.controller('quotController', function($scope){
	$scope.submitStatus = 0;
	$scope.quote = {quo:"This is my quote", auth:"And I'm the author"};
	$scope.submit = function() {
		$scope.quote = $scope.submit;
        $scope.submit = null;
        $scope.submitStatus =1;
	};
});