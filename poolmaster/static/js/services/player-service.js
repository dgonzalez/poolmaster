function PlayerService($http) {
  this.$http = $http;
}

PlayerService.prototype.getMatches = function() {
  return this.$http.get("/allmatches/");
}
