var myApp = angular.module('tournaments',['ngRoute']);

myApp.factory("$bleh", function($q) {
  return {
    test: function() {
    }
  }
});

myApp.controller('LoginController', function($scope, $location, $bleh){
    $scope.username = "";
    $scope.password = "";

    $scope.click = function() {
      console.log($bleh);
      $location.path("/home");
    };
});

myApp.controller('HomeController', function() {
});

myApp.config(function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl : '/static/pages/login.html',
            controller : 'LoginController'
        })
        .when('/home', {
            templateUrl : '/static/pages/home.html',
            controller : 'HomeController'
        })
});

