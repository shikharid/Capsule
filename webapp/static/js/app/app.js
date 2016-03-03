''

angular.module('userApp', [
  'restangular',
  'ngRoute',
  'ngAnimate',
  'ngCookies'
]).run(['$http', function($http){
      $http.defaults.xsrfHeaderName = 'X-CSRFToken';
      $http.defaults.xsrfCookieName = 'csrftoken';
    }]);


