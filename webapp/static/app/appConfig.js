'use strict';

angular.module('capsuleApp').config(['URLS', 'PARTIALS', '$routeProvider', '$locationProvider', 'RestangularProvider', '$mdThemingProvider',
    function(URLS, PARTIALS, $routeProvider, $locationProvider, RestangularProvider, $mdThemingProvider) {

        RestangularProvider.setBaseUrl(URLS.BASE_URL);
        $mdThemingProvider.theme('landingTheme')
    .primaryPalette('light-blue').backgroundPalette('blue', {default: '400'});
        $mdThemingProvider.theme('loginCardTheme')
    .primaryPalette('light-blue')
        .warnPalette('green');
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');

        $routeProvider.
            when(URLS.LOGIN, {
                //controller: 'LoginController',
                templateUrl: PARTIALS.LOGIN
            }).
            when(URLS.LOGOUT, {
                //controller: 'LogoutController',
                templateUrl: PARTIALS.LOGOUT
            }).
            otherwise({
                redirectTo: URLS.INDEX
            });
}]);