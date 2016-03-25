'use strict';

angular.module('capsuleApp').controller('assignmentFacultyController', ['ADMIN', 'Authentication', '$location', '$scope', 'FacultyAssignment',
function(ADMIN, Authentication, $location, $scope, FacultyAssignment){
    activate();
    function activate(){
        Authentication.isAuthenticated().then(
            function(data){
                if(!data.loggedIn) {
                    $location.url(URLS.LOGIN);
                }
                else{
                    FacultyAssignment.getFacultyAssignmentList().then(
                        function (data) {
                            $scope.assignment = data;
                        },
                        function(data) {
                            $scope.error = 'Error loading assignments';
                        }
                    );
                }
            },
            function(data){
                $scope.error = 'Error connecting to server.Retry.';
            }
        );
    }

    $scope.gotoAssignment = function(index){
        $location.url(ADMIN.LIVE_A + '/' + $scope.assignment[index].id);
    }
}]);