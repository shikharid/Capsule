'use strict';

angular.module('capsuleApp').config(['URLS', 'PARTIALS', '$routeProvider', '$locationProvider', 'RestangularProvider', '$mdThemingProvider',
    function(URLS, PARTIALS, $routeProvider, $locationProvider, RestangularProvider, $mdThemingProvider) {

        RestangularProvider.setBaseUrl(URLS.BASE_URL);

        $mdThemingProvider.theme('landingTheme')
            .primaryPalette('light-blue')
            .backgroundPalette('blue', {default: '400'});

        $mdThemingProvider.theme('loginCardTheme')
            .primaryPalette('light-blue')
            .warnPalette('green');

        $mdThemingProvider.theme('default').primaryPalette('light-blue').warnPalette('pink');

        $mdThemingProvider.theme('default-dark').primaryPalette('light-blue').warnPalette('pink').dark();

        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');

        $routeProvider.
            when(URLS.LOGIN, {
                controller: 'LoginController',
                templateUrl: PARTIALS.LOGIN
            }).
            when(URLS.LOGOUT, {
                controller: 'LogoutController',
                templateUrl: PARTIALS.LOGOUT
            }).
            when(URLS.EDITOR, {
                controller: 'editorController',
                templateUrl: PARTIALS.EDITOR
            }).
            when(URLS.PENDING, {
               controller: 'pendingController',
                templateUrl: PARTIALS.PENDING
            }).
            when(URLS.PENDING_PROBLEMS, {
               controller: 'problemListController',
                templateUrl: PARTIALS.PROBLEM_LIST
            }).
            otherwise({
                redirectTo: URLS.INDEX
            });
}]);