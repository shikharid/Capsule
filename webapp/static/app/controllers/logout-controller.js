'use strict';

angular.module('capsuleApp').controller('LogoutController', ['URLS', '$location', '$scope', 'Authentication', '$route', '$window',
    function(URLS, $location, $scope, Authentication, $route, $window){
        activate();
        function activate(){
            Authentication.logout().then(
                function(data){
                    $location.url(URLS.LOGIN);
                    $window.location.reload();
                },
                function(data){
                    $scope.serverError = 'Error connecting to server.Retry.';
                }
            );
        }
}]);