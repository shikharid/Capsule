'use strict';

angular.module('capsuleApp').controller('LogoutController', ['URLS', '$location', '$scope', 'Authentication',
    function(URLS, $location, $scope, Authentication){
        activate();
        function activate(){
            Authentication.logout().then(
                function(data){
                        $location.url(URLS.INDEX)
                },
                function(data){
                    $scope.serverError = 'Error connecting to server.Retry.';
                }
            );
        }
}]);