var myApp = angular.module('tournaments',['ngRoute', 'ngCookies']);

myApp.service("playerService", function($http) {
  return new PlayerService($http);
});

myApp.service("authService", function($cookies, $http, $rootScope) {
  return new AuthService($cookies, $http, $rootScope);
});


myApp.controller('LoginController', function($scope, $location, $cookies,
                                             authService, $rootScope) {
    $scope.username = "";
    $scope.password = "";
    $scope.loginError = "";
    $scope.loginAction = function() {
        promise = authService.login($scope.username, $scope.password);
        promise.then(
            function(data) {
                $rootScope.authToken = data.data.token;
                $location.path('/home');
            },
            function(response) {
                $scope.loginError = response.data.non_field_errors[0];
        });
    }
});

myApp.controller('HomeController', function($scope, playerService) {
    playerService.getMatches().then(function(value) {
      $scope.matches = value.data;
    });
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

