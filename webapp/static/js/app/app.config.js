'use strict';
    angular.module('userApp').config(['URLS', 'PARTIALS', '$routeProvider', '$locationProvider', 'RestangularProvider',
        function(URLS, PARTIALS, $routeProvider, $locationProvider, RestangularProvider) {

            RestangularProvider.setBaseUrl(URLS.BASE_URL);

            $locationProvider.html5Mode(true);
            $locationProvider.hashPrefix('!');

            $routeProvider.
                when(URLS.REGISTER, {
                    controller: 'RegisterController',
                    templateUrl: PARTIALS.REGISTER
                }).
                when(URLS.LOGIN, {
                    controller: 'LoginController',
                    templateUrl: PARTIALS.LOGIN
                }).
                when(URLS.LOGOUT, {
                    controller: 'LogoutController',
                    templateUrl: PARTIALS.LOGOUT
                }).
                when(URLS.INDEX, {
                    controller: 'DashboardController',
                    templateUrl: PARTIALS.INDEX
                }).
                when(URLS.UPDATE, {
                    controller: 'ProfileUpdateController',
                    templateUrl: PARTIALS.UPDATE
                }).
                when(URLS.LIST, {
                    controller: "UserListController",
                    templateUrl: PARTIALS.LIST_TEMPLATE
                }).
                otherwise({
                    redirectTo: URLS.INDEX
                });
    }]);