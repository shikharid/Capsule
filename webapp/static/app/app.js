'use strict';

angular.module('capsuleApp', [
    'restangular',
    'ngRoute',
    'ngAnimate',
    'ngCookies',
    'ngMaterial',
    'angular-loading-bar'
]).run(['$http', function($http){
      $http.defaults.xsrfHeaderName = 'X-CSRFToken';
      $http.defaults.xsrfCookieName = 'csrftoken';
    }]);
