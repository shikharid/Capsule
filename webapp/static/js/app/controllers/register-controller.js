'use strict';

angular.module('userApp').controller('RegisterController', ['URLS', '$location', '$scope', 'Authentication',
    function(URLS, $location, $scope, Authentication) {
        $scope.user = {};

        activate();

        function activate(){
            if(Authentication.isAuthenticated()){
                $location.url(URLS.INDEX);
            }
        }

        $scope.register = function() {
            $scope.formState = '';

            if($scope.password != $scope.confirm_password) {
                $scope.form.$valid = false;
            }

            if($scope.form.$valid) {
                Authentication.register($scope.user).then(function (data) {
                        $scope.formState = "Successfully registered.Login to continue";
                    }, function (data) {

                        for (var key in data.data) {
                            if ((key in $scope.form)) {
                                $scope.form[key].$invalid = true;
                                $scope.form[key].error = data.data[key][0];
                            } else {
                                $scope.formState = data.data[key][0];
                            }
                        }
                    });
            }
            else{
                $scope.formState = 'Please correct the errors';
            }
        }
}]);