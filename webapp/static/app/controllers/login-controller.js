'use strict';

angular.module('capsuleApp').controller('LoginController', ['URLS', '$location', '$scope', 'Authentication', '$window',
    function(URLS, $location, $scope, Authentication, $window){
        activate();
        function activate(){
            Authentication.isAuthenticated().then(
                function(data){
                    if(data.loggedIn) {
                        $location.url(URLS.INDEX);
                    }
                },
                function(data){
                    $scope.serverError = 'Error connecting to server.Retry.';
                }
            );
        }
        $scope.login = function(){
            Authentication.login($scope.user).then(
            function(data){
                $location.url(URLS.INDEX);
                $window.location.reload();
            },
            function(data){
                $scope.formError = "Invalid Login Details";
            }
            );
        }
}]);