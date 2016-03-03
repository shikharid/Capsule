'use strict';

angular.module('capsuleApp', [
    'restangular',
    'ngRoute',
    'ngAnimate',
    'ngCookies',
    'ngMaterial'
]).run(['$http', function($http){
      $http.defaults.xsrfHeaderName = 'X-CSRFToken';
      $http.defaults.xsrfCookieName = 'csrftoken';
    }]).controller('LoginController', function(){});
