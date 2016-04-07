'use strict';

angular.module('capsuleApp').controller('editAssignmentController', ['ADMIN', 'Authentication', '$location', '$scope', '$routeParams', 'FacultyAssignment', 'FacultyProblem',
function(ADMIN, Authentication, $location, $scope, $routeParams, FacultyAssignment, FacultyProblem) {
    activate();
    var assignmentID;
    function activate() {
        assignmentID = $routeParams.assignmentID;
        window.scroll(0, 0);
        Authentication.isAuthenticated().then(
            function(data) {
                if(!data.loggedIn) {
                    $location.url(URLS.LOGIN);
                }
                else{
                    FacultyAssignment.getAssignment(assignmentID).then(
                        function(data) {
                            $scope.assignment = data;
                            $scope.assignment.deadline = new Date($scope.assignment.deadline);
                            FacultyProblem.listProblem(assignmentID).then(
                                function(data) {
                                    $scope.problems = data;
                                },
                                function(data) {
                                    $scope.error = data;
                                }
                            )
                        },
                        function(data){
                            $scope.error = data;
                        }
                    )
                }
            },
            function(data) {
                $scope.error = 'Error connecting to server.Retry.';
            }
        );
    }

    $scope.updateAssignment = function() {
        if($scope.form.$invalid)
            return;

        FacultyAssignment.editAssignment(assignmentID, $scope.assignment).then(
            function(data) {
                $scope.assignment = data;
                $scope.assignment.deadline = new Date($scope.assignment.deadline);
            },
            function(data) {
                $scope.error = data;
            }
        )
    };

    $scope.gotoProblem = function(index) {
        $location.url('assignment/' + assignmentID + '/problems/' + $scope.problems[index].id);
    };

    $scope.deleteProblem = function(index, $event) {
        $event.stopPropagation();
        FacultyProblem.deleteProblem(assignmentID, $scope.problems[index].id).then(
            function(data) {
                FacultyProblem.listProblem(assignmentID).then(
                    function(data) {
                        $scope.problems.splice(index, 1);
                    },
                    function(data) {
                        $scope.error = data;
                    }
                );
            },
            function(data) {
                $scope.error = data;
            }

        )
    };

    $scope.addProblem = function() {
        $location.url('assignment/' + assignmentID + '/problems/add');
    }


}]);