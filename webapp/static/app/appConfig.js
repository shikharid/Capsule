'use strict';

angular.module('capsuleApp').config(['URLS', 'PARTIALS', '$routeProvider', '$locationProvider', 'RestangularProvider', '$mdThemingProvider', 'ADMIN',
    function(URLS, PARTIALS, $routeProvider, $locationProvider, RestangularProvider, $mdThemingProvider, ADMIN) {

        RestangularProvider.setBaseUrl(URLS.BASE_URL);

        $mdThemingProvider.theme('landingTheme')
            .primaryPalette('indigo')
            .backgroundPalette('blue', {default: '400'});

        $mdThemingProvider.theme('loginCardTheme')
            .primaryPalette('light-blue')
            .warnPalette('green');

        $mdThemingProvider.theme('default').primaryPalette('light-blue').warnPalette('pink');
        $mdThemingProvider.theme('default-form').primaryPalette('cyan');
        $mdThemingProvider.theme('code-dark').primaryPalette('blue-grey', {
                  'default': '400', // by default use shade 400 from the pink palette for primary intentions
                  'hue-1': '100', // use shade 100 for the <code>md-hue-1</code> class
                  'hue-2': '600', // use shade 600 for the <code>md-hue-2</code> class
                  'hue-3': 'A100' // use shade A100 for the <code>md-hue-3</code> class
                }).warnPalette('deep-orange').dark();

        $mdThemingProvider.theme('default-dark').primaryPalette('blue-grey').accentPalette('red').dark();
        $mdThemingProvider.theme('notify').primaryPalette('light-green').accentPalette('deep-orange')
            .warnPalette('amber');

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
            when(ADMIN.LIVE_A, {
                controller: 'assignmentFacultyController',
                templateUrl: PARTIALS.ASSIGNMENT_LIST
            }).
            when(ADMIN.COMPLETE_A, {
                controller: 'reviewAssignmentListController',
                templateUrl: PARTIALS.COMP_ASSIGN_LIST
            }).
            when(ADMIN.EVAL_A, {
                controller: 'reviewAssignmentController',
                templateUrl: PARTIALS.REVIEW_ASS
            }).
            when(ADMIN.REVIEW_A, {
                controller: 'reviewStudentAssignmentController',
                templateUrl: PARTIALS.REVIEW_STU
            }).
            when(ADMIN.REVIEW_P, {
                controller: 'reviewStudentSubmissionController',
                templateUrl: PARTIALS.REVIEW_SUB
            }).
            when(ADMIN.ADD_A, {
                controller: 'addAssignmentController',
                templateUrl: PARTIALS.ASSIGNMENT_ADD
            }).
            when(ADMIN.EDIT_A, {
                controller: 'editAssignmentController',
                templateUrl: PARTIALS.ASSIGNMENT_EDIT
            }).
            when(ADMIN.ADD_P, {
                controller: 'addProblemController',
                templateUrl: PARTIALS.PROBLEM_ADD
            }).
            when(ADMIN.EDIT_P, {
                controller: 'editProblemController',
                templateUrl: PARTIALS.PROBLEM_EDIT
            }).
            otherwise({
                redirectTo: URLS.INDEX
            });
}]);