'use strict';

angular.module('capsuleApp').controller('TestcaseController', ['ADMIN', 'Authentication', '$location', '$scope', '$routeParams', 'FacultyProblem',
function(ADMIN, Authentication, $location, $scope, $routeParams, FacultyProblem) {
    activate();
    var assignmentID;
    var problemID;
    function activate() {
        assignmentID = $routeParams.assignmentID;
        problemID = $routeParams.problemID;
        window.scroll(0, 0);
        Authentication.isAuthenticated().then(
            function(data) {
                if(!data.loggedIn) {
                    $location.url(URLS.LOGIN);
                }
            },
            function(data) {
                $scope.error = 'Error connecting to server.Retry.';
            }
        );
    }

    $scope.submit = function() {
        if($scope.form.$invalid)
            return;
        FacultyProblem.addProblem(assignmentID, $scope.problem).then(
            function(data) {
                $location.url('assignment/' + assignmentID);
            },
            function(data) {
                $scope.error = data;
            }
        )
    }
}]);