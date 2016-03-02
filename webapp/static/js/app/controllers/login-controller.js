'use strict';

angular.module('userApp').controller('LoginController', ['URLS', '$location', '$scope', 'Authentication',
    function(URLS, $location, $scope, Authentication){
        activate();
        function activate(){
            if(Authentication.isAuthenticated()){
              $location.url(URLS.UPDATE);
            }
        }
        $scope.login = function(){
            Authentication.login($scope.email, $scope.password).then(
            function(data){
                $location.url(URLS.UPDATE);
            },
            function(data){
                $scope.formState = "Invalid Login Details";
            }
            );
        }
}]);