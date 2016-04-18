'use strict';

angular.module('capsuleApp').controller('problemListController', ['$sce', '$routeParams', 'URLS', 'Authentication', '$location', '$scope', 'Problem',
function($sce, $routeParams, URLS, Authentication, $location, $scope, Problem){
    activate();
    function activate(){
        Authentication.isAuthenticated().then(
            function(data){
                if(!data.loggedIn) {
                    $location.url(URLS.LOGIN);
                }
                else{
                    Problem.getProblemList($routeParams.id).then(
                        function(data){
                            $scope.problems = data;
                        },
                        function(data){
                            $scope.error = 'Error retrieving Problem Set.Confirm that you are allowed to access the assignment from your faculty and retry';
                        }
                    );

                }
            },
            function(data){
                $scope.error = 'Error connecting to server.Retry.';
            }
        );
    }

    $scope.goToProblem = function (idx) {
        console.log(URLS.PENDING + '/' + $routeParams.id + '/' + $scope.problems[idx].id);
        $location.url(URLS.PENDING + '/' + $routeParams.id + '/' + $scope.problems[idx].id);
    };
}]);

angular.module('capsuleApp').controller('problemSolveController', ['$sce', '$routeParams', 'URLS', 'Authentication', '$location', '$scope', 'Problem',
function($sce, $routeParams, URLS, Authentication, $location, $scope, Problem){
    var assignmentID, problemID;
    activate();
    function activate(){
        assignmentID = $routeParams.id;
        problemID = $routeParams.problemID;
        Authentication.isAuthenticated().then(
            function(data){
                if(!data.loggedIn) {
                    $location.url(URLS.LOGIN);
                }
                else{
                    Problem.getProblemList($routeParams.id).then(
                        function(data){
                            $scope.problems = data;
                        },
                        function(data){
                            $scope.error = 'Error retrieving Problem Set.Confirm that you are allowed to access the assignment from your faculty and retry';
                        }
                    );

                }
            },
            function(data){
                $scope.error = 'Error connecting to server.Retry.';
            }
        );
    }

    $scope.goToProblem = function (idx) {
        console.log(URLS.PENDING + '/' + $routeParams.id + '/' + $scope.problems[idx].id);
        $location.url(URLS.PENDING + '/' + $routeParams.id + '/' + $scope.problems[idx].id);
    };

    $scope.solveProblem = function(problemId) {
                            // Link to solve problem
                            console.log(problemId);
                        };

    $scope.convertToSafe = function(unsafe) {
        return $sce.trustAsHtml(unsafe);
    };
}]);