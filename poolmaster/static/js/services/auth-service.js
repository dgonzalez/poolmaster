function AuthService($cookies, $http, $rootScope) {
  this.$cookies = $cookies;
  this.$http = $http;
  this.$rootScope = $rootScope;
}

AuthService.prototype.login = function(username, password) {
    var data = {
      'username': username,
      'password': password
    }
    return this.$http.post('/api-token-auth/', data);
}
