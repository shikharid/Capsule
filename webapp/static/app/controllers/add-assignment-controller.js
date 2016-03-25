'use strict';

angular.module('capsuleApp').controller('addAssignmentController', ['ADMIN', 'Authentication', '$location', '$scope', 'FacultyAssignment',
function(ADMIN, Authentication, $location, $scope, FacultyAssignment){
    activate();
    function activate(){
        Authentication.isAuthenticated().then(
            function(data){
                if(!data.loggedIn) {
                    $location.url(URLS.LOGIN);
                }
            },
            function(data){
                $scope.error = 'Error connecting to server.Retry.';
            }
        );
    }

    $scope.submit = function(){
        if($scope.form.$invalid)
            return;
        FacultyAssignment.addAssignment($scope.assignment).then(
            function(data){
                $location.url(ADMIN.LIVE_A);
            },
            function(data){
                console.log('Response' + data);
            }
        );
    };

}]);