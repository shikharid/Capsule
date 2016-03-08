'use strict';

angular.module('capsuleApp').controller('pendingController', ['URLS', 'Authentication', '$location', '$scope', 'Assignment',
function(URLS, Authentication, $location, $scope, Assignment){
    var COLORS = ['#FF5252', '#FF4081', '#E040FB', '#7C4DFF', '#8C9EFF', '#82B1FF', '#80D8FF', '#A7FFEB', '#69F0AE', '#B2FF59'];
    activate();
    function activate(){
        Authentication.isAuthenticated().then(
            function(data){
                if(!data.loggedIn) {
                    $location.url(URLS.LOGIN);
                }
                else{
                    Assignment.getStudentAssignmentList().then(
                        function (data) {
                            $scope.assignment = data;
                            for(var i = 0;i < $scope.assignment.length; ++i){
                                $scope.assignment[i]['color'] = COLORS[Math.floor(Math.random()*COLORS.length)];
                            }
                        },
                        function(data) {
                            $scope.error = 'Error loading pending assignments';
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
        $location.url(URLS.PENDING + '/' + $scope.assignment[index].id);
    }
}]);